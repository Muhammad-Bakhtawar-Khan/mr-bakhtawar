#!/usr/bin/env python3
"""Validate MBK identity configuration against this static portfolio source tree."""
from pathlib import Path
import json, re, sys, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
config = json.loads((ROOT / 'identity-config.json').read_text(encoding='utf-8'))
errors, warnings = [], []
person, brand = config['person'], config['brand']
if not person.get('name') or not brand.get('name'):
    errors.append('Person and brand names must be set in identity-config.json.')
if not person.get('whatsappUrl', '').startswith('https://wa.me/'):
    errors.append('WhatsApp URL must use https://wa.me/.')
if not person.get('email') or '@' not in person['email']:
    errors.append('A valid public email is required.')

# All page JSON-LD blocks must be valid JSON.
for page in ROOT.glob('*.html'):
    source = page.read_text(encoding='utf-8', errors='replace')
    for block in re.findall(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', source, re.I | re.S):
        try:
            json.loads(block)
        except Exception as exc:
            errors.append(f'{page.name}: invalid JSON-LD: {exc}')
    if 'wa.me/' in source and person['whatsappUrl'] not in source:
        warnings.append(f'{page.name}: contains a WhatsApp URL different from configured primary URL.')

try:
    sitemap = ET.parse(ROOT / 'sitemap.xml').getroot()
    urls = [el.text for el in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    if len(urls) != len(set(urls)):
        errors.append('Sitemap contains duplicate URLs.')
    for url in urls:
        if not url.startswith(person['url']):
            errors.append(f'Sitemap URL is outside the personal portfolio canonical domain: {url}')
except Exception as exc:
    errors.append(f'Invalid sitemap.xml: {exc}')

robots = (ROOT / 'robots.txt').read_text(encoding='utf-8')
if not re.search(r'User-agent:\s*OAI-SearchBot\s+Allow:\s*/', robots, re.I):
    warnings.append('OAI-SearchBot is not explicitly allowed in robots.txt.')
if not re.search(r'User-agent:\s*GPTBot\s+Disallow:\s*/', robots, re.I):
    warnings.append('GPTBot training access is not explicitly disallowed; confirm owner policy.')

for required in ['about-muhammad-bakhtawar-khan.html', 'official-links.html', 'web-development.html', 'ai-api-integration.html', 'technical-seo.html', 'cybersecurity.html', 'digital-branding.html']:
    if not (ROOT / required).exists():
        errors.append(f'Missing required page: {required}')

print(f'Checked {len(list(ROOT.glob("*.html")))} HTML pages.')
print(f'Sitemap URLs: {len(urls) if "urls" in locals() else 0}.')
for warning in warnings:
    print('WARNING:', warning)
for error in errors:
    print('ERROR:', error)
if errors:
    sys.exit(1)
print('Identity configuration validation passed.')
