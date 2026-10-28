# Portfolio branding and verification

## Source and scope

The workspace initially contained an empty React starter. Both supplied ZIP
attachments have the same SHA-256 checksum. The portfolio source, public pages,
assets, scripts, directory and gallery data were restored from that archive.
Existing environment scripts and dependencies were retained.

Production identity: **Mr. Bakhtawar Portfolio**  
Owner: **Bakhtawar Khan**  
Descriptor: **Personal Digital Portfolio · MBK Global**  
Existing production origin: **https://mr-bakhtawar.netlify.app**

## Changed areas

- `src/App.tsx`: text-only identity, responsive navigation, homepage introduction,
  founder feature, footer and branded sharing title. Retained directory filtering,
  gallery controls, native sharing/clipboard fallback and navigation destinations.
  Added Escape-key handling to the React mobile menu.
- `src/index.css`: restored existing homepage styles; removed unused monogram rules.
- `public/about.html`: named editorial founder introduction, existing portrait,
  technical-interest feature and project/contact calls to action. Kept existing
  project ecosystem, principles, process, FAQ, directory and contact links.
- `public/assets/css/portfolio.css`: deleted the pseudo-element that generated
  the circular founder initials badge rather than hiding it.
- `public/assets/css/identity.css`: shared responsive personal identity and founder
  styling using the existing palette and typography; reduced-motion support.
- `index.html` and `.figma/make/site.json`: a single emitted homepage description
  and social metadata set; production canonical; absolute HTTPS sharing image;
  crawler-visible titles, social tags and structured data. Removed the inherited
  production indexing prohibition; `public/robots.txt` remains the original
  public crawling policy.
- `public/**/*.html`: consistent header/footer identity, site name, website
  structured-data name, preview image and icons. Preserved page-specific titles
  and descriptions, redirects and form/script behavior. Consolidated duplicate
  metadata, including the gallery page's duplicate social URL.
- `public/assets/images/bakhtawar-portfolio-social-v1.png`: real 1200 × 630 PNG,
  using an existing owner-supplied portrait and the requested personal identity.
- `public/favicon.svg`, `public/assets/images/favicon.svg`,
  `public/assets/images/portfolio-icon-*.png`, `public/site.webmanifest`:
  non-circular personal icons and updated installable-site identity.
- `package.json`: customizable project name only; no dependency changes.
- `vite.config.ts`: default title string only; no changes to platform plugin logic.

No occurrences of the unwanted template title remain in the current project
source, including hidden configuration files. Vendor dependencies and Git history
are outside this source audit.

## Completed verification

- `pnpm build`: passed.
- `pnpm exec tsc --noEmit`: passed.
- `pnpm format src/App.tsx`, followed by
  `pnpm exec oxfmt --check src/App.tsx`: passed.
- Built-document audit across 105 root HTML files: relevant content pages have
  exactly one required metadata entry per key, with absolute production image
  URLs. Redirect documents, the 404 document and the unmodified Google verification
  document are treated separately.
- All original static-page anchor destinations and named form controls were
  compared against the supplied archive: retained. No broken local file
  references were introduced.
- Homepage and founder page: browser-tested at 320, 390, 768, 1024 and 1440-pixel
  viewport widths without horizontal overflow. Inspected desktop/mobile
  screenshots and light/dark themes.
- Mobile navigation and Escape dismissal, theme toggle, directory search and
  clipboard-sharing fallback: passed. No browser page errors during those checks.
- Projects, services, contact, hiring, gallery, case studies, manifest and preview
  image: HTTP 200 locally; preview has `image/png` content type and 1200 × 630 pixels.
- External project availability, real email delivery, WhatsApp message delivery
  and OS-native share-sheet completion are not claimed as end-to-end tested.

## Public deployment findings and remaining step

The production homepage was fetched directly, including with a WhatsApp user
agent. It still serves the previous deployment:

- previous homepage and social titles;
- duplicate descriptions;
- no homepage canonical or `og:url`;
- a relative portrait URL rather than a landscape sharing card;
- `noindex, nofollow`.

The new image URL currently returns **404 on production** because these changes
have not been published there. It is available in the local preview and build.
No live WhatsApp cache refresh or production deployment is claimed.

Publish this project's build to the existing Netlify site, with `dist` as the
published output. Do not change the origin or redirect existing URLs. Confirm
the live HTML contains one metadata set and that the following URL returns a
public HTTP 200 response with `Content-Type: image/png`:

https://mr-bakhtawar.netlify.app/assets/images/bakhtawar-portfolio-social-v1.png

The repository's site configuration previously injected extra metadata into the
homepage. That configuration is now aligned with the HTML shell. No evidence of
additional host-injected personal branding was observed on the supplied Netlify
URL. Source edits cannot control the surrounding editor or an unrelated share URL.

After deployment, use Meta's Sharing Debugger to request a new scrape, then test
the exact production URL in a new WhatsApp message. WhatsApp maintains its own
cache; Meta's re-scrape does not guarantee an immediate WhatsApp refresh. If the
old preview persists, wait for cache expiry or test a benign versioned URL such
as `https://mr-bakhtawar.netlify.app/?share=v2` while retaining the canonical URL.
Already-sent messages may retain their original preview.
