# SEO maintenance

## Every release

- Run the prescribed build, TypeScript check, static SEO validator and browser
  fixture. Review route reconciliation and the keyword target set.
- Check new/changed titles, descriptions, main headings, visible breadcrumbs,
  appropriate schema and final internal destinations.
- Rebuild responsive copies only when images change; keep originals and update
  references using the delivery map. Do not replace meaningful alt with a name
  keyword repeated everywhere.
- Regenerate sitemap entries only for actual eligible canonical pages; do not
  automatically assign today's date as lastmod.
- Review forms and contact workflows without sending real test enquiries.
- Search for secrets before packaging; exclude `.env`, credentials, private
  exports, dependency folders, Git history and previous archives.

## Monthly

Export Search Console, compare coverage and branded/non-branded query groups,
check production redirects/404s and inspect genuine orphaned pages. Review
outbound project/profile availability without assuming third-party uptime.
Record actual field CWV where a sufficient sample exists; local timings are not
field metrics.

## Quarterly

Review service scope, project evidence, author biography and public profile
consistency. Validate that geographic targeting reflects real customers and
capability rather than generated city pages. Refresh official technical
references and content that has genuinely become outdated.

Historical snapshots are immutable evidence. Use
`python tools/seo_audit.py regression --live` for a new limited public crawl and
keep its collection time. The regression tools are not a substitute for human
review, Google's interpretation of schema, or private analytics.
