# SEO Audit — Mr. Bakhtawar / MBK Global

**Site:** https://mr-bakhtawar.netlify.app/ · **Stack:** static HTML, CSS, vanilla JS · **Audit date:** 27 Oct 2026
**Status: PHASE 1 COMPLETE (read-only). No site file has been edited, deleted, merged, renamed or deployed. Every fix below is a proposal awaiting approval.**

## 1. Verification classes

| Class | Meaning |
|---|---|
| **Verified (source)** | Confirmed by parsing the actual project files (91 HTML pages, CSS, JS, config, docs) |
| **Likely / needs testing** | Probable from source but depends on live behaviour |
| **Not Tested** | Needs network or credentials this environment lacks |

**Limits of this run:** the sandbox has no outbound network (DNS for `mr-bakhtawar.netlify.app` failed), so no live status codes, redirects, response headers, rendered HTML, Core Web Vitals or Lighthouse figures were collected. Search Console, GA4 and backlink-index data were not available. The earlier audit was independently re-verified against the files; its findings held, with the corrections noted in §3.

## 2. Baseline (before any change)

| Metric | Value | Method |
|---|---|---|
| HTML pages / sitemap URLs | 91 / 88 (404, thank-you, Google verification file excluded correctly) | file scan |
| Canonicals | 90 of 90 self-referencing, one host | parse |
| Broken internal links | 0 | link check |
| Orphan indexable pages | 0 | link graph |
| JSON-LD blocks parse | all | parse |
| Images with alt | 154 / 154 | parse |
| Images without width+height | 4 | parse |
| Blog post body text | ~170 words, ~33 unique | overlap analysis |
| JS errors, mobile (375 px) overflow on 11 sampled pages | none (offline, `file://`) | Playwright |
| CSS / JS size | 67 KB / 3.7 KB | bytes |
| Core Web Vitals, headers, status codes | **Not measured** | no network |

## 3. Findings (full detail in `SEO-ISSUES.csv`)

**Corrections to the earlier audit:** the gallery is described as "self-hosted" in the README but uses GitHub-raw hotlinks (worse than first reported); the backlink tracker has 159 data rows, not 160; there are 12 inline scripts and 203 inline `<style>` blocks, which matters for CSP.

| ID | Sev. | Finding | Status |
|---|---|---|---|
| F-01 | **Critical** | 45 blog posts are one template: ~33 unique words each, 7 of 8 paragraphs shared with 10+ pages, similarity 0.86–0.88 | Verified |
| F-02 | High | Security headers live only in `vercel.json`; the site is on Netlify with no `_headers`/`netlify.toml` | Verified (live headers Not Tested) |
| F-03 | High | 10 docs (23 refs) name `obsolete Vercel hostname`; all live signals use the Netlify host | Verified |
| F-04 | High | Homepage shows ★★★★★ cards with stock avatars (labelled "sample") — review-style trust signal without real reviews | Verified |
| F-05 | Medium | Article schema lacks dates/image; 45 posts have no JSON-LD; BreadcrumbList on 1/91 pages; no trustworthy dates exist in the project | Verified |
| F-06 | Medium | 7 `article-*` pages have no `<h1>` | Verified |
| F-07 | Medium | Thin/overlapping pages: Technical SEO ×4, API integration ×4, AEO ×3 | Verified |
| F-08 | Medium | Hotlinked images (gallery, 125 JSON-LD refs), 4 images lack dimensions, above-the-fold lazy-load on `about.html`, large PNG/JPG | Verified; effect Not Measured |
| F-09 | Medium | `@import` of Google Fonts in `style.css` (render-blocking chain) | Verified; impact Not Measured |
| F-10 | Medium | No CSP | Verified |
| F-11–F-13 | Low | Duplicate descriptions (7 pages), no `lastmod` (no real dates), duplicate IDs, `<time>` misuse | Verified |
| F-14 | Medium | `scripts/sync_identity.py` rewrites every page and the sitemap; it would overwrite approved edits | Verified |
| F-15–F-16 | Info | Open AI-crawler policy (owner decision); backlink tracker review | Verified |

**What is already sound:** canonical/sitemap/noindex hygiene, zero broken links, valid JSON-LD, complete alt text, no fake rating markup in schema, no http:// links, no key-pattern strings in source, noindex correctly kept off robots.txt.

**Important context for F-01:** the posts have almost no page-specific content, so "merging" means writing new original guides, not stitching existing text. Repetition alone does not prove a Google penalty; the risk is thin, near-duplicate pages that serve no distinct search need.

## 4. Proposed content consolidation (45 → 8 pillars)

| Pillar | URL | Absorbs |
|---|---|---|
| P1 Technical SEO | `technical-seo-checklist-mbk.html` (existing) | technical-seo-checklist, robots-txt, xml-sitemaps, canonical-urls, google-indexing, article-technical-seo |
| P2 On-page SEO | `on-page-seo-guide.html` (new) | seo-title-tags, meta-descriptions, image-seo, internal-linking, structured-data, portfolio-seo |
| P3 Content & intent | `content-strategy-and-search-intent.html` (new) | keyword-research, search-intent, content-quality, content-planning, faq-content, local-seo-basics |
| P4 Performance & UX | `web-performance-and-ux-guide.html` (new) | web-performance, responsive-design, user-experience, web-accessibility, web-forms |
| P5 Security & privacy | `web-security-basics-for-small-sites.html` (existing) | api-security, cybersecurity-learning, privacy-by-design, domain-ssl-basics, digital-rights, reverse-engineering-ethics |
| P6 Deploy & maintain | `deployment-and-maintenance-guide.html` (new) | github-workflow, vercel-deployment, website-launch, website-maintenance, developer-documentation, cloud-computing-basics |
| P7 Automation & AI | `automation-and-ai-workflows-guide.html` (new) | ai-workflows, n8n-workflows, automation-basics, data-validation, product-thinking |
| P8 Brand & identity | `personal-branding-and-online-identity.html` (new) | personal-branding, digital-identity, online-reputation, social-profile-links, testimonial-ethics, community-feedback |

Each old URL gets a **301 to its own closest pillar** (never the homepage, never one generic target). Also: `api-integration-for-modern-web-projects.html` → `article-api-integration.html`; the 7 project notes plus `article-ai-automation` and `article-react-performance` stay, gain an H1/date and link to the pillars. Row-by-row mapping: `SEO-URL-MAPPING.csv`; per-page overlap data: `SEO-CONTENT-OVERLAP-MATRIX.csv`. High-inbound URLs needing link updates first: `blog-content-quality` and `blog-personal-branding` (55 inbound links each, site-wide footer).

**Content rules:** pillars will be written as accurate general guidance. No invented experience, results, clients, credentials or statistics. Sections that would benefit from your real project examples will be marked for you to supply.

## 5. Other proposed changes

- **Canonical/domain:** keep `https://mr-bakhtawar.netlify.app/`; update the 10 docs; no custom domain is claimed.
- **Headers (Netlify):** `_headers` at the publish root, with nosniff, Referrer-Policy, `X-Frame-Options: SAMEORIGIN`, Permissions-Policy, HSTS `max-age=31536000` (no preload), and CSP in **Report-Only** first (needs `unsafe-inline` for styles/scripts, Google Fonts, GitHub-raw and pravatar images). `vercel.json` is kept, since the README still describes a Vercel path. **Please confirm the Netlify publish directory.**
- **Schema:** BlogPosting/Article + BreadcrumbList + WebPage on the surviving articles; date properties only from dates you confirm.
- **Images:** self-host gallery images (needs your original files), WebP/AVIF with fallbacks, dimensions, `fetchpriority` on the homepage portrait, remove lazy-load on `about.html` portrait.
- **Fonts:** replace the CSS `@import` with preconnect + link.
- **Metadata:** unique descriptions for 7 pages; H1 on 7 pages; fix duplicate IDs/heading skip; keep 404 and thank-you `noindex`.
- **Sitemap:** rebuild after consolidation (≈47 URLs: 88 − 47 redirected + 6 new pillars); no `lastmod` or image sitemap without a real benefit and real dates.
- **Homepage carousel:** remove star ratings and stock avatars.

## 6. Scoring rubric (measured, source-based)

Score = passed ÷ (passed + failed) checks in each dimension. "Not tested" checks are excluded and listed. This is **not** an official search-engine metric and says nothing about rankings.

| Dimension | Pass | Fail | Not tested | Score |
|---|---|---|---|---|
| Technical SEO | 5 | 3 | 1 | 62 |
| Content quality | 2 | 4 | 0 | 33 |
| On-page SEO | 4 | 2 | 0 | 67 |
| Structured data | 3 | 3 | 1 | 50 |
| Security | 2 | 2 | 1 | 50 |
| Performance | 1 | 5 | 1 | 17 (static checks only; Core Web Vitals unmeasured) |

Equal-weight mean: **47 / 100**. This is a baseline for comparison after fixes, not a grade.

## 7. Backlink tracker (recommendations only)

159 rows, all "Not started". Review buckets: 41 genuine professional profiles, 30 community/open-source, 22 directories (many conditional), 10 editorial/self-publishing, **56 low-value, irrelevant or risky** (bookmarking sites, web-2.0 duplicate blogs, document-sharing sites, spam-prone forums, review sites that require real customers). No paid-link wording was found. Nothing was submitted or contacted. Detail: `SEO-BACKLINK-REVIEW.csv`. Prefer a small set of profiles you will maintain, plus earned editorial and community mentions.

## 8. Risks and expected benefits

**Risks:** retiring 45 URLs with no Search Console evidence on their traffic (check first); redirects misconfigured on Netlify (test before deploy); new content needing your accuracy review; `sync_identity.py` overwriting edits; CSP breaking inline code (hence Report-Only).
**Expected benefits (not guarantees):** fewer near-duplicate URLs to crawl, clearer topic structure, correct security headers, fewer third-party image/font dependencies, trustworthy schema. No ranking, indexing, traffic, backlink or Core Web Vitals improvement is claimed until measured.

## 9. Limitations

No live crawl or headers; no Lighthouse; no Search Console/GA4; HTML validity checked only for IDs, headings and parsing (no W3C validator); mobile checks were offline so remote images/fonts did not load; competitor and keyword data were not collected (no data source).
