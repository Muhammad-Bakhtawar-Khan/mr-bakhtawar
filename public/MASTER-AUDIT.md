# Master Audit — MBK Global / Mr. Bakhtawar

**Reference host:** https://mr-bakhtawar.netlify.app/  
**Implementation status:** Source changes and local static checks completed; deployment and live verification pending.  
**Backup:** `MBK-ORIGINAL-UNCHANGED.zip` is a byte-for-byte copy of the supplied website archive and was not edited.

## Scope and source of truth
Inspected `Mr_Bakhtawar_Full_SEO_Upgrade.zip` and the seven-file supporting `files.zip`. The HTML/CSS/configuration in the website archive was treated as authoritative; audit CSVs were used as evidence and reviewed against actual files. The separate `claude-seo-main.zip` is a SEO skill/plugin repository, not a website source archive, and was not mixed into the deliverable.

## Verified implementation
- Added Netlify `_headers` at the project root, which matches the observed root-level static publish layout. Headers include HSTS (one year, no preload), `nosniff`, strict-origin referrer policy, `X-Frame-Options: DENY`, and CSP in **Report-Only** mode. Live headers are not claimed as verified.
- Added `_redirects` with 47 301 force rules for source pages mapped to existing, relevant pillar/article destinations. Redirect source HTML remains in the working project for reversibility; the untouched original archive also retains every original file. Live precedence/status must be checked after deployment.
- Replaced stale references to the obsolete Vercel hostname and unapproved custom-domain reference with the canonical Netlify reference in project docs/config/source. Historical URLs unrelated to those incorrect production references were otherwise preserved.
- Removed the homepage review-style five-star treatment and stock avatar references, replacing the carousel cards with explicitly labelled portfolio highlights. These are not presented as customer reviews.
- Promoted missing top-level headings on article pages where the original markup had no H1; the 11 article pages are retained.
- Created six new original pillar guides: on-page SEO, content strategy/search intent, performance/UX, deployment/maintenance, automation/responsible AI, and personal branding/online identity. Existing technical SEO and web security pillar URLs are retained and expanded.
- Added Article schema and BreadcrumbList to article pages when absent, with no invented publication or modification dates. The six new guides include Article schema and breadcrumbs.
- Added local image dimensions where the file was available and detectable, removed lazy loading from a page's first image if present, and added lazy loading/async decoding to suitable later images. No remote image was rehosted or converted.
- Removed the CSS `@import` font chain. A system font fallback remains available; font appearance should be reviewed visually before release.
- Fixed duplicate IDs found in `about-muhammad-bakhtawar-khan.html`, `book-a-call.html`, `changelog.html` and `resume.html`.
- Rebuilt `sitemap.xml` from canonical, existing indexable HTML pages, excluding redirected URLs, the 404 page, verification token and thank-you pages.
- Kept `vercel.json` rather than assuming it controls Netlify. Preserved `robots.txt` crawler policy; no bot policy changes were made.

## Content and redirect decisions
The source overlap matrix reported highly repetitive boilerplate across 45 `blog-*.html` pages. Redirects are configured for the mappings marked as merge into pillar/article only where both source and destination files existed. Six new destinations were created before their redirects were configured. Source HTML is retained in the working package, but Netlify force redirects intentionally make the mapped URLs resolve to the new destinations when deployed.

The 11 `article-*.html` pages remain present. `PHASE 2 REVIEW` mappings are not redirected. Because Search Console and backlink-index data were unavailable, the owner should review redirect performance and the redirect inventory after deployment. The rules are reversible.

## Image and licensing limitations
`IMAGE-SEO-AUDIT.csv` inventories locally and externally referenced images. Remote image dimensions, file size and license are marked unknown when not verifiable. The 25 GitHub-hosted gallery images remain externally referenced; no permission to rehost was assumed. Personal photography was not replaced with stock imagery.

## Structured data and dates
JSON-LD syntax was checked locally. Article schema uses the visible page title/description and canonical URL, with an author identity and main entity where justified. No `datePublished` or `dateModified` values were invented. Existing schema on non-article pages was not blindly replaced. This is source validation, not a guarantee that search engines will accept rich results.

## Known limitations / unresolved
- No deployment, DNS changes, account access, external profile creation or form submission occurred.
- Live HTTP status codes, headers, redirect behavior, rendered remote images, console errors and deployed canonical output are not verified.
- Search Console query/click data, backlink-index data, and owner-confirmed article dates were unavailable.
- Playwright package was present, but its Chromium executable was not installed; responsive visual and console tests could not run in a real browser.
- Lighthouse and Core Web Vitals were not measured. LCP ≤ 2.5s, INP ≤ 200ms and CLS ≤ 0.1 remain goals, not reported results.
- A few content details, image rights, and any owner-only experience claims still require owner review.
- HSTS should only be kept if the production host is reliably HTTPS; Netlify-hosted sites normally are, but response verification is still required.

## Status vocabulary
`Fixed and verified` means verified by local source checks. `Fixed locally; live verification pending` means source/config changes exist but the deployed behavior has not been tested. `Partially fixed` marks work with evidence or measurement gaps. `Not tested` means required browser, network or account access was unavailable.
