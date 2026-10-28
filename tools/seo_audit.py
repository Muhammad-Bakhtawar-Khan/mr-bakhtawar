#!/usr/bin/env python3
"""Read-only site inventory/crawl. Explicit phases preserve the initial baseline."""
import argparse
import concurrent.futures
import csv
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from lxml import html

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://mr-bakhtawar.netlify.app"
STAMP = datetime.now(timezone.utc).isoformat()


def write_csv(path, rows, fields=None):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = fields or (list(rows[0]) if rows else ["No records"])
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def document(text):
    return html.document_fromstring(text or "<html></html>")


def extract(text):
    d = document(text)
    head = d.find("head")
    if head is None:
        return {"title": "", "description": "", "canonical": "", "robots": "",
                "h1": [], "h2": [], "schemas": [], "schema_errors": [],
                "links": [], "images": [], "words": 0, "main_text": "",
                "metadata_duplicates": [], "meta": {}, "refresh": ""}
    metas = {}
    counts = Counter()
    for e in head.findall("meta"):
        key = (e.get("property") or e.get("name") or "").lower()
        if key:
            counts[key] += 1
            metas[key] = e.get("content", "")
    schemas, errors = [], []
    for e in head.xpath('./script[@type="application/ld+json"]'):
        try:
            value = json.loads(e.text or "")
            schemas.extend(value if isinstance(value, list) else value.get("@graph", [value]))
        except (ValueError, AttributeError) as exc:
            errors.append(str(exc))
    mains = d.xpath("//main")
    # Exclude repeated site-directory boilerplate from content-quality measurements.
    if mains:
        main = html.fromstring(html.tostring(mains[0]))
        for e in main.xpath('.//script|.//style|.//*[contains(@class,"mbk-related-links") or contains(@class,"mbk-site-directory") or contains(@class,"academy-directory") or contains(@class,"global-archive")]'):
            if e.getparent() is not None:
                e.getparent().remove(e)
        main_text = " ".join(main.text_content().split())
    else:
        main_text = ""
    canonical = head.xpath('./link[contains(concat(" ",@rel," ")," canonical ")]/@href')
    return {
        "title": head.findtext("title") or "",
        "description": metas.get("description", ""),
        "canonical": canonical[0] if canonical else "",
        "robots": metas.get("robots", ""),
        "h1": [" ".join(e.text_content().split()) for e in d.xpath("//main//h1")],
        "h2": [" ".join(e.text_content().split()) for e in d.xpath("//main//h2")],
        "schemas": schemas, "schema_errors": errors,
        "links": d.xpath("//a/@href"),
        "images": [dict(e.attrib) for e in d.xpath("//img")],
        "words": len(main_text.split()), "main_text": main_text,
        "metadata_duplicates": [k for k, n in counts.items() if n > 1],
        "meta": metas,
        "refresh": " ".join(head.xpath('./meta[translate(@http-equiv,"REFSH","refsh")="refresh"]/@content')),
    }


def redirects():
    rules = {}
    for line in (ROOT / "public/_redirects").read_text().splitlines():
        p = line.split()
        if p and not p[0].startswith("#") and len(p) >= 3:
            rules[p[0]] = {"target": p[1], "status": p[2]}
    return rules


def sitemap_urls(text):
    return [e.text for e in ET.fromstring(text).iter() if e.tag.endswith("}loc") and e.text]


def local_routes():
    pages = {"/": ROOT / "index.html"}
    pages.update({"/" + str(p.relative_to(ROOT / "public")): p
                  for p in (ROOT / "public").rglob("*.html")})
    return pages


def route_type(route):
    if route == "/":
        return "Homepage"
    if route == "/index.html":
        return "Homepage alias"
    if re.fullmatch(r"/google[0-9a-f]+\.html", route):
        return "Search verification"
    if "backlink-seo-plan" in route:
        return "Internal planning utility"
    if route in redirects():
        return "Legacy redirect"
    if route == "/404.html":
        return "Error document"
    if route == "/thank-you.html":
        return "Form utility"
    if any(x in route for x in ["article-", "guide", "blog-", "seo-for-", "entity-clarity", "content-design", "personal-branding", "search-intent", "chatbots-explained", "checklist", "interface-design"]):
        return "Article / guide"
    if route in ["/services.html", "/web-development.html", "/ai-api-integration.html",
                 "/technical-seo.html", "/cybersecurity.html", "/digital-branding.html"] or any(x in route for x in ["development.html", "automation.html"]):
        return "Service"
    if route in ["/projects.html", "/case-studies.html", "/changelog.html", "/delivered-project.html"]:
        return "Portfolio / process"
    return "Profile / directory / contact"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch(url, folder):
    """No redirects followed: their true initial statuses are evidence."""
    request = urllib.request.Request(url, headers={"User-Agent": "MBK-SEO-Audit/1.0 (owner-requested; limited concurrency)"})
    result = {"url": url, "collected_at": STAMP, "status": "", "location": "",
              "content_type": "", "error": "", "file": ""}
    try:
        time.sleep(.12)
        try:
            response = urllib.request.build_opener(NoRedirect).open(request, timeout=20)
        except urllib.error.HTTPError as e:
            response = e
        body = response.read(5_000_000)
        result.update(status=response.code, location=response.headers.get("Location", ""),
                      content_type=response.headers.get("Content-Type", ""),
                      x_robots_tag=response.headers.get("X-Robots-Tag", ""),
                      cache_control=response.headers.get("Cache-Control", ""))
        path = folder / (hashlib.sha256(url.encode()).hexdigest()[:20] + ".body")
        path.write_bytes(body)
        result["file"] = str(path.resolve().relative_to(ROOT))
        if "html" in result["content_type"]:
            result["page"] = extract(body.decode("utf-8", "replace"))
    except Exception as e:
        result["error"] = f"{type(e).__name__}: {e}"
    return result


def inventory(phase):
    folder = ROOT / "reports/evidence" / phase
    folder.mkdir(parents=True, exist_ok=True)
    sources = {route: extract(path.read_text()) for route, path in local_routes().items()}
    snapshot = {"collected_at": STAMP, "origin": ORIGIN, "pages": sources,
                "redirects": redirects(), "dynamic_routes": [],
                "source_files": {r: str(p.relative_to(ROOT)) for r, p in local_routes().items()}}
    (folder / "source.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2))
    return snapshot


def crawl(snapshot, phase):
    folder = ROOT / "reports/evidence" / phase
    urls = {ORIGIN + r for r in snapshot["pages"]}
    urls |= {ORIGIN + "/index.html", ORIGIN + "/robots.txt", ORIGIN + "/sitemap.xml"}
    urls |= set(sitemap_urls((ROOT / "public/sitemap.xml").read_text()))
    # Discover route-like internal references, separating file resources from pages.
    for page in snapshot["pages"].values():
        for link in page["links"]:
            u = urllib.parse.urlsplit(urllib.parse.urljoin(ORIGIN + "/", link))
            if u.netloc == urllib.parse.urlsplit(ORIGIN).netloc and (u.path.endswith(".html") or u.path == "/"):
                urls.add(ORIGIN + u.path)
    found = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for r in pool.map(lambda u: fetch(u, folder), sorted(urls)):
            found[r["url"]] = r
    sm = found.get(ORIGIN + "/sitemap.xml", {})
    if sm.get("status") == 200:
        try:
            extra = set(sitemap_urls((ROOT / sm["file"]).read_text())) - set(found)
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
                for r in pool.map(lambda u: fetch(u, folder), sorted(u for u in extra if u.startswith(ORIGIN + "/"))):
                    found[r["url"]] = r
        except ET.ParseError:
            pass
    (folder / "live.json").write_text(json.dumps(found, ensure_ascii=False, indent=2))
    print("Public fetches:", len(found), Counter(str(v["status"]) for v in found.values()))
    return found


def issues(page, route):
    if route_type(route) in ["Search verification", "Legacy redirect"]:
        return ["Not an independent indexable content page"]
    out = []
    if not page["title"]:
        out.append("Missing title")
    if not page["description"]:
        out.append("Missing description")
    if len(page["title"]) > 65:
        out.append("Review long title (not a Google cutoff)")
    if len(page["description"]) > 175:
        out.append("Review long description (not a Google cutoff)")
    if page["canonical"] != ORIGIN + route:
        out.append("Review canonical")
    if len(page["h1"]) != 1:
        out.append("H1 not exactly one in source")
    if not page["h2"] and page["words"] > 150:
        out.append("No main-content H2")
    if page["words"] < 200:
        out.append("Short main content: manual usefulness review, not a ranking threshold")
    if page["metadata_duplicates"]:
        out.append("Duplicate metadata")
    if page["schema_errors"]:
        out.append("Invalid JSON-LD")
    if any(not i.get("alt") for i in page["images"]):
        out.append("Review empty/missing alt in context")
    if any(not i.get("width") or not i.get("height") for i in page["images"]):
        out.append("Image dimensions missing")
    return out


def baseline(snapshot, live, output="reports/complete-page-inventory.csv"):
    local_sitemap = set(sitemap_urls((ROOT / "public/sitemap.xml").read_text()))
    rows = []
    all_routes = set(snapshot["pages"])
    all_routes.update(snapshot["redirects"])
    all_routes.update(urllib.parse.urlsplit(u).path for u in live if u.endswith(".html"))
    for route in sorted(all_routes):
        p = snapshot["pages"].get(route, {})
        result = live.get(ORIGIN + route, {})
        lp = result.get("page", {})
        if not p:
            p = extract("")
        indexable = (route not in snapshot["redirects"] and route_type(route) not in ["Search verification", "Internal planning utility", "Error document", "Form utility", "Homepage alias"]
                     and "noindex" not in p["robots"])
        rows.append({
            "URL": ORIGIN + route, "Route": route,
            "Source File": snapshot["source_files"].get(route, "URL variant / live-only"),
            "Page Type": route_type(route), "Dynamic Route": "No",
            "Separate Content Page": "No" if route == "/index.html" or route in snapshot["redirects"] else "Yes",
            "Source Indexability": "Eligible" if indexable else "Not eligible / utility / alias",
            "Live HTTP Status": result.get("status", "Not fetched"),
            "Live Error": result.get("error", ""), "Live Redirect": result.get("location", ""),
            "Source Title": p["title"], "Live Title": lp.get("title", ""),
            "Source Description": p["description"], "Live Description": lp.get("description", ""),
            "Source Canonical": p["canonical"], "Live Canonical": lp.get("canonical", ""),
            "Source Robots": p["robots"], "Live Robots": lp.get("robots", ""),
            "Live X-Robots-Tag": result.get("x_robots_tag", ""),
            "H1": " | ".join(p["h1"]), "H2 Count": len(p["h2"]),
            "Main Content Words": p["words"],
            "Content Purpose": p["description"] or route_type(route),
            "Source Sitemap": "Yes" if ORIGIN + route in local_sitemap else "No",
            "Technical Issues": "; ".join(issues(p, route)),
            "Audit Status": "Audited" if result.get("status") else "Blocked: live fetch",
            "Collected At UTC": snapshot["collected_at"],
        })
    write_csv(output, rows)
    print("Inventory rows:", len(rows), "source documents:", len(snapshot["pages"]))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("phase", choices=["initial", "final", "regression"])
    p.add_argument("--live", action="store_true", help="Explicitly fetch the public site; no publishing")
    args = p.parse_args()
    if args.phase == "initial" and (ROOT / "reports/evidence/initial/source.json").exists():
        raise SystemExit("Initial baseline exists; refusing to overwrite it.")
    snapshot = inventory(args.phase)
    live = crawl(snapshot, args.phase) if args.live else {}
    if args.phase == "initial":
        baseline(snapshot, live)
    else:
        baseline(snapshot, live, f"reports/{args.phase}-page-inventory.csv")


if __name__ == "__main__":
    main()
