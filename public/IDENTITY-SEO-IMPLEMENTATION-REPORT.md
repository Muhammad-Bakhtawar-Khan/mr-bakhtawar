# MBK Global / Muhammad Bakhtawar Khan — Identity & SEO Update

## Implementation completed in this source package
- Added a dedicated founder identity page: `about-muhammad-bakhtawar-khan.html`.
- Added a central public links/project directory: `official-links.html`.
- Added service landing pages for web development, AI/API integration, technical SEO, web security practices, and digital branding.
- Added `identity-config.json` as the central maintainer-facing source of identity, contact, profile and project data, plus `scripts/sync_identity.py` to synchronize contact data, core Person/Organization JSON-LD and the sitemap, and `scripts/validate_identity.py` to validate the package.
- Updated homepage identity messaging to use the conservative, owner-supported title `Founder of MBK Global` rather than asserting CEO without a fresh explicit confirmation.
- Updated Organization structured-data identifiers to use the brand domain (`https://mr-bakhtawar.netlify.app/#organization`) and added a contact point on the homepage schema.
- Added internal links from major portfolio pages to the founder profile, link directory and brand website.
- Changed Book a Call form behavior to prefill a WhatsApp request for +92 320 0276941. Visitors must review and press Send; it does not create a calendar booking or transmit automatically.
- Updated `robots.txt` to allow `OAI-SearchBot` for search discovery while keeping `GPTBot` disallowed for training, reflecting separate controls. Other AI crawlers remain restricted.
- Rebuilt `llms.txt` as a factual navigation aid and regenerated `sitemap.xml` from canonical static HTML pages, excluding the `index.html` duplicate, `404.html` and `thank-you.html`.
- Removed invalid closing tags for void HTML elements and keyword-stuffed `meta keywords` tags; corrected three pre-existing invalid JSON-LD blocks on Book a Call, Resume and Changelog pages.
- Added `IDENTITY-CONTENT-ARCHITECTURE.md` and `POST-DEPLOYMENT-MONITORING.md` for page mapping, answer coverage, ethical reputation guidance and post-launch checks.

## Live evidence checked during this update
- `https://mr-bakhtawar.netlify.app/` — page content was accessible; identifies Muhammad Bakhtawar Khan as founder of mbkGlobal and lists the public phone and several profiles.
- `https://mr-bakhtawar.netlify.app/` — page content was accessible; personal portfolio links to the brand and projects.
- `https://mbktv.vercel.app/` — page content was accessible and identifies MBK TV as a project by MBK Global.
- `https://mbkmarkets.vercel.app/` — URL opened but useful rendered text was not readable in the inspection, so page claims should be reviewed manually.
- `https://mbkdownloader.vercel.app/` — inspection showed a redirect to `https://videodownloaderbymr-bakhtawar.netlify.app/`; destination was not readable in the inspection. Confirm final URL, project status and legal/content compliance before promoting it.
- `https://noorquranbymbk.vercel.app/` — page title was accessible.
- OpenAI's official crawler documentation states that `OAI-SearchBot` supports ChatGPT search discovery and is distinct from `GPTBot`, which relates to training: https://developers.openai.com/api/docs/bots

## Validation performed locally
- `scripts/validate_identity.py`: passed.
- Sitemap XML parse: checked by the build script.
- Structured data JSON blocks: checked by the build script after generation.
- Internal relative links: checked for target existence where applicable.
- JavaScript syntax: checked with Node.js when available.
- HTML parse/build and live deployment were not run here; this is a static HTML package, not an actual deployment.

## Owner review needed
1. Confirm whether `Founder & CEO` is the approved public title. Until then, the new founder page uses `Founder`.
2. Recheck social account ownership and exact URLs (especially LinkedIn, GitHub and Twitch).
3. Review the MBK Markets live content and the MBK Downloader redirect destination.
4. Confirm which services are commercially available now versus areas of interest or planned work.
5. Recheck Instagram, Facebook, X and Pinterest links. Some platforms restricted automated inspection; the links were taken from the live brand site. Replace the Facebook share URL with a stable profile URL if available.
6. After deployment, check status codes, canonical tags, robots.txt, sitemap availability, form behavior on mobile, Google Search Console and Bing Webmaster Tools.
7. `llms.txt`, structured data and metadata help clarify content but do not guarantee indexing, knowledge panels, featured snippets or AI citations.
