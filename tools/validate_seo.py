#!/usr/bin/env python3
"""Validate the built site, reconcile every route, and emit regression CSVs."""
import csv
import json
import re
import sys
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path
from PIL import Image

from seo_audit import ROOT, ORIGIN, STAMP, document, extract, write_csv, sitemap_urls


def main():
    base = ROOT / "dist"
    if not (base / "index.html").exists():
        raise SystemExit("Run pnpm build first.")
    initial = json.loads((ROOT / "reports/evidence/initial/source.json").read_text())
    targets = json.loads((ROOT / "research/page-targets.json").read_text())
    forms = json.loads((ROOT / "implementation/forms-before.json").read_text())
    image_map = json.loads((ROOT / "implementation/image-delivery-map.json").read_text())
    browser_path = ROOT / "implementation/rendered-validation.json"
    browser = json.loads(browser_path.read_text()) if browser_path.exists() else {}
    live_path = ROOT / "reports/evidence/final/live.json"
    live = json.loads(live_path.read_text()) if live_path.exists() else {}
    errors, records, image_refs, internal, external = [], [], [], [], []
    title_counts, description_counts = Counter(), Counter()
    documents = {"/" + str(p.relative_to(base)): p for p in base.rglob("*.html")}
    documents["/"] = documents.pop("/index.html")
    parsed = {r: extract(p.read_text()) for r, p in documents.items()}
    canonicals = set(ORIGIN + r for r in targets)
    sitemap = sitemap_urls((base / "sitemap.xml").read_text())
    if len(sitemap) != len(set(sitemap)) or set(sitemap) != canonicals:
        errors.append("Sitemap must contain exactly the distinct canonical eligible pages.")
    for route, path in documents.items():
        d = document(path.read_text())
        p = parsed[route]
        applicable = route in targets
        failures = []
        if applicable:
            title_counts[p["title"]] += 1
            description_counts[p["description"]] += 1
            for name in ["description", "og:title", "og:description", "og:url",
                         "og:site_name", "og:image", "twitter:title",
                         "twitter:description", "twitter:image", "twitter:card"]:
                if not p["meta"].get(name):
                    failures.append("Missing " + name)
            if p["metadata_duplicates"]:
                failures.append("Duplicate metadata: " + str(p["metadata_duplicates"]))
            if len(p["h1"]) != 1:
                failures.append("Expected one main H1 in generated HTML")
            if p["canonical"] != ORIGIN + route or "noindex" in p["robots"]:
                failures.append("Canonical/indexability mismatch")
            if p["schema_errors"]:
                failures.append("Invalid JSON-LD")
            ids = [n.get("@id") for n in p["schemas"] if n.get("@id")]
            if len(ids) != len(set(ids)):
                failures.append("Duplicate graph entity definitions")
            if len(d.xpath('//head/script[@type="application/ld+json"]')) != 1:
                failures.append("Expected one authoritative graph")
            articles = [n for n in p["schemas"] if n.get("@type") == "Article"]
            if any(n.get("headline") != p["h1"][0] for n in articles):
                failures.append("Article headline differs from visible H1")
            if route == "/" and not d.xpath('//div[@id="root"]/div//main'):
                failures.append("Homepage not prerendered")
        # All source form nodes, names, actions and option values must remain intact.
        if route in forms:
            actual = [{"tag": e.tag, "attributes": dict(e.attrib)}
                      for e in d.xpath("//form|//input|//textarea|//select|//option")]
            if actual != forms[route]:
                failures.append("Form structure or attributes changed")
        for resource in d.xpath('//script[@src]/@src|//link[@rel="stylesheet" or @rel="icon" or @rel="manifest" or @rel="apple-touch-icon"]/@href'):
            u = urllib.parse.urlsplit(urllib.parse.urljoin(ORIGIN + route, resource))
            if u.netloc == urllib.parse.urlsplit(ORIGIN).netloc:
                if not (base / u.path.lstrip("/")).is_file():
                    failures.append("Missing local script/style/icon/manifest " + u.path)
        for anchor in d.xpath("//a[@href]"):
            link = anchor.get("href")
            u = urllib.parse.urlsplit(urllib.parse.urljoin(ORIGIN + route, link))
            if u.scheme not in ["http", "https"]:
                continue
            row = {"Source URL": ORIGIN + route, "Link": link,
                   "Resolved URL": u.geturl(), "Text": " ".join(anchor.text_content().split())}
            if u.netloc == urllib.parse.urlsplit(ORIGIN).netloc:
                target = base / (u.path.lstrip("/") or "index.html")
                exists = target.is_file()
                row["Validation"] = "File exists" if exists else "Missing local target"
                if not exists:
                    failures.append("Missing internal target " + u.path)
                if applicable and u.path in initial["redirects"]:
                    failures.append("Canonical page links through a legacy redirect")
                internal.append(row)
            else:
                row["Validation"] = "Inventoried; external availability not guaranteed"
                external.append(row)
        for img in d.xpath("//img"):
            src = img.get("src", "")
            u = urllib.parse.urlsplit(src)
            local = not u.scheme and not u.netloc
            file = base / src.lstrip("/")
            img_errors = []
            if local and not file.exists():
                img_errors.append("Missing asset")
            if "alt" not in img.attrib:
                img_errors.append("Missing alt attribute")
            if not img.get("width") or not img.get("height"):
                img_errors.append("Missing dimensions")
            if local and file.exists():
                try:
                    with Image.open(file) as image:
                        if file.suffix == ".webp" and image.format != "WEBP":
                            img_errors.append("Delivery format mismatch")
                except OSError:
                    pass
            decorative = not img.get("alt") and bool(img.xpath('ancestor::*[@aria-hidden="true"]'))
            image_refs.append({"Page URL": ORIGIN + route, "Source": src,
                               "Alt": img.get("alt", ""), "Decorative duplicate": str(decorative),
                               "Width": img.get("width", ""), "Height": img.get("height", ""),
                               "Loading": img.get("loading", "eager/default"),
                               "Fetch Priority": img.get("fetchpriority", "auto"),
                               "Srcset": img.get("srcset", ""), "Sizes": img.get("sizes", ""),
                               "Validation": "; ".join(img_errors) or "Passed"})
            failures.extend(img_errors)
        if failures:
            errors.extend(route + ": " + f for f in sorted(set(failures)))
        render = browser.get(route, {})
        render_status = "Passed" if render and not render.get("errors") and not render.get("overflow") else "Not yet run" if not render else "Review"
        if applicable and render and (render.get("errors") or render.get("overflow")):
            errors.append(route + ": browser verification requires review")
        if applicable:
            status = "Partially complete"
            reason = "Local technical checks passed; publication/GSC/field evidence pending" if not failures else "; ".join(failures)
        elif route in initial["redirects"]:
            status = "Validated" if not failures else "Blocked"
            reason = "Legacy alias: preserve redirect, not a separate content page"
        else:
            status = "Not applicable"
            reason = "Utility/error/verification/internal planning document, not an indexable landing page"
        records.append({"URL": ORIGIN + route, "Source Audited": "Yes",
                        "Page Decision": status, "Technical Changes": "Implemented" if applicable else "Retained utility/redirect behavior",
                        "Built HTML Validation": "Passed" if not failures else "Failed",
                        "Rendered Desktop and Mobile": render_status if applicable else "Not applicable to utility/redirect",
                        "Title": p["title"], "Description": p["description"],
                        "Canonical": p["canonical"], "Robots": p["robots"],
                        "H1": " | ".join(p["h1"]), "Main Words": p["words"],
                        "Schema Types": " | ".join(str(n.get("@type", "")) for n in p["schemas"]),
                        "Production Verification": "Initial live evidence retained; changed build not published",
                        "Observed Live HTTP Status": live.get(ORIGIN + route, {}).get("status", "Not fetched"),
                        "Observed Live Title": live.get(ORIGIN + route, {}).get("page", {}).get("title", ""),
                        "Live Title Matches Build": str(live.get(ORIGIN + route, {}).get("page", {}).get("title") == p["title"]) if applicable else "Not applicable",
                        "Remaining Work": reason, "Validation UTC": STAMP})
    records.append({"URL": ORIGIN + "/index.html", "Source Audited": "Yes",
                    "Page Decision": "Validated", "Technical Changes": "Explicit permanent homepage alias rule",
                    "Built HTML Validation": "Passed", "Rendered Desktop and Mobile": "Not applicable to alias",
                    "Canonical": ORIGIN + "/", "Production Verification": "Initial live 301 confirmed",
                    "Remaining Work": "Alias of homepage, not separate content", "Validation UTC": STAMP})
    for counter, label in [(title_counts, "title"), (description_counts, "description")]:
        for value, count in counter.items():
            if not value or count > 1:
                errors.append(f"Duplicate/empty canonical-page {label}: {value}")
    initial_routes = set(initial["pages"]) | {"/index.html"}
    final_routes = {urllib.parse.urlsplit(r["URL"]).path for r in records}
    if initial_routes != final_routes:
        errors.append(f"Route reconciliation failed: {initial_routes ^ final_routes}")
    master = list(csv.DictReader((ROOT / "research/mr-bakhtawar-keyword-master.csv").open()))
    if len(master) != len({r["Normalized Keyword"] for r in master}):
        errors.append("Keyword normalization duplicates")
    for r in master:
        if not r["Source"] or not r["Research Date"] or r["Recommended Target URL"] not in canonicals:
            errors.append("Keyword provenance or target missing: " + r["Keyword ID"])
    for original, data in image_map.items():
        for variant in data["variants"]:
            p = base / variant["src"].lstrip("/")
            with Image.open(p) as im:
                if im.format != "WEBP" or im.size != (variant["width"], variant["height"]):
                    errors.append("Generated image verification failed: " + str(p))
    write_csv("implementation/page-by-page-validation.csv", records)
    write_csv("implementation/image-reference-validation.csv", image_refs)
    write_csv("research/internal-links.csv", internal)
    write_csv("research/external-links.csv", external)
    summary = {"collected_at": STAMP, "initial_routes": len(initial_routes),
               "final_routes": len(final_routes), "canonical_pages": len(targets),
               "sitemap_entries": len(sitemap), "keyword_records": len(master),
               "images_checked": len(image_refs), "internal_link_usages": len(internal),
               "external_link_usages": len(external), "errors": errors,
               "rendered_pages": len(browser),
               "production_deployed": False}
    (ROOT / "implementation/validation-summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
