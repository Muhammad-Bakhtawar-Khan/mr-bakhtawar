# Transparent prioritization

The CSV priority score is an internal sorting aid, never a ranking forecast:

`min(100, brand relevance × 6 + business relevance × 5 + intent value × 3
+ observed-suggestion flag × 10 + 12)`

- Brand relevance: 1–5; explicit personal brand terms receive 5.
- Business relevance: 1–5, based on the site's actual offered scope.
- Intent value: navigational 5, commercial 4, informational 3, visual 2.
- Observed-suggestion flag: 1 only when the endpoint returned the exact phrase.
  This is weaker than measured demand and is not a volume estimate.
- 12 is a common existing-page implementation-feasibility allowance. It does not
  pretend to distinguish effort where there is no supporting estimate.

Competition and quantified potential value are unknown and not imputed.
Dependencies and effort are handled in the page plan and roadmap rather than
inventing numerical precision. Revise the model with real GSC and conversion data.

## Engineering gates override scores

P0: prevent false claims, malformed/duplicate schema, broken canonical routing,
missing crawlable homepage content or accidental indexing of internal utilities.
P1: branded identity, image correctness, links, useful headings and answer clarity.
P2: original evidence-based case studies and educational expansion.
P3: speculative markets/topics pending evidence. Never publish doorway pages to
improve a spreadsheet score.
