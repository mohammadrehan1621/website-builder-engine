import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

sites = [
    ('Raadha Rani', 'https://raadha-rani-patna.pages.dev'),
    ('Ali Mobile', 'https://ali-mobile-patna.pages.dev')
]

for name, base_url in sites:
    print(f"\n==========================================")
    print(f"=== VERIFYING {name.upper()} ({base_url}) ===")
    print(f"==========================================")
    req = urllib.request.Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    js_matches = re.findall(r'src="(/assets/[^"]+\.js)"', html)
    css_matches = re.findall(r'href="(/assets/[^"]+\.css)"', html)
    
    # 1. Verify Public HTML has NO visible Store Admin button
    has_public_admin_btn = 'Store Admin' in html or 'Bhaiya Store Admin' in html
    print('  Public HTML is 100% CLEAN of Admin buttons:', not has_public_admin_btn)

    if css_matches:
        css_url = base_url + css_matches[0]
        css = urllib.request.urlopen(urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
        print('  CSS URL:', css_url)
        print('  hardware-120fps class in CSS:', 'hardware-120fps' in css)
        print('  No heavy filter: blur(60px) in CSS:', 'blur(60px)' not in css and 'blur(50px)' not in css)
        if name == 'Raadha Rani':
            print('  Lively Background Sparkles in CSS:', 'animate-float-sparkle' in css)
            print('  Lively Aurora Drift in CSS:', 'animate-aurora-drift-1' in css)

    if js_matches:
        js_url = base_url + js_matches[0]
        js = urllib.request.urlopen(urllib.request.Request(js_url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
        print('  JS URL:', js_url)
        print('  30 Verified Customer Reviews & Videos in JS:', '30 Verified Customer Reviews' in js)
        print('  15 Google Maps Reviews in JS:', '15 Google Maps Reviews' in js)
        print('  15 Social Videos in JS:', '15 Social Videos' in js)
        print('  hardware-120fps in JS:', 'hardware-120fps' in js)
        
        if name == 'Raadha Rani':
            print('  Floor Numbers Removed in JS (Floor 1/2/3):', 'Floor 1' not in js and 'Floor 2' not in js and 'Floor 3' not in js and 'Ground Floor' not in js)
            print('  Rupee Prices Removed in JS (\u20b925,000 / \u20b91,25,000 / \u20b918,500):', '\u20b925,000' not in js and '\u20b91,25,000' not in js and '\u20b918,500' not in js)
            print('  Bridal Trousseau Curator in JS:', 'Curate Your Bridal Trousseau' in js or 'Trousseau' in js)
            print('  Lively Background Component in JS:', 'animate-float-sparkle' in js or 'LivelyBackground' in js or 'animate-aurora' in js)
            print('  Laptop Hardware Binding System in JS:', 'radha_patna_laptop_2026' in js)
            print('  Mobile/Tablet Lockout Guard in JS:', 'Store Laptop Required' in js)
            print('  1-Click WhatsApp Pairing Query in JS:', 'pair_laptop' in js)
        
        if name == 'Ali Mobile':
            print('  Laptop Hardware Binding System in JS:', 'ali_patna_laptop_2026' in js)
            print('  Mobile/Tablet Lockout Guard in JS:', 'Store Laptop Required' in js)
            print('  1-Click WhatsApp Pairing Query in JS:', 'pair_laptop' in js)
            print('  Satyanarayan Market in JS:', 'Satyanarayan' in js)
