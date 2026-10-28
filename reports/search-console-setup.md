# Search Console setup and measurement

1. Use the owner's Google account. For a hosted Netlify subdomain, create a
   **URL-prefix property** for `https://mr-bakhtawar.netlify.app/`; do not assume
   control of Netlify's parent-domain DNS.
2. Select an ownership method actually available to the owner. The repository
   contains a Google verification file, but its presence does not prove current
   account ownership or property access. Preserve it and use the token supplied
   by the real Search Console account if a replacement is needed.
3. Publish this build first. Inspect homepage/about/project/service HTML and
   indexing directives on the actual live origin.
4. Submit `https://mr-bakhtawar.netlify.app/sitemap.xml`. It contains 54 distinct
   canonical pages, no redirect aliases, no thank-you/error/verification/internal
   tracker and no fabricated last-modified dates.
5. Inspect key URLs and follow indexing diagnostics. A request is not a guarantee
   of inclusion or timing. Do not misuse the specialized Google Indexing API for
   ordinary portfolio pages.
6. Export Performance by query/page/country/device; save indexing and CWV reports.
   Keep private exports outside `public/` and the distributed ZIP.
7. Start a baseline from observed data. Separate brand/namesake queries, compare
   28-day periods with seasonality, and annotate releases. Do not turn impressions
   into invented search-volume figures.

No Search Console credentials, ownership verification or private data access were
available during implementation. Google Rich Results Test, live URL Inspection
and field CWV checks must be performed after publication.
