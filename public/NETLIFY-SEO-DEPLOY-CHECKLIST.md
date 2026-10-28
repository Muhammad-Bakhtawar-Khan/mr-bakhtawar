# Netlify SEO Deployment Checklist

This static portfolio is configured for `https://mr-bakhtawar.netlify.app/`.

1. Deploy the contents of this folder to the Netlify site `mr-bakhtawar`.
2. After deployment, open `/sitemap.xml` and `/robots.txt` and confirm they return the XML and text files, not a 404 or the homepage.
3. In Google Search Console, add/verify the Netlify property and submit `sitemap.xml`.
4. Inspect the homepage and a few existing HTML pages. Confirm each canonical URL uses `https://mr-bakhtawar.netlify.app/`.
5. Keep the separate MBK Global and other project URLs in `sameAs`/project links where relevant; they are not replaced because they are separate sites.

Note: This updates the static code and sitemap. It does not submit the sitemap to Google or guarantee indexing/ranking.
