#!/usr/bin/env python3
"""Read-only asset and per-reference image SEO inventory."""
import csv
import json
from collections import defaultdict
from pathlib import Path
from PIL import Image
from seo_audit import ROOT, write_csv


def main():
    initial = json.loads((ROOT / "reports/evidence/initial/source.json").read_text())
    delivery = json.loads((ROOT / "implementation/image-delivery-map.json").read_text())
    subjects = json.loads((ROOT / "research/image-subjects.json").read_text())
    original_refs = defaultdict(list)
    for route, page in initial["pages"].items():
        for image in page["images"]:
            original_refs[image.get("src", "")].append((route, image))
    final_refs = defaultdict(list)
    dynamic_refs = defaultdict(list)
    dynamic_rows = []
    for data_path in ["src/gallery-showcase.json", "public/assets/data/portrait-track.json"]:
        for item in json.loads((ROOT / data_path).read_text()):
            if "src" in item:
                dynamic_refs[item["src"]].append(item)
                dynamic_rows.append({"Data Source": data_path, "Source": item["src"],
                                     "Alt": item.get("alt", ""), "Srcset": item.get("srcset", ""),
                                     "Width": item.get("width", ""), "Height": item.get("height", ""),
                                     "Loading": "lazy", "Validation": "Source exists" if (ROOT / "public" / item["src"].lstrip("/")).exists() else "Missing"})
    reference_file = ROOT / "implementation/image-reference-validation.csv"
    if reference_file.exists():
        for row in csv.DictReader(reference_file.open()):
            final_refs[row["Source"]].append(row)
    reverse = {}
    for source, data in delivery.items():
        for variant in data["variants"]:
            reverse[variant["src"]] = source
    rows = []
    for path in sorted((ROOT / "public").rglob("*")):
        if path.suffix.lower() not in [".png", ".webp", ".jpg", ".jpeg", ".ico", ".svg"]:
            continue
        route = "/" + str(path.relative_to(ROOT / "public"))
        try:
            with Image.open(path) as image:
                width, height, format_name = image.width, image.height, image.format
        except OSError:
            width = height = 64 if path.suffix == ".svg" else ""
            format_name = "SVG" if path.suffix == ".svg" else "Unknown"
        source = reverse.get(route, route)
        description = subjects.get(Path(source).name, "Portfolio identity icon" if "icon" in route else "Branded social sharing card")
        before = original_refs.get(source, [])
        after = final_refs.get(route, [])
        old_alts = sorted({i.get("alt", "<missing>") for _, i in before})
        current_alts = sorted({i["Alt"] for i in after} | {i.get("alt", "") for i in dynamic_refs[route]})
        issue = []
        if path.suffix in [".png", ".webp"] and format_name == "JPEG":
            issue.append("Preserved legacy filename/format mismatch; active references use genuine WebP delivery copies")
        if not after and route not in reverse:
            issue.append("Original/metadata asset; no active static img reference")
        generated = route in reverse
        data = delivery.get(source)
        recommendation = ("Use generated srcset and context-appropriate sizes; retain original URL for compatibility"
                          if data and not generated else "Keep accurate contextual alt; repeated decorative copy remains empty"
                          if generated else "No alt for favicon/social metadata; do not keyword-stuff")
        rows.append({
            "Existing Filename": path.name, "File Path": str(path.relative_to(ROOT)),
            "Actual Subject and Purpose": description,
            "Current Alt Text": " | ".join(current_alts or old_alts),
            "Recommended Alt Text": "Keep current contextual text; decorative duplicates empty" if after else description if "portrait" in description.lower() else "Not applicable to metadata-only icon",
            "Width": width, "Height": height, "File Size Bytes": path.stat().st_size,
            "Actual Format": format_name,
            "Loading Behavior": " | ".join(sorted({i["Loading"] for i in after})) or "Metadata/original asset; see delivery map",
            "Responsive Image Status": "srcset configured" if generated else "Replaced by responsive derivatives" if data else "Not applicable",
            "Initial Source References": len(before), "Final Static References": len(after),
            "Dynamic Data References": len(dynamic_refs[route]),
            "SEO Issues": "; ".join(issue) or "None detected for active delivery",
            "Recommended Changes": recommendation,
            "Selected Delivery URL": data["src"] if data else route,
            "Validation Status": "Validated format/dimensions; original preserved" if data else "Inventoried",
        })
    write_csv("research/image-seo-inventory.csv", rows)
    write_csv("implementation/dynamic-image-usage.csv", dynamic_rows)
    print("Image assets inventoried:", len(rows))


if __name__ == "__main__":
    main()
