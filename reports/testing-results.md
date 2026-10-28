# Verification results

- `pnpm build`: passed, including static React homepage prerender.
- `pnpm exec tsc --noEmit`: passed.
- `pnpm exec oxfmt --check src/App.tsx src/main.tsx tools/prerender-home.mjs tools/browser_validate.cjs`: passed after formatting correction.
- `python -m py_compile tools/*.py`: passed.
- `python tools/validate_seo.py`: passed; zero detected technical errors.
- `python tools/image_inventory.py`: 118 assets inventoried.
- Browser fixture: all 54 canonical pages passed at 1440 and 390 pixels, with
  no recorded runtime/hydration errors, image-load failures or document overflow.
- Hydrated directory search, clipboard fallback, theme switching and menu/Escape
  dismissal passed. Three form compose flows passed with `window.open` intercepted;
  no real messages were sent.
- Original form nodes/actions/names/options match the saved baseline.
- Built audit checked 106 static image usages and
  5489 internal anchor usages.
- Keyword records: 191, deduplicated with source/date/confidence and canonical targets.
- Public final crawl: 109 fetched resources, no fetch errors; 60 HTTP 200/49 HTTP 301.
- Browser test fixes: excluded the intentionally empty lightbox placeholder from
  missing-asset checks and waited for the asynchronous clipboard result. A format
  check initially failed on the test script, was corrected and passed.

No dedicated lint or unit-test script exists. Google Rich Results Test, private
Search Console, Lighthouse/PageSpeed, field CWV and physical-device tests were not
run; no substitute pass is claimed. Production changes are not published.

Machine evidence: `implementation/validation-summary.json`,
`implementation/rendered-validation.json`, individual CSVs and raw public responses.
