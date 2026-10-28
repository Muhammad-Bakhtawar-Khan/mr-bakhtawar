# Changelog

## SEO implementation — 2026-10-27
Actual changes in the working copy:
- Added `_headers` for Netlify security headers and CSP Report-Only.
- Added `_redirects` with 47 301 force rules for mapped consolidations; source HTML remains in the package.
- Updated current production-host references in HTML, Markdown, JSON, XML, text and CSV documents.
- Rebuilt `sitemap.xml` using canonical existing indexable pages; omitted redirected URLs, verification/error/thank-you pages.
- Replaced homepage sample review cards with labelled portfolio highlights; removed stock avatar usage and star-rating styling/presentation.
- Added six new pillar guides; expanded existing technical SEO and web security guides.
- Added missing Article and BreadcrumbList JSON-LD to article pages when absent, without invented dates.
- Fixed article H1 omissions, duplicate IDs and duplicate meta description group found in the source audit.
- Added local image dimensions where verifiable and adjusted loading/decoding attributes.
- Removed CSS Google Fonts `@import` chain.
- Added/updated `MASTER-AUDIT.md`, `PAGE-BY-PAGE-AUDIT.csv`, `CONTENT-OVERLAP-MATRIX.csv`, `IMAGE-SEO-AUDIT.csv`, `SEO-URL-MAPPING.csv`, `SEO-ISSUES.csv`, `TEST-REPORT.md`, `FINAL-ROADMAP.md` and `README.md`.

## Not performed
No deployment, DNS change, Search Console access, backlink measurement, external profile creation, real form submission, or `scripts/sync_identity.py` execution. `vercel.json` was retained.
