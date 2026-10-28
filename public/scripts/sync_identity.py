#!/usr/bin/env python3
"""Synchronize core public identity/contact fields from identity-config.json.

Run from any directory with: python scripts/sync_identity.py
Review the resulting diff before deployment. This is a static-site helper, not a deployment tool.
"""
from pathlib import Path
import json, re, html, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
config = json.loads((ROOT / 'identity-config.json').read_text(encoding='utf-8'))
person, brand = config['person'], config['brand']
portfolio_url = person['url'].rstrip('/')
brand_url = brand['url'].rstrip('/')
email = person['email']
wa_url = person['whatsappUrl']
phone = person['whatsapp']
same_as = person.get('schemaSameAs', [])

# Keep visible contact details consistent across existing static pages.
for page in ROOT.rglob('*.html'):
    source = page.read_text(encoding='utf-8', errors='replace')
    source = re.sub(r'https://wa\.me/\d+', lambda _: wa_url, source)
    source = source.replace('mailto:Bakhtawark085@gmail.com', 'mailto:' + email)
    source = source.replace('Bakhtawark085@gmail.com', email)
    source = source.replace('+92 320 0276941', phone)
    source = source.replace('03200276941', phone.replace('+', '').replace(' ', ''))
    # Update structured data on the two primary identity pages from the same config.
    if page.name in {'index.html', 'about-muhammad-bakhtawar-khan.html'}:
        def update_jsonld(match):
            try:
                data = json.loads(match.group(1))
            except Exception:
                return match.group(0)
            graph = data.get('@graph', [])
            if not graph and isinstance(data, dict): graph = [data]
            for node in graph:
                typ = node.get('@type')
                if typ == 'Person' and node.get('@id', '').endswith('/#person'):
                    node['name'] = person['name']
                    node['alternateName'] = person['alternateNames']
                    node['url'] = portfolio_url + '/'
                    node['description'] = person['description']
                    node['jobTitle'] = 'Founder'
                    node['sameAs'] = same_as
                    node['worksFor'] = {'@type': 'Organization', '@id': brand_url + '/#organization', 'name': brand['name'], 'url': brand_url + '/'}
                elif typ == 'Organization' and node.get('@id', '').endswith('/#organization'):
                    node['name'] = brand['name']
                    node['url'] = brand_url + '/'
                    node['description'] = brand['description']
                    node['founder'] = {'@id': portfolio_url + '/#person'}
                    node['contactPoint'] = {'@type':'ContactPoint','contactType':'project enquiries','telephone':phone.replace(' ', ''),'email':email,'url':wa_url,'availableLanguage':['English','Urdu']}
            return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'
        source = re.sub(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', update_jsonld, source, count=1, flags=re.I|re.S)
    page.write_text(source, encoding='utf-8')

# Refresh the sitemap from canonical, indexable HTML pages.
exclude = {'404.html', 'thank-you.html', 'index.html'}
urls = set()
for page in ROOT.glob('*.html'):
    if page.name in exclude: continue
    source = page.read_text(encoding='utf-8', errors='replace')
    if re.search(r'<meta\s+name=["\']robots["\']\s+content=["\'][^"\']*noindex', source, re.I): continue
    canonical_url = None
    for tag in re.findall(r'<link\b[^>]*>', source, re.I):
        rel_match = re.search(r'\brel=["\']([^"\']+)', tag, re.I)
        href_match = re.search(r'\bhref=["\']([^"\']+)', tag, re.I)
        if rel_match and 'canonical' in rel_match.group(1).lower().split() and href_match:
            canonical_url = href_match.group(1)
            break
    urls.add(canonical_url or (portfolio_url + '/' + page.name))
urls.add(portfolio_url + '/')
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
image_urls = [
    (portfolio_url + '/assets/images/gallery/muhammad-bakhtawar-khan-mbk-global-founder-office-portrait.png', 'Muhammad Bakhtawar Khan (MBK) at the MBK Global office desk'),
    (portfolio_url + '/assets/images/gallery/muhammad-bakhtawar-khan-mbk-professional-navy-portrait.webp', 'Portrait of Muhammad Bakhtawar Khan wearing navy clothing in a lounge chair'),
    (portfolio_url + '/assets/images/gallery/muhammad-bakhtawar-khan-mbk-white-outfit-full-length-portrait.png', 'Full-length portrait of Muhammad Bakhtawar Khan in a white traditional outfit'),
    (portfolio_url + '/assets/images/gallery/muhammad-bakhtawar-khan-mbk-founder-profile-navy-seated.jpg', 'Muhammad Bakhtawar Khan seated in a navy outfit for a professional portrait'),
]
for url in sorted(urls):
    xml += '  <url><loc>' + html.escape(url) + '</loc>'
    if url.rstrip('/') == portfolio_url:
        for image_url, caption in image_urls:
            xml += '<image:image><image:loc>' + html.escape(image_url) + '</image:loc><image:caption>' + html.escape(caption) + '</image:caption></image:image>'
    xml += '</url>\n'
xml += '</urlset>\n'
(ROOT / 'sitemap.xml').write_text(xml, encoding='utf-8')

# Keep the sitemap declaration aligned with the configured portfolio URL.
robots_path = ROOT / 'robots.txt'
robots = robots_path.read_text(encoding='utf-8')
robots = re.sub(r'(?im)^Sitemap:\s*\S+', 'Sitemap: ' + portfolio_url + '/sitemap.xml', robots)
robots_path.write_text(robots, encoding='utf-8')

print(f'Synchronized contact data and primary entity JSON-LD. Rebuilt sitemap with {len(urls)} URLs.')
