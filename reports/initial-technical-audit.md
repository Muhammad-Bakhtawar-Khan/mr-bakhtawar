# Initial technical audit

The full source inventory and public fetch took place before website changes in
this phase. Machine-readable evidence is in `reports/evidence/initial/`; exact
collection times, initial HTTP status, redirects, headers, errors and extracted
metadata are retained per URL. These records are observations, not search ranking
or traffic measurements.

## Coverage

- 106 source HTML documents, including the React homepage shell and the nested
  internal backlink tracker.
- 48 configured legacy redirects: these are URL aliases, not 48 additional
  independent articles.
- `/index.html` is an additional homepage variant, not separate content.
- 109 public requests: 60 HTTP 200 and 49 HTTP 301 responses. Includes robots and
  sitemap resources. No public request in this crawl was inaccessible.
- 54 source sitemap entries. No dynamic route framework or parameterized content
  routes were found. React's directory filters do not create new indexable URLs.
- The public Google verification token is a verification resource, not content.
  The 404, thank-you page and backlink tracker are utilities, not landing pages.

## Evidence-backed priorities

1. Homepage main content is client-rendered; HTML-only crawlers receive no H1 or
   meaningful main content. Add static build-time prerendering, not a new backend.
2. Five pages repeat entire JSON-LD graphs: gallery (five graphs), contact,
   projects, news and social (three graphs each). Deduplicate entity definitions
   and align types with visible page purposes.
3. Some titles are truncated in the middle of words. Several educational pages
   have only generic WebPage schema. Short content needs editorial assessment,
   not automatic padding or an arbitrary word-count target.
4. Profile sameAs links and professional titles require evidence review. Source
   links alone are owner-supplied assertions, not independent ownership proof.
5. Some image elements intentionally use empty alt text; do not replace them with
   repeated founder names. Examine each usage and intrinsic file format. Inventory
   all assets and rendered references before optimization.
6. Repeated legacy internal links need normalization to final destinations; keep
   the redirects themselves for existing inbound URLs.
7. The active live site must be compared with the changed source after publishing.
   A local fix is not evidence of a production fix, indexing or a rich result.

## Limits

No Search Console, analytics, Keyword Planner export, paid backlink dataset,
field Core Web Vitals, client deliverables, confirmed international targeting,
business address or credentials were supplied. They are not inferred. Baseline
ranking, traffic, conversion, search volume, difficulty, CPC and backlink metrics
remain unknown.
