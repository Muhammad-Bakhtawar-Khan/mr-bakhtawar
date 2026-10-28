# Post-deployment SEO & Identity Monitoring

## Immediately after deployment

1. Open the homepage, founder profile, official links directory, all five new service pages, Contact and Book a Call on a phone and desktop.
2. Confirm the deployed hostname is the expected personal portfolio domain. The brand website remains `https://mr-bakhtawar.netlify.app/`.
3. Check that every canonical URL returns the matching page and that `index.html` does not compete with the root homepage.
4. Open `/robots.txt`, `/sitemap.xml` and `/llms.txt`; confirm HTTP 200 and correct contents.
5. Confirm `OAI-SearchBot` is allowed by robots.txt and that any CDN/WAF does not block legitimate crawler requests. Keep `GPTBot` policy separate.
6. Submit a test Book a Call form on mobile. Confirm WhatsApp opens with all entered fields and that the user must press Send. Verify no unintended personal data is placed in the URL or analytics.
7. Click every project and social link. Recheck the MBK Downloader redirect destination and MBK Markets content before promoting them.

## Search engine checks

- Google Search Console: inspect important URLs, review indexing/canonical reports, submit the sitemap, monitor crawl stats and enhancement reports.
- Bing Webmaster Tools: submit sitemap and review crawl/index coverage.
- Rich Results Test / Schema Markup Validator: check the homepage, founder profile and service pages. Structured data validity does not guarantee rich results.
- Lighthouse or PageSpeed Insights: review mobile performance, accessibility, best practices and SEO.
- Use server/hosting logs to inspect status codes and bot access if available. Do not infer crawler access solely from robots.txt.

## Monthly review

- Reconfirm official profile URLs and ownership.
- Update project status, screenshots and service scope.
- Review broken internal/external links and redirect chains.
- Compare impressions, clicks and landing-page queries without promising a particular ranking.
- Remove or correct outdated claims and duplicate content.
- Review privacy policy and form handling if analytics, storage or backend processing is added.

## Success criteria

Success means accurate identity information, crawlable and canonical pages, useful service explanations, functioning contact flows, clear project attribution and measurable improvement in relevant search discovery. Rankings, knowledge panels, AI citations, traffic volume and leads cannot be guaranteed.
