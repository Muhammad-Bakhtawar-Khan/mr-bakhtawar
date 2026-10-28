# Mr. Bakhtawar Portfolio — SEO/AEO/GEO Update Report

## Included
- Updated homepage title and meta description around “Mr. Bakhtawar”, full name, and “Founder of MBK Global”.
- Normalized personal canonical host references to `https://mr-bakhtawar.netlify.app/` where they were the portfolio's own canonical.
- Added descriptive author metadata and filled missing social preview metadata on HTML pages.
- Updated `robots.txt` to allow public crawler access for common search and AI discovery user agents, including GPTBot.
- Updated `llms.txt` with page navigation and public identity context.
- Added a homepage gallery section using the photographs already referenced by `gallery.html`, with lazy loading, alt text, captions and responsive CSS.
- Added 40 SEO/AEO/GEO and website-maintenance notes to `news.html`. They are explicitly written as notes and priorities, not claims that Google has already indexed or ranked the site.

## Important limitations
- `robots.txt` is a request to compliant crawlers; it cannot force a crawler to visit, index, cite, or train on the website.
- Public access for AI search bots is separate from model-training use. GPTBot is allowed by the site policy here, but this does not guarantee training or inclusion.
- Deploying these files does not itself submit a sitemap to Google Search Console.
- Verify the deployed sitemap and representative pages after upload. External project URLs and remote gallery images should be checked from a live browser.
