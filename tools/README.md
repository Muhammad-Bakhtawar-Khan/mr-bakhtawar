# Repeatable SEO tools

These tools run locally. They do not publish, access private analytics, acquire
backlinks, send WhatsApp messages or edit third-party profiles.

## Requirements

Use the project's existing Node/pnpm toolchain. Audit scripts require Python 3.10+
and `python -m pip install -r tools/requirements.txt`. Python dependencies are
tooling only, not website runtime dependencies. Browser checks require Playwright
and a compatible Chromium installation; they are optional tooling, not a new
frontend framework.

## Commands

```sh
pnpm build
pnpm exec tsc --noEmit
python tools/seo_audit.py regression
python tools/validate_seo.py
python tools/image_inventory.py
```

- `pnpm build` runs Vite followed by `prerender-home.mjs`. The renderer transpiles
  the existing App, imports its real directory/gallery data and renders initial
  React state into the built homepage. It starts no server and makes no network
  requests. React hydrates that same markup in production. Future changes to
  App imports require updating the explicit build-time import handling.
- `seo_audit.py initial --live` created this project's immutable initial baseline.
  It refuses to overwrite an existing initial snapshot. Use `regression --live`
  for a fresh public crawl. Fetches are limited to five workers, bounded by a
  timeout and retain initial 3xx statuses instead of pretending aliases are pages.
  Review snapshot diffs rather than replacing historical evidence.
- `validate_seo.py` checks all built HTML, page titles/descriptions, canonical and
  sitemap sets, robots, H1, JSON-LD syntax/IDs/headlines, local links, image delivery,
  original form attributes, keyword provenance and complete route reconciliation.
  It exits nonzero on detected technical failures. It does not replace Google's
  Rich Results Test or field Core Web Vitals measurement.
- `image_inventory.py` inventories originals, responsive copies and static
  references. Subject descriptions are based on the saved contact sheet; it does
  not infer a photograph's place, date, qualifications or commercial success.
- `optimize_images.py` is a dry run by default. `--write` generates delivery copies
  only in `public/assets/images/optimized/` plus a delivery map. It never alters or
  deletes originals and does not rewrite references automatically.
- `python tools/package_project.py --output /tmp/mr-bakhtawar-seo-project.zip`
  creates a new source/build/evidence ZIP, file-hash manifest and checksum sidecar.
  It refuses to overwrite an existing archive, excludes dependency/Git/runtime/
  environment/private-export folders and verifies ZIP integrity. Review the
  manifest for sensitive files before distributing any future package.
  Add `--source-only` to omit reproducible `dist` output when attachment limits
  require a smaller source export; all original/delivery image assets stay included.

## Browser verification

```sh
node tools/browser_validate.cjs
python tools/validate_seo.py
```

Use `PLAYWRIGHT_MODULE` for an already-installed Playwright module if it is not
resolvable from this project, and `CHROMIUM_EXECUTABLE` for a system Chromium.
The captured environment used:

```sh
PLAYWRIGHT_MODULE=/opt/playwright-mcp/node_modules/playwright \
CHROMIUM_EXECUTABLE=/usr/bin/chromium node tools/browser_validate.cjs
```

The fixture serves built files through Playwright request interception; it does
not start or replace the supervised development server. It checks every canonical
page at desktop/mobile widths, loads image copies, checks runtime/hydration errors
and exercises navigation. The three forms are tested with `window.open`
intercepted: prepared WhatsApp URLs are verified, **no enquiry is sent**.

`localFixtureLoadMs` is a local test duration, not LCP, INP, CLS or a field result.
Screenshots are local rendered evidence, not proof of production deployment.

## Safety

Keep private analytics exports and credentials outside `public/`. Do not include
them in ZIPs. Never run old mutating identity helpers without reviewing their diff.
The existing public identity configuration was aligned in this update to avoid
restoring outdated names/profile assertions. All new reports are outside the
public website directory.
