# SEO Changelog

**No changes have been applied.** The project is unchanged; the audit worked on a scratch copy. This file lists the *planned* changes, grouped so they can be approved and applied in small, tested batches. After approval, each batch will be recorded here with the files actually modified and the test results.

## Safety steps before batch 1
1. Create a Git checkpoint (or zip backup) of the project as delivered.
2. Run the baseline tests again (links, canonicals, JSON-LD, duplicates).
3. Do not run `scripts/sync_identity.py` at any point (it rewrites all pages and the sitemap).

## Planned batches

| Batch | Files | Change | Reason (finding) | Risk |
|---|---|---|---|---|
| 1 Config | `_headers` (new) or `netlify.toml` (new), `vercel.json` (kept, unchanged) | Add Netlify headers; CSP Report-Only | F-02, F-10 | Low; confirm publish directory |
| 2 Docs | README.md and 9 other `.md` files | Replace old Vercel domain, correct deployment/gallery claims | F-03 | None |
| 3 Quick fixes | 7 `article-*` pages; about pages; `projects.html`, `book-a-call.html`, `changelog.html`, `resume.html`; `news.html` | Add H1; unique descriptions; fix IDs/heading; `<time>` → `<span>` | F-06, F-11, F-13 | Low |
| 4 Homepage trust | `index.html` | Remove star ratings and stock avatars from carousel | F-04 | Low; design preserved |
| 5 Images/fonts | `index.html`, `about*.html`, `gallery.html`, `assets/css/style.css`, new `assets/images/*` | Dimensions, loading attributes, WebP, self-host (needs your originals), font loading | F-08, F-09 | Medium |
| 6 Content | 6 new pillar pages; rewrite `technical-seo-checklist-mbk.html`, `web-security-basics-for-small-sites.html`; update `blog.html`, footer links | Original guides, internal links | F-01, F-07 | Medium; needs your review |
| 7 Redirects | `_redirects` (new) | 47 permanent 301s, each to its closest page (see `SEO-URL-MAPPING.csv`); remove the 47 retired source files only after you approve and the redirects are tested | F-01 | Medium |
| 8 Schema/sitemap | affected pages, `sitemap.xml`, `llms.txt`, `identity-config.json` | BlogPosting/BreadcrumbList; rebuild sitemap; keep identity data consistent | F-05, F-12 | Low |

## Not changing
Visual design, navigation, contact/WhatsApp functionality, `robots.txt` bot policy (owner decision), `vercel.json`, brand assets, existing project URLs outside the mapping.
