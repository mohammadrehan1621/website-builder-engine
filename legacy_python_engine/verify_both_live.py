import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("--- VERIFYING RAADHA RANI LIVE DEPLOYMENT ---")
url1 = 'https://raadha-rani-patna.pages.dev/'
req1 = urllib.request.Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
html1 = urllib.request.urlopen(req1).read().decode('utf-8')
matches_js = re.findall(r'src="(/assets/[^"]+\.js)"', html1)
matches_css = re.findall(r'href="(/assets/[^"]+\.css)"', html1)
print('Raadha Rani JS bundles:', matches_js)
print('Raadha Rani CSS bundles:', matches_css)

if matches_css:
    css_url = 'https://raadha-rani-patna.pages.dev' + matches_css[0]
    css_text = urllib.request.urlopen(urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
    print('CSS Size:', len(css_text), 'bytes')
    print('runway-spotlight-left in CSS:', 'runway-spotlight-left' in css_text)
    print('spotlightSway in CSS:', 'spotlightSway' in css_text)
    print('floating-sparkle in CSS:', 'floating-sparkle' in css_text)
    print('sparkleDrift in CSS:', 'sparkleDrift' in css_text)

if matches_js:
    js_url1 = 'https://raadha-rani-patna.pages.dev' + matches_js[0]
    js_text1 = urllib.request.urlopen(urllib.request.Request(js_url1, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
    print('JS Size:', len(js_text1), 'bytes')
    print('Background picture in Hero:', 'Luxury Bridal Catwalk Ambience' in js_text1)
    print('Live stage spotlight present:', 'runway-spotlight-left' in js_text1)
    print('Floating sparkles present:', 'floating-sparkle sparkle-1' in js_text1)
    print('LIVE ON STAGE badge present:', 'LIVE ON STAGE' in js_text1)
