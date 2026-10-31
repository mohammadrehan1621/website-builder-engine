import re
import os

target_files = [
    r"C:\Users\rehan\Desktop\Rehan_Quant_Lab\Website_RehanQuantLab\index.html",
    r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev\index.html"
]

new_desc = '<meta name="description" content="Founder & Principal Systems Architect at Rehan Quant Lab. Developer of ExpressBill POS, RQL Aegis, and 17 Offline-First Sovereign Desktop Business Applications with zero monthly fees." />'
new_og_desc = '<meta property="og:description" content="Founder & Principal Systems Architect at Rehan Quant Lab. Developer of ExpressBill POS, RQL Aegis, and 17 Offline-First Sovereign Desktop Business Applications with zero monthly fees." />'
new_tw_desc = '<meta name="twitter:description" content="Founder & Principal Systems Architect at Rehan Quant Lab. Developer of ExpressBill POS, RQL Aegis, and 17 Offline-First Sovereign Desktop Business Applications with zero monthly fees." />'

new_schema = '''<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Mohammad Rehan",
    "jobTitle": "Founder & Principal Systems Architect",
    "description": "Founder & Principal Systems Architect at Rehan Quant Lab™. Specializing in offline-first desktop business software, ultra-low-latency in-memory databases (AegisDB™), and high-availability distributed systems.",
    "url": "https://rehanquantlab.com",
    "image": "https://rehanquantlab.com/og_preview.png",
    "worksFor": {
      "@type": "Organization",
      "name": "Rehan Quant Lab",
      "url": "https://rehanquantlab.com",
      "logo": "https://rehanquantlab.com/og_preview.png",
      "sameAs": [
        "https://github.com/rehanquantlab",
        "https://www.linkedin.com/company/rehanquantlab",
        "https://x.com/rehanquantlab",
        "https://rehanquantlab.substack.com"
      ]
    },
    "sameAs": [
      "https://github.com/rehanquantlab",
      "https://github.com/mohammadrehan1621",
      "https://www.linkedin.com/in/mohammad-rehan-tech/",
      "https://x.com/rehanquantlab",
      "https://rehanquantlab.substack.com",
      "https://wa.me/917091518548"
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "ExpressBill POS™ — Offline-First Retail Billing & ERP",
    "operatingSystem": "Windows 10, Windows 11 (64-bit)",
    "applicationCategory": "BusinessApplication",
    "applicationSubCategory": "Point of Sale (POS) & Retail Inventory",
    "softwareVersion": "2.0.0-PROD",
    "description": "Enterprise offline-first retail Point of Sale (POS) and inventory management desktop software. Features sub-second barcode checkout, ESC/POS thermal receipt printing, GST calculation, and zero monthly subscription fees.",
    "offers": {
      "@type": "Offer",
      "price": "49.00",
      "priceCurrency": "USD",
      "priceValidUntil": "2030-12-31",
      "availability": "https://schema.org/InStock",
      "url": "https://rehanquantlab.com"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "ratingCount": "28"
    },
    "author": {
      "@type": "Person",
      "name": "Mohammad Rehan"
    }
  },
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "RQL Retail Suite™ — Complete Offline Retail Master Bundle",
    "operatingSystem": "Windows 10, Windows 11 (64-bit)",
    "applicationCategory": "BusinessApplication",
    "softwareVersion": "2.0.0-PROD",
    "description": "Complete 7-application sovereign desktop workstation suite for retail stores: POS billing, thermal barcode printing, multi-counter LAN mesh, inventory variance audit, and khata customer credit management.",
    "offers": {
      "@type": "Offer",
      "price": "129.00",
      "priceCurrency": "USD",
      "priceValidUntil": "2030-12-31",
      "availability": "https://schema.org/InStock",
      "url": "https://rehanquantlab.com"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "5.0",
      "ratingCount": "19"
    },
    "author": {
      "@type": "Organization",
      "name": "Rehan Quant Lab"
    }
  }
]
</script>'''

for fpath in target_files:
    if not os.path.exists(fpath):
        print(f"Skipping {fpath} (not found)")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Meta desc
    content = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']\s*/?>', new_desc, content, count=1)
    # OG desc
    content = re.sub(r'<meta\s+property=["\']og:description["\']\s+content=["\'].*?["\']\s*/?>', new_og_desc, content, count=1)
    # Twitter desc
    content = re.sub(r'<meta\s+name=["\']twitter:description["\']\s+content=["\'].*?["\']\s*/?>', new_tw_desc, content, count=1)
    # Schema.org
    content = re.sub(r'<script\s+type=["\']application/ld\+json["\']>.*?</script>', new_schema, content, count=1, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated SEO & Rich Snippets in: {fpath}")

print("Sync completed successfully.")
