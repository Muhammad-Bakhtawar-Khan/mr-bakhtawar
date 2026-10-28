#!/usr/bin/env python3
"""Generate responsive delivery copies. Never changes or deletes originals."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
NAMES = {
    "muhammad-bakhtawar-khan-mbk-standing-professional-portrait.png": "bakhtawar-standing-white-portrait",
    "muhammad-bakhtawar-khan-mbk-white-outfit-full-length-portrait.png": "bakhtawar-white-outfit-portrait",
    "muhammad-bakhtawar-khan-mbk-global-founder-office-portrait.png": "bakhtawar-office-portrait",
    "muhammad-bakhtawar-khan-mbk-professional-navy-portrait.webp": "bakhtawar-seated-navy-portrait",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Write generated copies and delivery map")
    args = parser.parse_args()
    output = ROOT / "public/assets/images/optimized"
    mapping = {}
    for path in sorted((ROOT / "public/assets/images/gallery").glob("*")):
        try:
            with Image.open(path) as source:
                im = ImageOps.exif_transpose(source).convert("RGB")
                width, height = im.size
                stem = NAMES.get(path.name, path.stem)
                variants = []
                for size in sorted(set([min(width, 480), min(width, 960)])):
                    resized = im.resize((size, round(height * size / width)), Image.Resampling.LANCZOS)
                    target = output / f"{stem}-{size}.webp"
                    if args.write:
                        output.mkdir(parents=True, exist_ok=True)
                        resized.save(target, "WEBP", quality=86, method=6)
                    variants.append({"src": "/" + str(target.relative_to(ROOT / "public")),
                                     "width": resized.width, "height": resized.height})
                selected = variants[-1]
                mapping["/" + str(path.relative_to(ROOT / "public"))] = {
                    **selected,
                    "srcset": ", ".join(f'{v["src"]} {v["width"]}w' for v in variants),
                    "variants": variants,
                    "original_format": source.format,
                    "original_width": width, "original_height": height,
                    "original_bytes": path.stat().st_size,
                }
        except (OSError, ValueError):
            continue
    if args.write:
        (ROOT / "implementation/image-delivery-map.json").write_text(json.dumps(mapping, indent=2))
    print(f"{len(mapping)} originals inspected; generated copies {'written' if args.write else 'planned (dry run)'}.")


if __name__ == "__main__":
    main()
