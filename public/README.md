# Mr. Bakhtawar / MBK Global — static website

This project is a static HTML/CSS/JavaScript website. The production reference host used in this source package is **https://mr-bakhtawar.netlify.app/**. No deployment was performed during this implementation.

## Project structure
- Root `*.html`: website pages, including portfolio, contact, booking, guides and support pages.
- `assets/`: styles, scripts, images and other static assets.
- `sitemap.xml`, `robots.txt`, `llms.txt`, `identity-config.json`: crawl and identity support.
- `_headers`, `_redirects`: Netlify response-header and redirect configuration for a root publish directory.
- `SEO-ISSUES.csv`, `SEO-URL-MAPPING.csv`, `CONTENT-OVERLAP-MATRIX.csv`, `PAGE-BY-PAGE-AUDIT.csv`, `IMAGE-SEO-AUDIT.csv`: implementation records.
- `MASTER-AUDIT.md`, `TEST-REPORT.md`, `CHANGELOG.md`, `FINAL-ROADMAP.md`: findings and next steps.

## Local preview
Use Python 3 from this directory:
```bash
python -m http.server 8000
```
Open `http://127.0.0.1:8000/`. This preview does not emulate Netlify response headers or redirects. Do not submit live forms during testing.

## Local validation
```bash
python - <<'PY'
from pathlib import Path
from bs4 import BeautifulSoup
import json
root = Path('.')
for p in root.glob('*.html'):
    if p.name == 'google194f46fe9461fc27.html':
        continue  # Google site-verification token file, not a content page
    soup = BeautifulSoup(p.read_text(errors='replace'), 'html.parser')
    assert soup.html is not None, f'HTML parse issue: {p}'
    for block in soup.find_all('script', type='application/ld+json'):
        json.loads(block.string or block.get_text())
print('HTML and JSON-LD syntax checks completed.')
PY
```
The full recorded test results and limitations are in `TEST-REPORT.md`.

## Netlify deployment
1. Review the source changes and reports.
2. In Netlify, confirm the publish directory is the repository root (the current project stores HTML, `assets/`, `_headers`, `_redirects`, and `sitemap.xml` at root). If your actual deploy configuration uses another directory, move/copy these Netlify files to that publish directory.
3. Deploy using your normal process; this package has not been deployed.
4. Verify response headers and redirects from a terminal:
```bash
curl -sSI https://mr-bakhtawar.netlify.app/
curl -sSI https://mr-bakhtawar.netlify.app/blog-web-performance.html
curl -sSI https://mr-bakhtawar.netlify.app/technical-seo-checklist-mbk.html
curl -sS https://mr-bakhtawar.netlify.app/robots.txt
curl -sS https://mr-bakhtawar.netlify.app/sitemap.xml
```
For redirects, inspect the `Location` header and ensure the response is a single 301 to the intended destination. Confirm HSTS, `X-Content-Type-Options`, `Referrer-Policy`, `X-Frame-Options` and `Content-Security-Policy-Report-Only` in the actual response. A source config file alone does not prove the live host is serving the headers.

## Safety notes
- `vercel.json` is retained unchanged because it may serve a separate Vercel deployment. Netlify uses `_headers` and `_redirects`.
- GitHub-hosted gallery assets were not rehosted because ownership/licensing permission was not verified.
- Publication dates were not invented. Article schema omits date properties when source evidence is absent.
- Search Console, backlink index data, deployment credentials and live browser/network verification were not available in this run.
