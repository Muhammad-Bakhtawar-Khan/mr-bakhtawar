# Mr Bakhtawar SEO project

The actual Vite/React portfolio source is at this repository root; the deployable
build is `dist/`. SEO research, evidence, implementation records and tools live
outside `public/` so they are not automatically exposed as website content.

## Identity and scope

- Public brand: **Mr Bakhtawar**
- Personal name: **Bakhtawar Khan**
- Business/project brand: **MBK Global**
- Existing production URL: **https://mr-bakhtawar.netlify.app/**

The complete inventory accounts for 106 source HTML documents plus the
`/index.html` alias. There are **54 distinct canonical indexable pages**, not
106 independent articles. The remaining documents include 48 legacy redirects
and four verification/error/form/internal-planning utilities.

The keyword master has **191 records**: 22 observed suggestion records and 169
clearly labeled source/owner-supported candidates. None has a measured search
volume, CPC or difficulty. The 10,000 objective remains unfulfilled rather than
being filled with generated variations.

## Build and audit

```sh
pnpm install --frozen-lockfile
pnpm build
pnpm exec tsc --noEmit
python -m pip install -r tools/requirements.txt
python tools/validate_seo.py
python tools/image_inventory.py
```

Do not start a second server in Figma Make; its preview server is supervised.
The production build now prerenders the existing React homepage; React hydrates
it so its directory, share action, menu, filters and gallery remain interactive.

See `tools/README.md` for complete audit/browser commands and safety notes.

## Deliverables

- `research/`: keyword master and subsets, source/evidence collection, keyword
  clusters, page targets, image inventory, competitor limitations, answer map
  and researched ethical-authority opportunities.
- `implementation/`: individual page plan and validation records, change log,
  responsive-image map, form baseline, browser results and screenshots.
- `content/`: evidence-gated editorial calendar and specific article briefs.
- `reports/`: complete initial inventory, baseline, technical audit, scoring,
  roadmap, all-pages reconciliation, performance notes, launch/maintenance guides
  and explicit remaining blockers.
- `tools/`: repeatable, tested local inventory, validation, browser, prerender and
  image-generation tools.

The packaging tool can include source, reports, evidence and `dist`. The
downloadable source-only export omits the reproducible `dist` folder to fit the
attachment export limit; run `pnpm build` to regenerate it. All website assets
are retained. Dependencies, Git history, environment files, private exports and
the ZIP itself are excluded.

## What this delivery does not claim

No production deployment, indexing, ranking improvement, knowledge panel, rich
result, acquired backlink, AI citation, private analytics access or field Core
Web Vitals result is claimed. All indexed pages are marked **Partially complete**
overall while their local technical validation is recorded separately.

Direct competitor SERP identification was blocked by challenges/unusable result
sets. Original client results, qualifications, foreign-market delivery, Shopify
specialization and project coverage metrics were not invented.

For publication and Search Console, follow `reports/deployment-guide.md` and
`reports/search-console-setup.md`. Earlier reports inside `public/` and
`BRANDING-REPORT.md` are historical source material, not the validation authority
for this phase; use the current `implementation/` records.
"# mr-bakhtawar" 
