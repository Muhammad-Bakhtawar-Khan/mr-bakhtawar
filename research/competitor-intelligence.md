# Competitor and entity intelligence

## Collection and limitations

See `evidence/collection.json` and `evidence/secondary-serp.json`, with exact query
URLs, response dates, status codes and saved response bodies. Four branded/
professional query groups were attempted on Google and Bing; three were also
attempted on DuckDuckGo.

- Google returned HTTP 302 redirects to its `/sorry/` challenge. No challenge was
  bypassed and no Google rankings are reported.
- DuckDuckGo returned HTTP 202 challenge documents, not usable results.
- Bing returned HTTP 200 documents but the extracted result sets were unrelated
  to the complete queries (e.g. internet speed tests for the portfolio query,
  dictionary entries for “Mr”). They fail the relevance quality gate and are
  excluded from competitive conclusions. A response status is not proof of a
  valid SERP.

**No reliable direct competitor or competitor ranking was verified in this
environment.** Competitor traffic, authority, backlinks, positions, keyword
coverage and geographic visibility are unknown. The gap CSV explicitly records
blocked query groups instead of presenting fabricated competitors.

## Observed name ambiguity, not competitors

Google's autocomplete endpoint returned actress-related suggestions for
“bakhtawar khan” and MBK consultancy/holding/career suggestions. These are evidence
of returned phrases only—not proof that the searches refer to this person or
business. Actress, spouse, age, drama, careers, Qatar and holding-company queries
were excluded. No other person's biography or business facts were imported.

## Public identity corroboration

The source-listed GitHub profile responded HTTP 200 with a matching founder/
MBK Global description. The source-listed DEV profile responded HTTP 200 with a
matching name, technical description and cross-link to that GitHub account. The
DEV personal website points to `mbkglobal.vercel.app`, not the current canonical
portfolio. Owner-controlled profile consistency is therefore a concrete action.
This is corroborating public self-description, not legal identity verification.

Twitch returned a generic shell; profile-specific details could not be verified.
It remains a visible existing link but is not used as a verified schema identity.

## Realistic differentiation

Use the full personal name with the public brand, stable entity IDs and a single
official URL. Publish original project decisions, screenshots, reproducible
examples and honest limitations. Existing project claims such as coin coverage
need owner evidence before promotion. Stronger substance is preferable to
creating hundreds of name/location variants.

## Next evidence request

Provide a Search Console query/page export and a consented localized SERP export
for Pakistan (and any genuinely served markets). Record engine, date, device,
country, query, result URL and whether it is organic, local, paid or a profile.
Inspect the top relevant pages individually; exclude namesakes and unrelated
organizations. Only then add comparative content/backlink findings.
