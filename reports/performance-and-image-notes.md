# Performance, images and accessibility

## Implemented and measured locally

- The existing React homepage is statically rendered at build time and hydrated
  with the same component. No second page implementation or runtime backend was
  added. Primary text/links no longer depend on JavaScript execution in production
  HTML.
- 35 supplied gallery images have 70 generated WebP delivery variants. Original
  files and URLs remain intact. The equivalent largest selected delivery files
  total 4,546,346 bytes versus 5,709,982 original bytes (20.4% smaller in aggregate).
  This is an asset-set comparison, not a measured page-transfer reduction or CWV
  score. Individual encodings may differ; smaller viewport srcsets reduce
  transfer where selected by the browser.
- Active static/React/archive references use genuine WebP files, explicit
  dimensions, srcset/sizes and contextual loading. The homepage portrait keeps
  high fetch priority; repeated offscreen archive images remain lazy.
- Four original filenames have JPEG bytes despite PNG/WebP suffixes. Rather than
  silently breaking historical URLs or replacing originals, active references
  now use correctly encoded delivery paths. Legacy originals remain inventoried.
- The full image inventory contains 118 original/generated/icon assets. The
  saved contact sheet was inspected; descriptions do not infer places, dates,
  professional accomplishments or endorsement from portrait backgrounds.
- Fonts retain explicit stylesheet links, existing fallback stacks and
  `display=swap`. No unnecessary font family or platform was added.
- Exact `X-Robots-Tag: noindex, nofollow` header rules exclude historical public
  audit documents and maintenance data from search landing-page eligibility.
  These header policies require production publication before taking effect;
  robots crawling is not blocked, so crawlers can observe noindex.

## Interpretation boundaries

Browser fixtures check rendering and overflow at 1440 and 390 pixels across all
54 canonical pages, plus functional controls/forms. They are not accessibility
certification, cross-browser certification or physical-device testing.
Existing focus states, keyboard menu dismissal, semantic main landmarks and
reduced-motion behavior are retained.

Lighthouse/PageSpeed and field LCP, INP, CLS/CrUX results were not collected.
`localFixtureLoadMs` is just test duration under a local built-file fixture. No
Core Web Vitals pass or performance ranking benefit is claimed. Use real-device
and field measurements after publication before further bundle/font tuning.
