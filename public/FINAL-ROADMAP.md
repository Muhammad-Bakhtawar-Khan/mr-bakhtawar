# Final Roadmap

## Before deployment
1. Review `SEO-URL-MAPPING.csv` and the 47 configured force redirects. Search Console and backlink-index evidence was not available; reverse any mapping that owner data suggests should be retained.
2. Confirm Netlify publishes the repository root. If the configured publish directory differs, place `_headers` and `_redirects` in the actual publish directory.
3. Review the six new pillar guides for owner-specific examples and any factual corrections. No owner experience or results were invented.
4. Review the system-font fallback visually; the Google Fonts CSS import was removed to avoid a render-blocking CSS import chain.
5. Confirm that the site's HTTPS deployment supports HSTS. Keep CSP in report-only mode while checking browser reports; do not enforce until legitimate inline code and integrations have been reviewed.
6. Review remote image licensing and dimensions if original assets or permissions become available.
7. Keep `vercel.json` only for its documented Vercel use; it does not configure Netlify response headers.

## After deployment
1. Run the `curl -sSI` commands in `README.md` and inspect actual headers.
2. Test each redirect source and confirm one-hop 301 behavior, no loops/chains, and correct final canonical.
3. Fetch the sitemap and robots.txt over HTTPS; submit the sitemap in Search Console if owner access is available.
4. Use a real browser at 375px, 390px, tablet and desktop widths; inspect keyboard focus, forms, console errors, image loading and carousel behavior. Do not send actual messages.
5. Run Lighthouse/PageSpeed Insights and review field data when available. Treat LCP ≤ 2.5 seconds, INP ≤ 200 ms and CLS ≤ 0.1 as targets only.
6. Recheck Search Console queries, indexing, inbound links and conversions after enough post-deployment data accumulates.
7. Tighten CSP only after reviewing report-only violations and migrating inline code if practical.

## Deferred
- Search Console/backlink analysis and performance-based redirect refinement (requires owner exports or credentials).
- Rehosting/conversion of third-party gallery images (requires verified originals and permission).
- Confirmed article publication/update dates (owner evidence required).
- Browser visual and JavaScript console testing (Chromium browser binary unavailable in this environment).
