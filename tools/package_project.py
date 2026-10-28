#!/usr/bin/env python3
"""Create a new reviewable source/build ZIP; no publishing or existing-file overwrite."""
import argparse
import hashlib
import os
import zipfile
from pathlib import Path
from seo_audit import ROOT, write_csv

EXCLUDED = {
    ".git", "node_modules", ".delivery", ".figaro", "__pycache__",
    ".cache", ".pytest_cache", "artifacts", "private", "private-exports",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="A new ZIP path; existing files are never overwritten")
    parser.add_argument("--source-only", action="store_true", help="Omit reproducible dist output for smaller exports")
    args = parser.parse_args()
    output = Path(args.output).resolve()
    if output.suffix.lower() != ".zip" or output.exists():
        raise SystemExit("Choose a new .zip output path.")
    files = []
    manifest_path = ROOT / "reports/package-file-manifest.csv"
    for directory, folders, names in os.walk(ROOT):
        folders[:] = sorted(f for f in folders if f not in EXCLUDED
                            and not (args.source_only and Path(directory) == ROOT and f == "dist")
                            and not (Path(directory) / f).is_symlink())
        for name in sorted(names):
            path = Path(directory) / name
            if path.is_symlink() or path == manifest_path or name.startswith(".env") or path.suffix in [".zip", ".pyc", ".log"]:
                continue
            if name.lower() in ["credentials.json", "secrets.json", "service-account.json"]:
                continue
            files.append(path)
    manifest = [{"Path": str(p.relative_to(ROOT)), "Bytes": p.stat().st_size,
                 "SHA256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
    write_csv("reports/package-file-manifest.csv", manifest)
    files.append(manifest_path)
    required = {
        "README.md", "package.json", "src/App.tsx",
        "research/mr-bakhtawar-keyword-master.csv",
        "implementation/page-by-page-validation.csv",
        "reports/complete-page-inventory.csv", "tools/README.md",
    }
    if not args.source_only:
        required.add("dist/index.html")
    if not required.issubset({str(p.relative_to(ROOT)) for p in files}):
        raise SystemExit("Required deliverables missing; refusing to package.")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for p in files:
            archive.write(p, "mr-bakhtawar-seo-project/" + str(p.relative_to(ROOT)))
    with zipfile.ZipFile(output) as archive:
        bad = archive.testzip()
        if bad:
            raise SystemExit("ZIP integrity failure: " + bad)
        if len(archive.namelist()) != len(files):
            raise SystemExit("ZIP entry-count mismatch.")
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(".zip.sha256").write_text(f"{digest}  {output.name}\n")
    print(f"Packaged and integrity-checked {len(files)} files; {output.stat().st_size:,} bytes.")
    print("ZIP:", output)
    print("SHA256:", digest)


if __name__ == "__main__":
    main()
