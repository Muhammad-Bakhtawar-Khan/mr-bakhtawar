# MBK Portfolio — SEO / AEO / GEO Audit Report

**Audit date:** 2026-10-23  
**Site:** https://mr-bakhtawar.netlify.app/  
**Scope:** local source audit of the latest supplied portfolio ZIP; live deployment was not changed.

## Verified local work completed

- Backed up the original extracted project before changes to `MBK_SEO_Audit_Original_Backup.zip`.
- Scanned 90 local HTML pages for titles, descriptions, canonical tags, H1 counts, image alt attributes, Open Graph/Twitter preview metadata, local references and JSON-LD syntax.
- Added missing `og:image`, `og:image:alt`, Twitter card/image/title/description metadata where absent on 55 HTML pages, using the page's existing image where available and a consistent MBK portrait fallback otherwise.
- Regenerated `sitemap.xml` from locally indexable HTML pages, excluding the noindex 404 and thank-you pages. Final sitemap URL count: 88.
- Confirmed no duplicate titles, descriptions or canonical URLs in the pre-fix local scan; JSON-LD syntax errors found after scan: 0; missing image alt attributes: 0.
- Preserved the existing crawler policy: Googlebot/Bingbot/OAI-SearchBot/ChatGPT-User allowed, GPTBot and several other AI crawlers disallowed. Confirm policy is intentional before changing it.
- Preserved Vercel security header configuration in `vercel.json`.

## Findings requiring follow-up

- H1 count differs from exactly one on 7 pages: article-bakhtawar-khan.html, article-mbk-global.html, article-mbk-markets.html, article-mbk-next-steps.html, article-mbk-tools.html, article-mbk-tv.html, article-noor-e-quran.html. These need a page-by-page semantic review; not blindly rewritten to avoid changing design/content incorrectly.
- Missing title/description/canonical entries: 0. Details are listed in the audit workbook; investigate each affected page.
- Local reference scan reported 0 candidate unresolved references. Many are root-absolute paths such as `/favicon.ico`, which are valid for the deployed domain but do not resolve as filesystem-relative paths in this scan. Validate actual HTTP responses after deployment.
- Performance, Core Web Vitals (LCP/INP/CLS), mobile layout, redirects, status codes, TLS, caching/compression, forms, live external links and crawler rendering were **not** verified live.
- Google Search Console and analytics account metrics/ownership cannot be confirmed from local files. No indexing, rankings or live PageSpeed scores are claimed.
- `robots.txt` currently blocks multiple AI crawlers by owner policy. This is a policy decision, not an error by itself; only change if broader AI-search crawling is intended.
- Local SEO and hreflang are treated as conditional/N/A for this English-language personal portfolio unless localized pages or a service-area business profile are intentionally supported.

## Deployment verification checklist

1. Deploy this package to the existing Vercel project and confirm the production domain/branch.
2. Fetch `/`, `/robots.txt`, `/sitemap.xml`, `/about-muhammad-bakhtawar-khan.html`, `/services.html`, `/projects.html`, `/official-links.html`, and representative articles; verify status, final URL, canonical and robots directives.
3. Run a full deployed crawl and resolve real 404s/redirect chains; test mobile navigation and all forms/contact actions.
4. Run PageSpeed Insights for mobile and desktop on homepage, founder profile, services, projects and top articles; record LCP, INP/field-data availability, CLS and Lighthouse diagnostics.
5. Validate representative JSON-LD in Schema Markup Validator and Google Rich Results Test; confirm schema matches visible content.
6. Use Search Console URL Inspection and sitemap submission with authorized account access; review queries, clicks, impressions and CTR after enough data accrues.
7. Confirm analytics and conversion events using the live browser/debug tools.

## Deliverables

- `MBK_Portfolio_SEO_Audit_Optimized.zip` — updated project files.
- `MBK_186_Point_SEO_Audit_Report.xlsx` — 186-row checklist with status, priority, evidence, finding, fix, assignee, due date and verification column.
- `MBK_SEO_Audit_Original_Backup.zip` — original files before changes.
