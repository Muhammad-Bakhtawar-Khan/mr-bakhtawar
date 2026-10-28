# SEO Roadmap

## A. Needs your input before work starts
1. **Approve** the 45 → 8 consolidation, the redirect plan and the batch order in `SEO-CHANGELOG.md`.
2. **Netlify publish directory** (project root or a subfolder?) so `_headers` and `_redirects` land in the right place.
3. **Real publication/update dates** for each surviving article (otherwise date fields stay out of schema).
4. **Homepage carousel:** remove stars/stock avatars, or supply real, permitted feedback.
5. **Gallery images:** provide originals if you want them self-hosted (GitHub-raw copies are not assumed to be yours to re-host).
6. **AI-crawler policy:** keep all 20 named bots allowed, or disallow training crawlers (GPTBot, CCBot, Google-Extended and similar).
7. Any real project facts and examples you want in the pillar guides (nothing will be invented).

## B. After approval (in order)
1. Backup → batches 1–4 (low risk, quick wins).
2. Batch 5 (images/fonts) with before/after measurements.
3. Batch 6 content, then batch 7 redirects, then batch 8 schema/sitemap.
4. Full test run: links, canonicals, sitemap coverage, JSON-LD, duplicate metadata, redirect loops/chains, image dimensions, console errors, mobile layout.
5. Deploy by you; then **live verification** of headers, redirects and canonicals (curl/Playwright with network), and Lighthouse.

## C. Phase 2 (later)
- Expand the 7 project notes with verified facts, dates and screenshots.
- Resolve AEO overlap (`seo-aeo-geo-for-personal-brands`, `generative-search-entity-clarity`, `answer-engine-content-design`) and thin service pages.
- Tighten CSP (move inline styles/scripts out, drop `unsafe-inline`) and switch Report-Only to enforced.
- Competitor/keyword research when a data source (e.g. Search Console, DataForSEO, Ahrefs) is available.
- Backlinks: maintain a small set of genuine profiles; pursue real editorial and community mentions; no mass submission.

## D. Monitoring plan
| What | Tool | Interval |
|---|---|---|
| Indexation, coverage, sitemap status | Search Console | Weekly for 8 weeks, then monthly |
| Queries, clicks, CTR on pillar pages | Search Console | Monthly; compare after 3 months |
| Conversions (WhatsApp/contact clicks) | Analytics (not currently installed) | Monthly |
| Core Web Vitals, Lighthouse | PageSpeed Insights / Lighthouse | After each deploy; monthly |
| Redirects, headers, canonicals | curl / `/seo drift baseline` then `compare` | After each deploy; quarterly |
| Content accuracy and freshness | Manual review | Every 6 months |
| Verified backlinks | Search Console links report | Quarterly |
| AI-search visibility | Manual spot checks only | Quarterly; treat as anecdotal |

Set baselines first (this audit is the source-based baseline); judge changes only after enough data accumulates (typically weeks to months), and make no claims until measured.
