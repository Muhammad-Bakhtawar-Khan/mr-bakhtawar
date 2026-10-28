# Publish the existing site safely

This phase does not deploy or alter the production hosting account.

1. Review the source diff and `implementation/validation-summary.json`.
2. Run `pnpm install --frozen-lockfile`, `pnpm build`, type checking and the tools
   documented in `tools/README.md`. Build requires development dependencies for
   Vite/TypeScript, including the build-time homepage renderer.
3. Publish **`dist/` to the existing Netlify site** with the build command
   `pnpm build`. No new domain is required. Keep the generated `_redirects`,
   `_headers`, verification file, robots and sitemap.
4. Confirm `/index.html` and all legacy routes use their intended permanent
   redirects, without loops or new chains. Check a genuinely nonexistent URL
   returns 404, not a soft-404 homepage.
5. Re-run the public audit and inspect the rendered live homepage with JavaScript
   disabled. Ensure text and main links are present in its HTTP HTML.
6. Confirm the new WebP variants and landscape PNG return public image content
   types, and that each live page has exactly one intended metadata set.
7. Submit the sitemap in the actual owner's Search Console property and monitor
   coverage. Source fixes do not themselves establish indexing.

## Sharing

The social PNG remains an absolute URL on the existing production origin:
`https://mr-bakhtawar.netlify.app/assets/images/bakhtawar-portfolio-social-v1.png`.
After publishing, verify HTTP 200 and `image/png`. Then request a scrape in
Meta's Sharing Debugger and test a new WhatsApp message. WhatsApp has a separate
cache; a Meta scrape does not guarantee immediate refresh. A benign `?share=v2`
test can distinguish a cached preview without changing canonical URLs.

## Platform boundaries

Site configuration remains the single homepage metadata emitter; the HTML shell
adds complementary tags without duplicate keys. The surrounding editor/share
wrapper and third-party crawler caches are not controlled by application source.
No new platform, server or CMS was introduced.
