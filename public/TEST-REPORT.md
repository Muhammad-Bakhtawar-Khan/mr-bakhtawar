# Test Report

**Test date:** 2026-10-27  
**Test scope:** Local source tree only; no deployment or external form submissions.

## Executed checks

| Check | Result | Evidence / notes |
|---|---|---|
| HTML parse/structure | PASS | Parsed 96 content HTML files with BeautifulSoup; no missing HTML root found. Google verification token file is intentionally excluded from content-page checks. |
| Internal relative links | PASS | Rechecked relative links in content pages; 0 missing targets. |
| Canonical host consistency | PASS | All 96 content pages have canonical links using the reference Netlify host. |
| Title and description presence | PASS | No content page missing title or meta description. |
| Duplicate titles | PASS | 0 duplicate title groups. |
| Duplicate descriptions | PASS | 0 duplicate description groups. |
| H1 count | PASS | Every content page has exactly one H1 after article corrections. |
| Duplicate HTML IDs | PASS | No duplicate IDs remain in content pages. |
| JSON-LD syntax | PASS | All JSON-LD blocks parsed as JSON; no syntax failures found. This is syntax validation, not Google's rich-result validation. |
| Sitemap-to-file coverage | PASS | 47 sitemap URLs; no missing local HTML targets. Redirected source URLs are excluded. |
| Redirect destinations | PASS | 47 rules; every destination exists locally. |
| Image inventory | PASS | 144 image references inventoried. Remote dimensions/licensing remain unknown where not verifiable. |
| Netlify config presence | PASS | `_headers` and `_redirects` exist in the observed root-level publish layout; `vercel.json` retained. |
| Stale hostname scan | PASS | Implementation docs/source no longer contain obsolete host strings; source audit copy was corrected to generic descriptions. |
| Security configuration review | PASS (source only) | HSTS, nosniff, Referrer-Policy, framing protection and CSP Report-Only are configured in `_headers`. Live response is untested. |

## Not run / unavailable

- **Mobile overflow at 375px / 390px, tablet and desktop:** NOT TESTED in browser. Playwright package was installed, but the Chromium executable was missing, so the browser could not launch.
- **Keyboard navigation and form accessibility:** NOT TESTED in a real browser. Source-level checks only; no form was submitted.
- **JavaScript console/runtime errors:** NOT TESTED in browser because no browser executable was available.
- **Live HTTP status, response headers, canonical output and redirect behavior:** NOT TESTED. This package was not deployed and outbound live-site verification was not available.
- **Lighthouse / Core Web Vitals:** NOT TESTED. No lab or field measurements were collected. LCP ≤ 2.5s, INP ≤ 200ms and CLS ≤ 0.1 are targets only.
- **Search Console, query/click data and backlink index:** NOT AVAILABLE. No traffic or link equity conclusions are made.
- **Image licensing and remote image dimensions:** NOT TESTED for third-party assets. No remote assets were rehosted.
- **Dependency security audit:** NOT APPLICABLE as a package/dependency install was not performed; no framework migration was introduced.

## Baseline comparison
A pre-edit inventory was saved as `BASELINE.json` outside the deliverable working site, and planned files were recorded in `FILES-TO-CHANGE.txt` during implementation. Baseline observations were compared with the final source checks: article H1 omissions and four duplicate-ID groups were corrected; duplicate descriptions were corrected; canonical host remained consistent; JSON-LD remains parseable; internal relative-link check has no missing targets. Sitemap URLs were rebuilt to omit redirects and include current canonical guide pages.

## Reproduction
From the site root, run:
```bash
python -m http.server 8000
```
Then in another terminal, run `curl -sSI https://mr-bakhtawar.netlify.app/` after deployment to verify live headers. See `README.md` for the full live verification commands.
