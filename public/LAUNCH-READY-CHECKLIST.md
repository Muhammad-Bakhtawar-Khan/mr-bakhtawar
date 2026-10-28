# Portfolio launch checklist — review before deployment

## Included in this package
- Unique existing page titles/descriptions retained; canonical and social-sharing tags checked/filled on HTML pages.
- Open Graph and Twitter large-image metadata use the existing locally hosted portfolio photograph. This is a functional fallback, not a custom-designed 1200×630 social card.
- Existing image alt text retained; missing alt attributes filled with a filename-based fallback. Review every alt description manually for accuracy.
- Services page includes visible FAQs and matching FAQPage structured data.
- Privacy policy rewritten to describe the current static site honestly: contact is via external email/WhatsApp links; analytics is not installed by default.
- Added 404 page and thank-you page. The thank-you page explicitly says it does not prove a form was submitted.
- Vercel security response headers configured in `vercel.json`.
- Sitemap rebuilt for public HTML pages; 404 and thank-you excluded. `robots.txt` references the sitemap.
- Internal relative links and archive integrity should be checked again after any domain/page changes.

## Must be completed by the site owner
1. **Confirm the production domain.** This package currently uses `https://mr-bakhtawar.netlify.app` because that is the domain already used by the source portfolio. If your real final URL is different, replace it consistently in every canonical tag, `og:url`, structured data, `sitemap.xml`, and `robots.txt` before deploying.
2. **Create a custom social share image.** Current fallback is the existing portfolio photograph. For best results, create a 1200×630 JPG/PNG with readable branding and test it in social preview tools after deployment.
3. **Analytics:** GA4 is intentionally not installed because no Measurement ID was supplied. If adding GA4, add your real `G-XXXXXXXXXX` ID and implement a consent-management approach appropriate to visitors' jurisdictions before loading non-essential analytics. Do not replace the placeholder with a fake ID.
4. **Forms:** the current contact page is link-based, not a server-backed form. Honeypot fields, rate limiting, server-side validation, spam filtering, and a real success/thank-you redirect cannot be honestly enabled without a form endpoint/provider. Connect a backend first; never put private API keys in front-end code.
5. **Testimonials/reviews:** no fabricated customer reviews have been added. Publish testimonials only with real permission and accurate attribution; if you have none yet, leave them off.
6. **FAQ:** review the five FAQ answers for accuracy and only keep answers that reflect your actual process and services.
7. **HTTPS:** Vercel normally serves deployed sites over HTTPS. Confirm the production URL redirects/loads securely after deployment; the HSTS header is configured for Vercel.
8. **Google Search Console:** add/verify the confirmed production property, submit `/sitemap.xml`, inspect the homepage and important pages, and request indexing where appropriate. Submission does not guarantee indexing or ranking.
9. **Links and image hosting:** click every project/social link and confirm all 25 `myimages` GitHub raw files exist with exactly matching lowercase filenames/extensions.
10. **Privacy/legal review:** update the policy if analytics, a contact form, ads, pixels, or any new data collection is enabled. This template is practical site copy, not legal advice.

## Important limitation
This is a static-site package. It cannot enforce backend anti-spam or server-side validation without a server/function/form provider. No claim is made that analytics, form delivery, or Search Console has been connected or tested live.
