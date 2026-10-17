"""
Generator for the fresh, modern, boutique Ladies Zone Exclusive Showroom website.
"""

import os
import json
import base64
from pathlib import Path

PROJECT_DIR = Path(r"C:\Users\rehan\Desktop\website_builder\projects\ladies_zone")
PROJECT_DIR.mkdir(parents=True, exist_ok=True)
ASSETS_DIR = PROJECT_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# Read starter products
from catalog_data import STARTER_PRODUCTS, logo_b64, catalog_json_str

INDEX_HTML_CONTENT = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover" />
  <title>Ladies Zone Exclusive Showroom | Boring Road, Patna — Women's Footwear, Suits & Western Wear</title>
  <meta name="description" content="Ladies Zone Exclusive Showroom in Boring Road, S.K. Puri, Patna. Premium looks at smart prices. Explore heels, bridal footwear, mojari & jutti, designer suits, and western dresses. In-store trials and WhatsApp enquiries." />
  <meta name="keywords" content="Ladies Zone Patna, Boring Road showroom, women footwear Patna, bridal shoes Patna, jutti Patna, suits Boring Road, western dresses Patna" />
  
  <!-- Canonical & Social Metadata -->
  <link rel="canonical" href="https://ladieszonepatna.in/" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Ladies Zone Exclusive Showroom" />
  <meta property="og:title" content="Ladies Zone Exclusive Showroom — Boring Road, Patna" />
  <meta property="og:description" content="Where Fashion Meets Comfort. Premium looks at smart prices. Footwear, Bridal, Mojari, Suits & Western Wear." />
  <meta property="og:url" content="https://ladieszonepatna.in/" />
  <meta property="og:image" content="https://ladieszonepatna.in/assets/logo.png" />
  <meta name="theme-color" content="#421021" />

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />

  <!-- Schema.org Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ClothingStore",
    "name": "Ladies Zone Exclusive Showroom",
    "image": "https://ladieszonepatna.in/assets/logo.png",
    "description": "Exclusive boutique showroom in Boring Road, Patna offering women's footwear, bridal shoes, jutti, ethnic suits, and western wear.",
    "telephone": ["+91-7091518548", "+91-8986047584"],
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Boring Road, S.K. Puri",
      "addressLocality": "Patna",
      "addressRegion": "Bihar",
      "postalCode": "800001",
      "addressCountry": "IN"
    }},
    "openingHoursSpecification": [
      {{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        "opens": "10:30",
        "closes": "21:00"
      }}
    ],
    "priceRange": "₹₹",
    "url": "https://ladieszonepatna.in/"
  }}
  </script>

  <style>
    :root {{
      --bg-cream: #faf7f5;
      --bg-white: #ffffff;
      --rose-primary: #be4b63;
      --rose-dark: #8c2e42;
      --rose-light: #fbebee;
      --plum: #380d1b;
      --gold: #bfa15f;
      --gold-light: #fef9ed;
      --text-dark: #1f1f23;
      --text-muted: #6e6e7c;
      --border-color: #ede5e1;
      --whatsapp-green: #25d366;
      --whatsapp-dark: #128c7e;
      --danger-red: #d32f2f;
      --shadow-sm: 0 2px 8px rgba(0,0,0,0.04);
      --shadow-md: 0 8px 24px rgba(56, 13, 27, 0.08);
      --shadow-lg: 0 16px 40px rgba(56, 13, 27, 0.12);
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 22px;
      --radius-pill: 9999px;
      --font-display: 'Playfair Display', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-cream);
      color: var(--text-dark);
      line-height: 1.6;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }}

    a {{
      color: inherit;
      text-decoration: none;
    }}

    button {{
      font-family: inherit;
      cursor: pointer;
      border: none;
      outline: none;
    }}

    /* Top Announcement Bar */
    .top-bar {{
      background: linear-gradient(90deg, #380d1b, #5f182f);
      color: #f7e6eb;
      font-size: 0.82rem;
      padding: 8px 20px;
      text-align: center;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
      z-index: 100;
    }}

    .top-bar-center {{
      flex: 1;
      font-weight: 500;
      letter-spacing: 0.3px;
    }}

    .top-bar-contact {{
      display: flex;
      gap: 15px;
      font-size: 0.8rem;
    }}

    .top-bar-contact a {{
      color: #ffd6e0;
      display: flex;
      align-items: center;
      gap: 4px;
      transition: color 0.2s;
    }}

    .top-bar-contact a:hover {{
      color: #ffffff;
    }}

    /* Admin Banner Bar */
    #adminBanner {{
      display: none;
      background: #1e1e24;
      color: #fff;
      padding: 10px 24px;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2px solid var(--gold);
      font-size: 0.88rem;
      position: sticky;
      top: 0;
      z-index: 1000;
    }}

    .admin-badge-tag {{
      background: var(--gold);
      color: #1e1e24;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: var(--radius-pill);
      font-size: 0.75rem;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    .admin-actions {{
      display: flex;
      gap: 10px;
      align-items: center;
    }}

    .btn-admin-action {{
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      font-size: 0.82rem;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .btn-admin-add {{
      background: var(--rose-primary);
      color: #fff;
    }}
    .btn-admin-add:hover {{
      background: var(--rose-dark);
    }}

    .btn-admin-backup {{
      background: #33333f;
      color: #e0e0e8;
    }}
    .btn-admin-backup:hover {{
      background: #444455;
    }}

    .btn-admin-logout {{
      background: transparent;
      color: #ff99aa;
      border: 1px solid #663344;
    }}
    .btn-admin-logout:hover {{
      background: #441a24;
    }}

    /* Main Navigation Header */
    .site-header {{
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 900;
      box-shadow: var(--shadow-sm);
    }}

    .header-container {{
      max-width: 1320px;
      margin: 0 auto;
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }}

    .brand-logo-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .brand-logo-img {{
      height: 48px;
      width: auto;
      object-fit: contain;
    }}

    .brand-text-block {{
      display: flex;
      flex-direction: column;
    }}

    .brand-name {{
      font-family: var(--font-display);
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--plum);
      letter-spacing: -0.3px;
      line-height: 1.1;
    }}

    .brand-tagline {{
      font-size: 0.72rem;
      color: var(--rose-primary);
      font-weight: 600;
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }}

    .nav-links {{
      display: flex;
      gap: 24px;
      align-items: center;
    }}

    .nav-link {{
      font-size: 0.92rem;
      font-weight: 600;
      color: var(--text-dark);
      padding: 6px 2px;
      position: relative;
      transition: color 0.2s;
    }}

    .nav-link:hover, .nav-link.active {{
      color: var(--rose-primary);
    }}

    .nav-link::after {{
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 0;
      height: 2px;
      background: var(--rose-primary);
      transition: width 0.25s ease;
    }}

    .nav-link:hover::after, .nav-link.active::after {{
      width: 100%;
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .btn-staff-login {{
      background: var(--rose-light);
      color: var(--rose-dark);
      font-size: 0.84rem;
      font-weight: 700;
      padding: 8px 18px;
      border-radius: var(--radius-pill);
      border: 1px solid #f2cfd7;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .btn-staff-login:hover {{
      background: var(--rose-primary);
      color: #fff;
    }}

    .btn-visit-badge {{
      background: var(--plum);
      color: #fff;
      font-size: 0.84rem;
      font-weight: 600;
      padding: 8px 18px;
      border-radius: var(--radius-pill);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .btn-visit-badge:hover {{
      background: var(--rose-dark);
      transform: translateY(-1px);
    }}

    /* Hero Section */
    .hero-section {{
      position: relative;
      background: linear-gradient(135deg, #fff5f7 0%, #fef3e9 50%, #f7edf2 100%);
      padding: 70px 24px 80px;
      overflow: hidden;
      border-bottom: 1px solid var(--border-color);
    }}

    .hero-container {{
      max-width: 1320px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      align-items: center;
      gap: 60px;
    }}

    .hero-content {{
      z-index: 2;
    }}

    .hero-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(190, 75, 99, 0.1);
      color: var(--rose-primary);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 6px 16px;
      border-radius: var(--radius-pill);
      margin-bottom: 20px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    .hero-title {{
      font-family: var(--font-display);
      font-size: 3.4rem;
      line-height: 1.15;
      font-weight: 700;
      color: var(--plum);
      margin-bottom: 20px;
      letter-spacing: -0.5px;
    }}

    .hero-title span {{
      color: var(--rose-primary);
      font-style: italic;
    }}

    .hero-subtitle {{
      font-size: 1.12rem;
      color: var(--text-muted);
      margin-bottom: 34px;
      max-width: 540px;
      line-height: 1.65;
    }}

    .hero-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 40px;
    }}

    .btn-hero-primary {{
      background: linear-gradient(135deg, var(--rose-primary), var(--rose-dark));
      color: #fff;
      font-size: 1rem;
      font-weight: 700;
      padding: 14px 32px;
      border-radius: var(--radius-pill);
      box-shadow: 0 8px 22px rgba(190, 75, 99, 0.35);
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}

    .btn-hero-primary:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 28px rgba(190, 75, 99, 0.45);
    }}

    .btn-hero-secondary {{
      background: #fff;
      color: var(--plum);
      border: 1px solid #dfd3d7;
      font-size: 1rem;
      font-weight: 700;
      padding: 14px 28px;
      border-radius: var(--radius-pill);
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}

    .btn-hero-secondary:hover {{
      background: #fbf5f7;
      border-color: var(--rose-primary);
      color: var(--rose-primary);
    }}

    .hero-stats {{
      display: flex;
      gap: 36px;
      border-top: 1px solid rgba(0,0,0,0.06);
      padding-top: 24px;
    }}

    .stat-item {{
      display: flex;
      flex-direction: column;
    }}

    .stat-number {{
      font-family: var(--font-display);
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--plum);
    }}

    .stat-label {{
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 500;
    }}

    .hero-media-wrap {{
      position: relative;
    }}

    .hero-card-main {{
      position: relative;
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      border: 4px solid #fff;
    }}

    .hero-card-main img {{
      width: 100%;
      height: 480px;
      object-fit: cover;
      display: block;
      transition: transform 0.6s ease;
    }}

    .hero-card-main:hover img {{
      transform: scale(1.03);
    }}

    .hero-floating-badge {{
      position: absolute;
      bottom: 24px;
      left: 24px;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(10px);
      border-radius: var(--radius-md);
      padding: 14px 20px;
      box-shadow: var(--shadow-md);
      display: flex;
      align-items: center;
      gap: 14px;
      max-width: 280px;
    }}

    .badge-icon-circle {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--rose-light);
      color: var(--rose-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      flex-shrink: 0;
    }}

    .badge-title {{
      font-weight: 700;
      font-size: 0.92rem;
      color: var(--plum);
      line-height: 1.2;
    }}

    .badge-sub {{
      font-size: 0.76rem;
      color: var(--text-muted);
    }}

    /* Categories Grid */
    .section-wrap {{
      max-width: 1320px;
      margin: 0 auto;
      padding: 70px 24px;
    }}

    .section-header {{
      text-align: center;
      max-width: 680px;
      margin: 0 auto 46px;
    }}

    .section-tag {{
      display: inline-block;
      color: var(--rose-primary);
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.2px;
      margin-bottom: 8px;
    }}

    .section-title {{
      font-family: var(--font-display);
      font-size: 2.3rem;
      color: var(--plum);
      font-weight: 700;
      line-height: 1.2;
      margin-bottom: 12px;
    }}

    .section-desc {{
      color: var(--text-muted);
      font-size: 1rem;
    }}

    .category-cards-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 20px;
      margin-bottom: 20px;
    }}

    .cat-card {{
      background: #fff;
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
      transition: all 0.3s ease;
      cursor: pointer;
      display: flex;
      flex-direction: column;
    }}

    .cat-card:hover {{
      transform: translateY(-6px);
      box-shadow: var(--shadow-md);
      border-color: var(--rose-primary);
    }}

    .cat-card-img {{
      width: 100%;
      height: 180px;
      object-fit: cover;
      display: block;
    }}

    .cat-card-body {{
      padding: 16px;
      text-align: center;
    }}

    .cat-card-title {{
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--plum);
      margin-bottom: 4px;
    }}

    .cat-card-subtitle {{
      font-size: 0.78rem;
      color: var(--rose-primary);
      font-weight: 600;
    }}

    /* Main Lookbook & Catalog Section */
    .catalog-wrapper {{
      background: #ffffff;
      border-radius: var(--radius-lg);
      padding: 36px 30px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}

    .catalog-toolbar {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
      margin-bottom: 32px;
      padding-bottom: 24px;
      border-bottom: 1px solid var(--border-color);
    }}

    .filter-tabs {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .tab-pill {{
      background: var(--bg-cream);
      color: var(--text-dark);
      font-size: 0.86rem;
      font-weight: 600;
      padding: 8px 18px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--border-color);
      transition: all 0.2s;
    }}

    .tab-pill:hover {{
      border-color: var(--rose-primary);
      color: var(--rose-primary);
    }}

    .tab-pill.active {{
      background: var(--rose-primary);
      color: #fff;
      border-color: var(--rose-primary);
      box-shadow: 0 4px 12px rgba(190, 75, 99, 0.25);
    }}

    .filter-search-box {{
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 280px;
    }}

    .search-input {{
      flex: 1;
      padding: 10px 16px;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-pill);
      font-size: 0.88rem;
      font-family: inherit;
      background: #fbf9f8;
      transition: all 0.2s;
    }}

    .search-input:focus {{
      outline: none;
      border-color: var(--rose-primary);
      background: #fff;
      box-shadow: 0 0 0 3px rgba(190, 75, 99, 0.12);
    }}

    .sort-select {{
      padding: 10px 16px;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-pill);
      font-size: 0.86rem;
      font-family: inherit;
      background: #fbf9f8;
      color: var(--text-dark);
      cursor: pointer;
    }}

    /* Product Grid */
    .products-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 28px;
    }}

    .product-card {{
      background: #fff;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      position: relative;
      transition: all 0.3s ease;
    }}

    .product-card:hover {{
      transform: translateY(-5px);
      box-shadow: var(--shadow-md);
      border-color: #eedde2;
    }}

    .card-media-wrap {{
      position: relative;
      width: 100%;
      height: 320px;
      background: #f7f4f2;
      overflow: hidden;
    }}

    .card-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.5s ease;
    }}

    .product-card:hover .card-img {{
      transform: scale(1.05);
    }}

    .card-tag-badge {{
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(56, 13, 27, 0.88);
      color: #fff;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      letter-spacing: 0.4px;
      text-transform: uppercase;
      backdrop-filter: blur(4px);
    }}

    .card-trial-badge {{
      position: absolute;
      top: 12px;
      right: 12px;
      background: rgba(255, 255, 255, 0.94);
      color: var(--rose-primary);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .card-quick-view {{
      position: absolute;
      bottom: 12px;
      left: 50%;
      transform: translateX(-50%) translateY(20px);
      background: rgba(255, 255, 255, 0.95);
      color: var(--text-dark);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 6px 16px;
      border-radius: var(--radius-pill);
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      opacity: 0;
      transition: all 0.25s ease;
      cursor: pointer;
    }}

    .product-card:hover .card-quick-view {{
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }}

    .card-body {{
      padding: 18px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }}

    .card-cat-label {{
      font-size: 0.76rem;
      color: var(--rose-primary);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      margin-bottom: 4px;
    }}

    .card-title {{
      font-family: var(--font-display);
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--plum);
      line-height: 1.3;
      margin-bottom: 8px;
    }}

    .card-price-row {{
      display: flex;
      align-items: baseline;
      gap: 10px;
      margin-bottom: 12px;
    }}

    .card-price-current {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--plum);
    }}

    .card-price-mrp {{
      font-size: 0.88rem;
      color: #999;
      text-decoration: line-through;
    }}

    .card-discount-tag {{
      font-size: 0.74rem;
      color: #2e7d32;
      font-weight: 700;
      background: #e8f5e9;
      padding: 2px 6px;
      border-radius: 4px;
    }}

    .card-sizes-row {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
      margin-bottom: 16px;
    }}

    .size-label {{
      font-size: 0.74rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .size-chip {{
      font-size: 0.72rem;
      font-weight: 600;
      background: #f5f0ed;
      color: var(--text-dark);
      padding: 2px 7px;
      border-radius: 4px;
    }}

    .card-actions {{
      margin-top: auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .btn-card-whatsapp {{
      background: var(--whatsapp-green);
      color: #fff;
      font-size: 0.88rem;
      font-weight: 700;
      padding: 10px 16px;
      border-radius: var(--radius-pill);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s;
      box-shadow: 0 4px 10px rgba(37, 211, 102, 0.2);
    }}

    .btn-card-whatsapp:hover {{
      background: var(--whatsapp-dark);
      transform: translateY(-1px);
    }}

    /* Card Admin Toolbar */
    .card-admin-row {{
      display: none;
      gap: 6px;
      margin-top: 6px;
      padding-top: 8px;
      border-top: 1px dashed #ffd1dc;
    }}

    .btn-card-delete {{
      flex: 1;
      background: #ffebee;
      color: var(--danger-red);
      font-size: 0.76rem;
      font-weight: 700;
      padding: 6px 10px;
      border-radius: 6px;
      border: 1px solid #ffcdd2;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      transition: all 0.15s;
    }}

    .btn-card-delete:hover {{
      background: var(--danger-red);
      color: #fff;
    }}

    .btn-card-edit {{
      flex: 1;
      background: #e3f2fd;
      color: #1565c0;
      font-size: 0.76rem;
      font-weight: 700;
      padding: 6px 10px;
      border-radius: 6px;
      border: 1px solid #bbdefb;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      transition: all 0.15s;
    }}

    .btn-card-edit:hover {{
      background: #1565c0;
      color: #fff;
    }}

    /* Feature Highlight Banners */
    .highlights-section {{
      background: linear-gradient(180deg, #faf7f5 0%, #f4ede9 100%);
      padding: 80px 24px;
      border-top: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }}

    .highlight-grid {{
      max-width: 1320px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 32px;
    }}

    .highlight-card {{
      background: #fff;
      border-radius: var(--radius-lg);
      padding: 40px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      position: relative;
      overflow: hidden;
    }}

    .highlight-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 6px;
      height: 100%;
      background: var(--rose-primary);
    }}

    .highlight-card-title {{
      font-family: var(--font-display);
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--plum);
      margin-bottom: 14px;
    }}

    .highlight-card-desc {{
      color: var(--text-muted);
      font-size: 0.98rem;
      margin-bottom: 24px;
      line-height: 1.6;
    }}

    /* Showroom Location & Timing Section */
    .showroom-section {{
      background: #ffffff;
      padding: 80px 24px;
      border-bottom: 1px solid var(--border-color);
    }}

    .showroom-container {{
      max-width: 1320px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 50px;
      align-items: center;
    }}

    .showroom-info-box {{
      display: flex;
      flex-direction: column;
    }}

    .info-list {{
      display: flex;
      flex-direction: column;
      gap: 20px;
      margin: 28px 0 34px;
    }}

    .info-item {{
      display: flex;
      align-items: flex-start;
      gap: 16px;
    }}

    .info-icon {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--rose-light);
      color: var(--rose-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      flex-shrink: 0;
    }}

    .info-text-title {{
      font-weight: 700;
      font-size: 0.98rem;
      color: var(--plum);
      margin-bottom: 2px;
    }}

    .info-text-sub {{
      font-size: 0.9rem;
      color: var(--text-muted);
    }}

    .showroom-map-wrap {{
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-md);
      border: 3px solid #fff;
      height: 380px;
      background: #eee;
    }}

    .showroom-map-wrap iframe {{
      width: 100%;
      height: 100%;
      border: 0;
    }}

    /* Reviews Section */
    .reviews-section {{
      padding: 80px 24px;
      background: var(--bg-cream);
    }}

    .reviews-grid {{
      max-width: 1320px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 26px;
    }}

    .review-card {{
      background: #fff;
      border-radius: var(--radius-md);
      padding: 30px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .review-stars {{
      color: #f59e0b;
      margin-bottom: 14px;
      font-size: 1.1rem;
    }}

    .review-text {{
      font-size: 0.94rem;
      color: var(--text-dark);
      font-style: italic;
      margin-bottom: 20px;
      line-height: 1.6;
    }}

    .review-author {{
      font-weight: 700;
      font-size: 0.9rem;
      color: var(--plum);
    }}

    .review-loc {{
      font-size: 0.78rem;
      color: var(--text-muted);
    }}

    /* Footer */
    .site-footer {{
      background: #240a12;
      color: #e5cbd3;
      padding: 60px 24px 30px;
      border-top: 3px solid var(--gold);
    }}

    .footer-container {{
      max-width: 1320px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr 1.2fr;
      gap: 40px;
      margin-bottom: 50px;
    }}

    .footer-brand-title {{
      font-family: var(--font-display);
      font-size: 1.4rem;
      color: #fff;
      margin-bottom: 12px;
      font-weight: 700;
    }}

    .footer-brand-desc {{
      font-size: 0.88rem;
      line-height: 1.6;
      color: #d1b5be;
      margin-bottom: 20px;
    }}

    .footer-col-title {{
      font-family: var(--font-display);
      font-size: 1.05rem;
      color: #fff;
      margin-bottom: 16px;
      font-weight: 600;
    }}

    .footer-links {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 0.88rem;
    }}

    .footer-links a:hover {{
      color: #ffd6e0;
      text-decoration: underline;
    }}

    .footer-bottom {{
      max-width: 1320px;
      margin: 0 auto;
      border-top: 1px solid rgba(255,255,255,0.1);
      padding-top: 24px;
      text-align: center;
      font-size: 0.82rem;
      color: #a88a94;
    }}

    /* Modals (Login, Quick View, Add Product) */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(5px);
      z-index: 2000;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .modal-box {{
      background: #fff;
      border-radius: var(--radius-lg);
      max-width: 540px;
      width: 100%;
      padding: 32px;
      box-shadow: var(--shadow-lg);
      position: relative;
      max-height: 90vh;
      overflow-y: auto;
    }}

    .modal-close-btn {{
      position: absolute;
      top: 18px;
      right: 18px;
      background: #f5eded;
      border-radius: 50%;
      width: 34px;
      height: 34px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      color: var(--text-dark);
      cursor: pointer;
    }}

    .modal-title {{
      font-family: var(--font-display);
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--plum);
      margin-bottom: 8px;
    }}

    .modal-desc {{
      font-size: 0.88rem;
      color: var(--text-muted);
      margin-bottom: 24px;
    }}

    .form-group {{
      margin-bottom: 18px;
    }}

    .form-label {{
      display: block;
      font-size: 0.84rem;
      font-weight: 700;
      color: var(--plum);
      margin-bottom: 6px;
    }}

    .form-control {{
      width: 100%;
      padding: 10px 14px;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.9rem;
    }}

    .form-control:focus {{
      outline: none;
      border-color: var(--rose-primary);
      box-shadow: 0 0 0 3px rgba(190, 75, 99, 0.12);
    }}

    .photo-dropzone {{
      border: 2px dashed #d5bfc6;
      border-radius: var(--radius-md);
      padding: 24px;
      text-align: center;
      background: #fdfafb;
      cursor: pointer;
      margin-bottom: 16px;
      transition: all 0.2s;
    }}

    .photo-dropzone:hover {{
      border-color: var(--rose-primary);
      background: #fff;
    }}

    .preview-img-box {{
      width: 100%;
      height: 200px;
      border-radius: var(--radius-sm);
      overflow: hidden;
      margin-top: 10px;
      display: none;
    }}

    .preview-img-box img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    /* Toast Notification */
    .toast-msg {{
      position: fixed;
      bottom: 28px;
      right: 28px;
      background: #1f1f24;
      color: #fff;
      padding: 12px 22px;
      border-radius: var(--radius-pill);
      box-shadow: var(--shadow-lg);
      font-size: 0.88rem;
      font-weight: 600;
      z-index: 3000;
      display: none;
      align-items: center;
      gap: 10px;
      border-left: 4px solid var(--rose-primary);
    }}

    /* Responsive Queries */
    @media (max-width: 1024px) {{
      .hero-container {{
        grid-template-columns: 1fr;
        text-align: center;
      }}
      .hero-content {{
        display: flex;
        flex-direction: column;
        align-items: center;
      }}
      .hero-stats {{
        justify-content: center;
      }}
      .category-cards-grid {{
        grid-template-columns: repeat(3, 1fr);
      }}
      .footer-container {{
        grid-template-columns: 1fr 1fr;
      }}
      .showroom-container {{
        grid-template-columns: 1fr;
      }}
      .highlight-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    @media (max-width: 768px) {{
      .top-bar-contact {{
        display: none;
      }}
      .nav-links {{
        display: none;
      }}
      .category-cards-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .reviews-grid {{
        grid-template-columns: 1fr;
      }}
      .footer-container {{
        grid-template-columns: 1fr;
      }}
      .hero-title {{
        font-size: 2.3rem;
      }}
      .catalog-toolbar {{
        flex-direction: column;
        align-items: stretch;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Announcement Bar -->
  <div class="top-bar">
    <div class="top-bar-center">
      ✨ <strong>Ladies Zone Exclusive Showroom</strong> • Boring Road, S.K. Puri, Patna • Open All 7 Days: 10:30 AM – 9:00 PM
    </div>
    <div class="top-bar-contact">
      <a href="tel:+917091518548">📞 +91 70915 18548</a>
      <a href="https://wa.me/918986047584" target="_blank" rel="noopener">💬 WhatsApp</a>
    </div>
  </div>

  <!-- Admin Sticky Control Bar (Visible when logged in) -->
  <div id="adminBanner">
    <div style="display: flex; align-items: center; gap: 10px;">
      <span class="admin-badge-tag">Staff Admin Mode</span>
      <span>Logged in as <strong>Showroom Manager</strong></span>
    </div>
    <div class="admin-actions">
      <button class="btn-admin-action btn-admin-add" onclick="openAddProductModal()">➕ Add New Product / Photo</button>
      <button class="btn-admin-action btn-admin-backup" onclick="exportCatalogBackup()">💾 Backup</button>
      <button class="btn-admin-action btn-admin-backup" onclick="resetDefaultCatalog()">🔄 Reset Default</button>
      <button class="btn-admin-action btn-admin-logout" onclick="adminLogout()">Logout</button>
    </div>
  </div>

  <!-- Main Navigation Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="#" class="brand-logo-wrap">
        <img src="assets/logo.png" alt="Ladies Zone Exclusive Showroom" class="brand-logo-img" onerror="this.style.display='none'" />
        <div class="brand-text-block">
          <div class="brand-name">Ladies Zone</div>
          <div class="brand-tagline">Exclusive Showroom • Patna</div>
        </div>
      </a>

      <nav class="nav-links">
        <a href="#catalog" class="nav-link" onclick="filterByCategory('all')">All Collection</a>
        <a href="#catalog" class="nav-link" onclick="filterByCategory('heels')">Heels & Sandals</a>
        <a href="#catalog" class="nav-link" onclick="filterByCategory('bridal')">Bridal Footwear</a>
        <a href="#catalog" class="nav-link" onclick="filterByCategory('mojari')">Mojari & Jutti</a>
        <a href="#catalog" class="nav-link" onclick="filterByCategory('suits')">Suits & Ethnic</a>
        <a href="#catalog" class="nav-link" onclick="filterByCategory('western')">Western Dresses</a>
        <a href="#showroom" class="nav-link">Visit Showroom</a>
      </nav>

      <div class="header-right">
        <button id="staffLoginBtn" class="btn-staff-login" onclick="openLoginModal()">
          🔒 Staff Login
        </button>
        <a href="#showroom" class="btn-visit-badge">
          📍 Boring Road
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-section">
    <div class="hero-container">
      <div class="hero-content">
        <div class="hero-pill">
          <span>👑 Exclusive Women's Boutique in Patna</span>
        </div>
        <h1 class="hero-title">
          Where Fashion Meets <span>Comfort.</span>
        </h1>
        <p class="hero-subtitle">
          Discover your style. Enjoy premium looks at smart prices — handcrafted bridal footwear, party-wear heels, authentic Punjabi juttis, designer salwar suits, and chic western dresses.
        </p>

        <div class="hero-actions">
          <a href="#catalog" class="btn-hero-primary">
            <span>Explore Collection</span>
            <span>↓</span>
          </a>
          <a href="#showroom" class="btn-hero-secondary">
            <span>Visit Showroom</span>
            <span>📍</span>
          </a>
        </div>

        <div class="hero-stats">
          <div class="stat-item">
            <span class="stat-number">500+</span>
            <span class="stat-label">Showroom Designs</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">Boring Rd</span>
            <span class="stat-label">Prime Location, Patna</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">100%</span>
            <span class="stat-label">In-Store Trial Ready</span>
          </div>
        </div>
      </div>

      <div class="hero-media-wrap">
        <div class="hero-card-main">
          <img src="https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=1000&q=80" alt="Ladies Zone Fashion Collection" />
        </div>
        <div class="hero-floating-badge">
          <div class="badge-icon-circle">🏬</div>
          <div>
            <div class="badge-title">Direct Showroom Trial</div>
            <div class="badge-sub">Try before you buy • S.K. Puri, Patna</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Shop By Category Cards -->
  <section class="section-wrap">
    <div class="section-header">
      <span class="section-tag">Curated Collections</span>
      <h2 class="section-title">Shop by Category</h2>
      <p class="section-desc">Handpicked styles tailored for weddings, festive occasions, parties, and everyday chic comfort.</p>
    </div>

    <div class="category-cards-grid">
      <!-- 1. Heels -->
      <div class="cat-card" onclick="filterByCategory('heels')">
        <img src="https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=600&q=80" alt="Heels & Sandals" class="cat-card-img" />
        <div class="cat-card-body">
          <div class="cat-card-title">Heels & Sandals</div>
          <div class="cat-card-subtitle">Stilettos, Kitten & Blocks</div>
        </div>
      </div>

      <!-- 2. Bridal -->
      <div class="cat-card" onclick="filterByCategory('bridal')">
        <img src="https://images.unsplash.com/photo-1535043934128-cf0b28d52f95?auto=format&fit=crop&w=600&q=80" alt="Bridal Footwear" class="cat-card-img" />
        <div class="cat-card-body">
          <div class="cat-card-title">Bridal Footwear</div>
          <div class="cat-card-subtitle">Zardozi, Nagra & Wedges</div>
        </div>
      </div>

      <!-- 3. Mojari -->
      <div class="cat-card" onclick="filterByCategory('mojari')">
        <img src="https://images.unsplash.com/photo-1608256246200-53e635b5b65f?auto=format&fit=crop&w=600&q=80" alt="Ethnic Mojari & Jutti" class="cat-card-img" />
        <div class="cat-card-body">
          <div class="cat-card-title">Mojari & Jutti</div>
          <div class="cat-card-subtitle">Velvet, Threadwork & Mirror</div>
        </div>
      </div>

      <!-- 4. Suits -->
      <div class="cat-card" onclick="filterByCategory('suits')">
        <img src="https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=600&q=80" alt="Suits & Ethnic Wear" class="cat-card-img" />
        <div class="cat-card-body">
          <div class="cat-card-title">Suits & Ethnic</div>
          <div class="cat-card-subtitle">Anarkalis, Sets & Banarasi</div>
        </div>
      </div>

      <!-- 5. Western -->
      <div class="cat-card" onclick="filterByCategory('western')">
        <img src="https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=600&q=80" alt="Western Dresses" class="cat-card-img" />
        <div class="cat-card-body">
          <div class="cat-card-title">Western Dresses</div>
          <div class="cat-card-subtitle">Party-wear, Satin & Floral</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Curated Lookbook / Catalog Section -->
  <section id="catalog" class="section-wrap" style="padding-top: 10px;">
    <div class="catalog-wrapper">
      <div class="catalog-toolbar">
        <div class="filter-tabs">
          <button class="tab-pill active" onclick="filterByCategory('all')">All Items</button>
          <button class="tab-pill" onclick="filterByCategory('heels')">👠 Heels & Sandals</button>
          <button class="tab-pill" onclick="filterByCategory('bridal')">👰 Bridal Footwear</button>
          <button class="tab-pill" onclick="filterByCategory('mojari')">✨ Mojari & Jutti</button>
          <button class="tab-pill" onclick="filterByCategory('suits')">👗 Suits & Ethnic</button>
          <button class="tab-pill" onclick="filterByCategory('western')">💃 Western Dresses</button>
        </div>

        <div class="filter-search-box">
          <input type="text" id="searchInput" class="search-input" placeholder="Search by name or style..." oninput="handleSearch()" />
          <select id="sortSelect" class="sort-select" onchange="handleSort()">
            <option value="featured">Featured</option>
            <option value="price-asc">Price: Low to High</option>
            <option value="price-desc">Price: High to Low</option>
          </select>
        </div>
      </div>

      <!-- Dynamic Product Grid -->
      <div id="productsGrid" class="products-grid">
        <!-- Rendered dynamically by JavaScript -->
      </div>
    </div>
  </section>

  <!-- Editorial Highlight Banners -->
  <section class="highlights-section">
    <div class="highlight-grid">
      <div class="highlight-card">
        <div>
          <span class="section-tag">Made for Your Special Moments</span>
          <h3 class="highlight-card-title">Regal Bridal & Wedding Footwear</h3>
          <p class="highlight-card-desc">
            Your wedding day demands uncompromised elegance and lasting comfort. Experience handcrafted zardozi heels, pearl mules, and dual-cushioned wedges engineered so you shine through every ceremony without shoe bites.
          </p>
        </div>
        <div>
          <button class="btn-hero-primary" onclick="filterByCategory('bridal')">Explore Bridal Collection</button>
        </div>
      </div>

      <div class="highlight-card">
        <div>
          <span class="section-tag">Elegance in Every Detail</span>
          <h3 class="highlight-card-title">Designer Ethnic Suits & Sets</h3>
          <p class="highlight-card-desc">
            From breezy pastel organza Anarkalis to rich festive Banarasi weaves and Chanderi sets. Curated with matching dupattas and tailored cuts ready for showroom trial.
          </p>
        </div>
        <div>
          <button class="btn-hero-primary" onclick="filterByCategory('suits')">Explore Suits & Sets</button>
        </div>
      </div>
    </div>
  </section>

  <!-- Showroom Visit & Directions Section -->
  <section id="showroom" class="showroom-section">
    <div class="showroom-container">
      <div class="showroom-info-box">
        <span class="section-tag">Visit Our Showroom</span>
        <h2 class="section-title">Experience the Collection in Person</h2>
        <p class="section-desc">
          Located in the heart of Boring Road, Patna. Visit us for personalized styling, size trials, and direct purchases.
        </p>

        <div class="info-list">
          <div class="info-item">
            <div class="info-icon">📍</div>
            <div>
              <div class="info-text-title">Showroom Address</div>
              <div class="info-text-sub">Ladies Zone Exclusive Showroom, Boring Road, S.K. Puri, Patna, Bihar — 800001</div>
            </div>
          </div>

          <div class="info-item">
            <div class="info-icon">⏰</div>
            <div>
              <div class="info-text-title">Showroom Hours</div>
              <div class="info-text-sub">Monday – Sunday: <strong>10:30 AM to 9:00 PM</strong> (Open All 7 Days)</div>
            </div>
          </div>

          <div class="info-item">
            <div class="info-icon">📞</div>
            <div>
              <div class="info-text-title">Customer Care & Enquiries</div>
              <div class="info-text-sub">
                Phone: <a href="tel:+917091518548" style="color:var(--rose-primary);font-weight:700;">+91 70915 18548</a> / <a href="tel:+918986047584" style="color:var(--rose-primary);font-weight:700;">+91 89860 47584</a>
              </div>
            </div>
          </div>
        </div>

        <div style="display: flex; gap: 14px; flex-wrap: wrap;">
          <a href="https://maps.google.com/?q=Ladies+Zone+Boring+Road+Patna" target="_blank" rel="noopener" class="btn-hero-primary">
            <span>📍 Get Directions on Google Maps</span>
          </a>
          <a href="https://wa.me/917091518548?text=Hello%20Ladies%20Zone,%20I%20want%20to%20visit%20the%20showroom%20today" target="_blank" rel="noopener" class="btn-hero-secondary">
            <span>💬 Message on WhatsApp</span>
          </a>
        </div>
      </div>

      <div class="showroom-map-wrap">
        <iframe 
          title="Ladies Zone Patna Location" 
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14390.871168496417!2d85.1105908!3d25.6142646!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39ed583a216b3f7f%3A0xb36b3ea4e17ef748!2sBoring%20Rd%2C%20Patna%2C%20Bihar!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin" 
          loading="lazy">
        </iframe>
      </div>
    </div>
  </section>

  <!-- Customer Reviews -->
  <section class="reviews-section">
    <div class="section-header">
      <span class="section-tag">Customer Love</span>
      <h2 class="section-title">What Our Customers Say</h2>
      <p class="section-desc">Real experiences from shoppers who visited our Boring Road showroom.</p>
    </div>

    <div class="reviews-grid">
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"Bought my bridal heels and sangeet juttis from Ladies Zone Boring Road. The memory foam padding is a lifesaver! Wore them for 6 hours straight without any pain. Highly recommended!"</p>
        <div>
          <div class="review-author">Pooja Sharma</div>
          <div class="review-loc">Kankarbagh, Patna</div>
        </div>
      </div>

      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"Smart prices and lovely variety! Their Anarkali suit collection is as good as premium designer boutiques in Delhi. The staff let me try multiple sizes patiently."</p>
        <div>
          <div class="review-author">Ananya Verma</div>
          <div class="review-loc">S.K. Puri, Patna</div>
        </div>
      </div>

      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"I always enquire on WhatsApp first to check if my size is available, and they keep it ready at the showroom counter. Super smooth shopping experience in Boring Road."</p>
        <div>
          <div class="review-author">Ritu Raj</div>
          <div class="review-loc">Bailey Road, Patna</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Luxury Footer -->
  <footer class="site-footer">
    <div class="footer-container">
      <div>
        <div class="footer-brand-title">Ladies Zone Exclusive Showroom</div>
        <p class="footer-brand-desc">
          Patna's premier women's fashion destination. Specializing in comfortable party heels, handcrafted bridal footwear, ethnic mojari, designer salwar suits, and western wear at smart prices.
        </p>
        <div style="font-size: 0.85rem; color: #ffd6e0;">
          📍 Boring Road, S.K. Puri, Patna, Bihar — 800001
        </div>
      </div>

      <div>
        <div class="footer-col-title">Categories</div>
        <ul class="footer-links">
          <li><a href="#catalog" onclick="filterByCategory('heels')">Heels & Sandals</a></li>
          <li><a href="#catalog" onclick="filterByCategory('bridal')">Bridal Footwear</a></li>
          <li><a href="#catalog" onclick="filterByCategory('mojari')">Ethnic Mojari & Jutti</a></li>
          <li><a href="#catalog" onclick="filterByCategory('suits')">Suits & Ethnic Wear</a></li>
          <li><a href="#catalog" onclick="filterByCategory('western')">Western Dresses</a></li>
        </ul>
      </div>

      <div>
        <div class="footer-col-title">Showroom Policies</div>
        <ul class="footer-links">
          <li><a href="#showroom">In-Store Trial Policy</a></li>
          <li><a href="#showroom">Showroom Exchange Policy</a></li>
          <li><a href="#showroom">WhatsApp Booking Service</a></li>
          <li><a href="#showroom">Customer Support</a></li>
        </ul>
      </div>

      <div>
        <div class="footer-col-title">Showroom Timings</div>
        <p style="font-size: 0.88rem; line-height: 1.6; margin-bottom: 12px; color: #d1b5be;">
          Monday – Sunday:<br />
          <strong>10:30 AM – 9:00 PM</strong><br />
          Open All 7 Days
        </p>
        <p style="font-size: 0.88rem; color: #d1b5be;">
          WhatsApp Enquiries:<br />
          <strong style="color:#ffd6e0;">+91 70915 18548</strong>
        </p>
      </div>
    </div>

    <div class="footer-bottom">
      &copy; 2026 Ladies Zone Exclusive Showroom. All rights reserved. Operated by Ladies Zone, Patna, Bihar, India.
    </div>
  </footer>

  <!-- Modal 1: Staff Admin Login -->
  <div id="loginModal" class="modal-overlay">
    <div class="modal-box">
      <button class="modal-close-btn" onclick="closeLoginModal()">✕</button>
      <h3 class="modal-title">Staff Admin Login</h3>
      <p class="modal-desc">Authorized showroom personnel only. Log in to add photos and manage product inventory.</p>

      <form id="adminLoginForm" onsubmit="handleLoginSubmit(event)">
        <div class="form-group">
          <label class="form-label">Staff ID or Phone</label>
          <input type="text" id="loginUsername" class="form-control" placeholder="admin or 8986047584" required />
        </div>
        <div class="form-group">
          <label class="form-label">Admin PIN</label>
          <input type="password" id="loginPin" class="form-control" placeholder="Enter PIN (e.g. 8986)" required />
        </div>
        <div id="loginError" style="color:var(--danger-red); font-size:0.82rem; margin-bottom:12px; display:none;">
          Invalid Staff ID or PIN. Please try again.
        </div>
        <button type="submit" class="btn-hero-primary" style="width:100%; justify-content:center;">
          Login to Staff Dashboard
        </button>
      </form>
    </div>
  </div>

  <!-- Modal 2: Add New Product / Upload Photo -->
  <div id="addProductModal" class="modal-overlay">
    <div class="modal-box" style="max-width: 600px;">
      <button class="modal-close-btn" onclick="closeAddProductModal()">✕</button>
      <h3 class="modal-title">Add New Product</h3>
      <p class="modal-desc">Upload a photo from your phone or PC, set the price, and publish instantly to the catalog.</p>

      <form id="addProductForm" onsubmit="handleAddProductSubmit(event)">
        <!-- Photo Upload Dropzone -->
        <div class="form-group">
          <label class="form-label">Product Photo *</label>
          <div class="photo-dropzone" onclick="document.getElementById('fileUploadInput').click()">
            <div style="font-size: 2rem; margin-bottom: 6px;">📸</div>
            <div style="font-weight: 700; color: var(--plum);">Tap to take photo or choose from gallery</div>
            <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 4px;">Supports JPG, PNG, WEBP (auto-compressed)</div>
          </div>
          <input type="file" id="fileUploadInput" accept="image/*" style="display:none;" onchange="handleImageFileSelect(event)" />
          <div id="previewImgBox" class="preview-img-box">
            <img id="previewImgElement" src="" alt="Selected Product Preview" />
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Product Name / Title *</label>
          <input type="text" id="newProdName" class="form-control" placeholder="e.g. Royal Rose Gold Bridal Heels" required />
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">Category *</label>
            <select id="newProdCat" class="form-control" required>
              <option value="heels">Heels & Sandals</option>
              <option value="bridal">Bridal Footwear</option>
              <option value="mojari">Ethnic Mojari & Jutti</option>
              <option value="suits">Suits & Ethnic Wear</option>
              <option value="western">Western Dresses</option>
            </select>
          </div>

          <div class="form-group">
            <label class="form-label">Tag / Label</label>
            <select id="newProdTag" class="form-control">
              <option value="New Arrival">New Arrival</option>
              <option value="Bestseller">Bestseller</option>
              <option value="Trending">Trending</option>
              <option value="Festive Special">Festive Special</option>
              <option value="Showroom Pick">Showroom Pick</option>
            </select>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">Showroom Price (₹) *</label>
            <input type="number" id="newProdPrice" class="form-control" placeholder="1899" required />
          </div>

          <div class="form-group">
            <label class="form-label">MRP (₹) (Optional strikethrough)</label>
            <input type="number" id="newProdMrp" class="form-control" placeholder="2999" />
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Available Sizes (Comma separated)</label>
          <input type="text" id="newProdSizes" class="form-control" placeholder="36, 37, 38, 39, 40 or M, L, XL" />
        </div>

        <div class="form-group">
          <label class="form-label">Short Description</label>
          <textarea id="newProdDesc" class="form-control" rows="2" placeholder="Fabric, heel height, fit notes, etc."></textarea>
        </div>

        <button type="submit" class="btn-hero-primary" style="width:100%; justify-content:center; padding: 12px;">
          ✨ Publish to Showroom Catalog
        </button>
      </form>
    </div>
  </div>

  <!-- Modal 3: Quick View Details -->
  <div id="quickViewModal" class="modal-overlay">
    <div class="modal-box" style="max-width: 620px;">
      <button class="modal-close-btn" onclick="closeQuickViewModal()">✕</button>
      <div id="quickViewContent">
        <!-- Rendered by JS -->
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="toastMsg" class="toast-msg">
    <span id="toastText">Action successful</span>
  </div>

  <!-- Master JavaScript Application -->
  <script>
    // Initial Starter Catalog
    const DEFAULT_CATALOG = {catalog_json_str};

    const WHATSAPP_NUMBERS = ["917091518548", "918986047584"];
    const PRIMARY_WA = "917091518548";

    // App State
    let products = [];
    let currentCategory = 'all';
    let searchQuery = '';
    let sortMode = 'featured';
    let isAdmin = false;
    let uploadedImageBase64 = '';

    // Initialize Catalog from localStorage or fallback
    function initApp() {{
      const savedProducts = localStorage.getItem('lz_catalog_products_v2');
      if (savedProducts) {{
        try {{
          products = JSON.parse(savedProducts);
        }} catch(e) {{
          products = [...DEFAULT_CATALOG];
        }}
      }} else {{
        products = [...DEFAULT_CATALOG];
        saveCatalog();
      }}

      // Check Admin Session
      const savedSession = sessionStorage.getItem('lz_admin_logged_in');
      if (savedSession === 'true') {{
        isAdmin = true;
      }}

      updateAdminUI();
      renderProducts();
    }}

    function saveCatalog() {{
      try {{
        localStorage.setItem('lz_catalog_products_v2', JSON.stringify(products));
      }} catch(e) {{
        console.warn("Storage quota exceeded", e);
        showToast("Storage quota warning: please backup catalog");
      }}
    }}

    function showToast(msg) {{
      const t = document.getElementById('toastMsg');
      const txt = document.getElementById('toastText');
      txt.textContent = msg;
      t.style.display = 'flex';
      setTimeout(() => {{
        t.style.display = 'none';
      }}, 3500);
    }}

    // Render Products Grid
    function renderProducts() {{
      const grid = document.getElementById('productsGrid');
      grid.innerHTML = '';

      let filtered = products.filter(p => {{
        const matchesCategory = (currentCategory === 'all' || p.category === currentCategory);
        const matchesSearch = !searchQuery || 
          p.name.toLowerCase().includes(searchQuery.toLowerCase()) || 
          (p.description && p.description.toLowerCase().includes(searchQuery.toLowerCase())) ||
          (p.tag && p.tag.toLowerCase().includes(searchQuery.toLowerCase()));
        return matchesCategory && matchesSearch;
      }});

      // Sorting
      if (sortMode === 'price-asc') {{
        filtered.sort((a, b) => Number(a.price) - Number(b.price));
      }} else if (sortMode === 'price-desc') {{
        filtered.sort((a, b) => Number(b.price) - Number(a.price));
      }}

      if (filtered.length === 0) {{
        grid.innerHTML = `
          <div style="grid-column: 1 / -1; text-align: center; padding: 60px 20px;">
            <div style="font-size: 3rem; margin-bottom: 12px;">🛍️</div>
            <h3 style="font-family: var(--font-display); color: var(--plum); margin-bottom: 8px;">No Products Found</h3>
            <p style="color: var(--text-muted); margin-bottom: 18px;">Try clearing your search query or selecting a different category.</p>
            <button class="btn-hero-primary" onclick="filterByCategory('all')">Show All Items</button>
          </div>
        `;
        return;
      }}

      filtered.forEach(p => {{
        const card = document.createElement('div');
        card.className = 'product-card';
        card.dataset.id = p.id;

        const discountPercent = p.mrp && p.mrp > p.price 
          ? Math.round(((p.mrp - p.price) / p.mrp) * 100) 
          : 0;

        const sizeChips = (p.sizes && p.sizes.length) 
          ? p.sizes.map(s => `<span class="size-chip">${{s}}</span>`).join('') 
          : '<span class="size-chip">Standard</span>';

        const waText = encodeURIComponent(
          `Hello Ladies Zone Showroom! I am interested in trying "${{p.name}}" (ID: ${{p.id}}, Price: ₹${{p.price}}) at your Boring Road showroom. Is this piece available for a trial?`
        );
        const waLink = `https://wa.me/${{PRIMARY_WA}}?text=${{waText}}`;

        card.innerHTML = `
          <div class="card-media-wrap">
            <img src="${{p.image}}" alt="${{p.name}}" class="card-img" loading="lazy" />
            <span class="card-tag-badge">${{p.tag || 'Showroom Pick'}}</span>
            <span class="card-trial-badge">🏬 Trial in Store</span>
            <button class="card-quick-view" onclick="openQuickView('${{p.id}}')">Quick View 👁️</button>
          </div>

          <div class="card-body">
            <div class="card-cat-label">${{p.categoryName || p.category}}</div>
            <h4 class="card-title">${{p.name}}</h4>

            <div class="card-price-row">
              <span class="card-price-current">₹${{Number(p.price).toLocaleString('en-IN')}}</span>
              ${{p.mrp && p.mrp > p.price ? `<span class="card-price-mrp">₹${{Number(p.mrp).toLocaleString('en-IN')}}</span>` : ''}}
              ${{discountPercent > 0 ? `<span class="card-discount-tag">${{discountPercent}}% OFF</span>` : ''}}
            </div>

            <div class="card-sizes-row">
              <span class="size-label">Sizes:</span>
              ${{sizeChips}}
            </div>

            <div class="card-actions">
              <a href="${{waLink}}" target="_blank" rel="noopener" class="btn-card-whatsapp">
                <span>💬 Enquire on WhatsApp</span>
              </a>

              <!-- Admin Controls (Toggled by admin status) -->
              <div class="card-admin-row" style="display: ${{isAdmin ? 'flex' : 'none'}};">
                <button class="btn-card-edit" onclick="editProductPrice('${{p.id}}')">✏️ Edit Price</button>
                <button class="btn-card-delete" onclick="deleteProduct('${{p.id}}')">🗑️ Delete</button>
              </div>
            </div>
          </div>
        `;

        grid.appendChild(card);
      }});
    }}

    // Filter by Category
    function filterByCategory(cat) {{
      currentCategory = cat;
      const pills = document.querySelectorAll('.tab-pill');
      pills.forEach(pill => {{
        const text = pill.textContent.toLowerCase();
        if (cat === 'all' && text.includes('all')) {{
          pill.classList.add('active');
        }} else if (cat === 'heels' && text.includes('heels')) {{
          pill.classList.add('active');
        }} else if (cat === 'bridal' && text.includes('bridal')) {{
          pill.classList.add('active');
        }} else if (cat === 'mojari' && text.includes('mojari')) {{
          pill.classList.add('active');
        }} else if (cat === 'suits' && text.includes('suits')) {{
          pill.classList.add('active');
        }} else if (cat === 'western' && text.includes('western')) {{
          pill.classList.add('active');
        }} else {{
          pill.classList.remove('active');
        }}
      }});

      renderProducts();
      const el = document.getElementById('catalog');
      if (el) el.scrollIntoView({{ behavior: 'smooth' }});
    }}

    function handleSearch() {{
      searchQuery = document.getElementById('searchInput').value.trim();
      renderProducts();
    }}

    function handleSort() {{
      sortMode = document.getElementById('sortSelect').value;
      renderProducts();
    }}

    // Quick View Modal
    function openQuickView(prodId) {{
      const p = products.find(x => x.id === prodId);
      if (!p) return;

      const discountPercent = p.mrp && p.mrp > p.price 
        ? Math.round(((p.mrp - p.price) / p.mrp) * 100) 
        : 0;

      const waText = encodeURIComponent(
        `Hello Ladies Zone Showroom! I would like to book a trial for "${{p.name}}" (ID: ${{p.id}}, Price: ₹${{p.price}}) at Boring Road, Patna.`
      );
      const waLink = `https://wa.me/${{PRIMARY_WA}}?text=${{waText}}`;

      const content = document.getElementById('quickViewContent');
      content.innerHTML = `
        <div style="display: flex; flex-direction: column; gap: 20px;">
          <div style="width: 100%; height: 320px; border-radius: var(--radius-md); overflow: hidden; background:#f7f4f2;">
            <img src="${{p.image}}" alt="${{p.name}}" style="width: 100%; height: 100%; object-fit: cover;" />
          </div>

          <div>
            <div style="font-size:0.8rem; color:var(--rose-primary); font-weight:700; text-transform:uppercase; margin-bottom:4px;">
              ${{p.categoryName || p.category}} • ${{p.tag || 'Showroom Exclusive'}}
            </div>
            <h3 style="font-family:var(--font-display); font-size:1.6rem; color:var(--plum); font-weight:700; margin-bottom:8px;">
              ${{p.name}}
            </h3>

            <div style="display:flex; align-items:baseline; gap:12px; margin-bottom:14px;">
              <span style="font-size:1.6rem; font-weight:800; color:var(--plum);">₹${{Number(p.price).toLocaleString('en-IN')}}</span>
              ${{p.mrp && p.mrp > p.price ? `<span style="font-size:1rem; color:#888; text-decoration:line-through;">₹${{Number(p.mrp).toLocaleString('en-IN')}}</span>` : ''}}
              ${{discountPercent > 0 ? `<span class="card-discount-tag">${{discountPercent}}% OFF</span>` : ''}}
            </div>

            <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.6; margin-bottom:18px;">
              ${{p.description || 'Visit our showroom in Boring Road, S.K. Puri, Patna to try this item in person with comfort fitting and custom size assistance.'}}
            </p>

            <div style="background:#fdf5f7; border:1px solid #f2d9e0; border-radius:var(--radius-sm); padding:12px 16px; margin-bottom:20px; font-size:0.84rem; color:var(--rose-dark);">
              🏬 <strong>Showroom Trial Service:</strong> No online payment required. Send us a WhatsApp message with your size, and our team will keep this piece ready in our Boring Road showroom!
            </div>

            <div style="display:flex; gap:12px; flex-wrap:wrap;">
              <a href="${{waLink}}" target="_blank" rel="noopener" class="btn-hero-primary" style="flex:1; justify-content:center;">
                💬 Enquire on WhatsApp
              </a>
              <a href="tel:+917091518548" class="btn-hero-secondary" style="justify-content:center;">
                📞 Call Showroom
              </a>
            </div>
          </div>
        </div>
      `;

      document.getElementById('quickViewModal').style.display = 'flex';
    }}

    function closeQuickViewModal() {{
      document.getElementById('quickViewModal').style.display = 'none';
    }}

    // Admin Authentication
    function openLoginModal() {{
      if (isAdmin) {{
        showToast("You are already logged in as Staff Admin");
        return;
      }}
      document.getElementById('loginModal').style.display = 'flex';
      document.getElementById('loginError').style.display = 'none';
    }}

    function closeLoginModal() {{
      document.getElementById('loginModal').style.display = 'none';
    }}

    function handleLoginSubmit(e) {{
      e.preventDefault();
      const u = document.getElementById('loginUsername').value.trim();
      const p = document.getElementById('loginPin').value.trim();

      // Accepted credentials: ID: admin or 8986047584; PIN: 8986
      if ((u.toLowerCase() === 'admin' || u === '8986047584' || u === '7091518548') && p === '8986') {{
        isAdmin = true;
        sessionStorage.setItem('lz_admin_logged_in', 'true');
        closeLoginModal();
        updateAdminUI();
        renderProducts();
        showToast("👑 Welcome back, Showroom Manager!");
      }} else {{
        document.getElementById('loginError').style.display = 'block';
      }}
    }}

    function adminLogout() {{
      isAdmin = false;
      sessionStorage.removeItem('lz_admin_logged_in');
      updateAdminUI();
      renderProducts();
      showToast("Logged out of Staff Mode");
    }}

    function updateAdminUI() {{
      const banner = document.getElementById('adminBanner');
      const staffBtn = document.getElementById('staffLoginBtn');

      if (isAdmin) {{
        banner.style.display = 'flex';
        staffBtn.innerHTML = '👑 Staff Active';
        staffBtn.style.background = '#e8f5e9';
        staffBtn.style.color = '#2e7d32';
      }} else {{
        banner.style.display = 'none';
        staffBtn.innerHTML = '🔒 Staff Login';
        staffBtn.style.background = 'var(--rose-light)';
        staffBtn.style.color = 'var(--rose-dark)';
      }}
    }}

    // Delete Product
    function deleteProduct(prodId) {{
      const p = products.find(x => x.id === prodId);
      if (!p) return;

      const confirmDel = confirm(`Are you sure you want to permanently delete "${{p.name}}"?`);
      if (confirmDel) {{
        products = products.filter(x => x.id !== prodId);
        saveCatalog();
        renderProducts();
        showToast(`🗑️ Deleted "${{p.name}}"`);
      }}
    }}

    // Edit Price
    function editProductPrice(prodId) {{
      const p = products.find(x => x.id === prodId);
      if (!p) return;

      const newPriceStr = prompt(`Enter new showroom price for "${{p.name}}" (Current: ₹${{p.price}}):`, p.price);
      if (newPriceStr !== null) {{
        const newPrice = Number(newPriceStr.trim());
        if (!isNaN(newPrice) && newPrice > 0) {{
          p.price = newPrice;
          saveCatalog();
          renderProducts();
          showToast(`✏️ Updated price to ₹${{newPrice}}`);
        }} else {{
          alert("Please enter a valid price number.");
        }}
      }}
    }}

    // Add Product Modal & Image Handling
    function openAddProductModal() {{
      uploadedImageBase64 = '';
      document.getElementById('previewImgBox').style.display = 'none';
      document.getElementById('addProductForm').reset();
      document.getElementById('addProductModal').style.display = 'flex';
    }}

    function closeAddProductModal() {{
      document.getElementById('addProductModal').style.display = 'none';
    }}

    function handleImageFileSelect(e) {{
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(event) {{
        const img = new Image();
        img.onload = function() {{
          // Compress via Canvas to avoid storage limits
          const canvas = document.createElement('canvas');
          const maxDim = 800;
          let width = img.width;
          let height = img.height;

          if (width > height) {{
            if (width > maxDim) {{
              height = Math.round((height * maxDim) / width);
              width = maxDim;
            }}
          }} else {{
            if (height > maxDim) {{
              width = Math.round((width * maxDim) / height);
              height = maxDim;
            }}
          }}

          canvas.width = width;
          canvas.height = height;
          const ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0, width, height);

          uploadedImageBase64 = canvas.toDataURL('image/jpeg', 0.82);
          document.getElementById('previewImgElement').src = uploadedImageBase64;
          document.getElementById('previewImgBox').style.display = 'block';
        }};
        img.src = event.target.result;
      }};
      reader.readAsDataURL(file);
    }}

    function handleAddProductSubmit(e) {{
      e.preventDefault();

      const name = document.getElementById('newProdName').value.trim();
      const cat = document.getElementById('newProdCat').value;
      const tag = document.getElementById('newProdTag').value;
      const price = Number(document.getElementById('newProdPrice').value);
      const mrp = Number(document.getElementById('newProdMrp').value) || 0;
      const rawSizes = document.getElementById('newProdSizes').value.trim();
      const desc = document.getElementById('newProdDesc').value.trim();

      const catNames = {{
        'heels': 'Heels & Sandals',
        'bridal': 'Bridal Footwear',
        'mojari': 'Ethnic Mojari & Jutti',
        'suits': 'Suits & Ethnic Wear',
        'western': 'Western Dresses'
      }};

      const sizes = rawSizes ? rawSizes.split(',').map(s => s.trim()).filter(Boolean) : ["Standard"];

      // Default placeholder if no photo was uploaded
      const finalImage = uploadedImageBase64 || "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=800&q=80";

      const newId = 'LZ-' + Date.now().toString().slice(-6);

      const newProduct = {{
        id: newId,
        name: name,
        category: cat,
        categoryName: catNames[cat] || cat,
        price: price,
        mrp: mrp > price ? mrp : 0,
        image: finalImage,
        tag: tag,
        sizes: sizes,
        description: desc || `Exclusive ${{catNames[cat]}} piece available at Ladies Zone Showroom, Boring Road, Patna.`
      }};

      products.unshift(newProduct);
      saveCatalog();
      closeAddProductModal();
      renderProducts();
      showToast(`✨ Published "${{name}}" to catalog!`);
    }}

    // Export Catalog Backup as JSON
    function exportCatalogBackup() {{
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(products, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", `ladies-zone-catalog-backup-${{new Date().toISOString().slice(0,10)}}.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
      showToast("💾 Catalog backup downloaded!");
    }}

    // Reset Default Catalog
    function resetDefaultCatalog() {{
      const confirmReset = confirm("Reset catalog to the default showroom collection? (This will restore all default products)");
      if (confirmReset) {{
        products = [...DEFAULT_CATALOG];
        saveCatalog();
        renderProducts();
        showToast("🔄 Restored default showroom catalog");
      }}
    }}

    // Global Modal Click-Outside Listener
    window.onclick = function(event) {{
      const modals = ['loginModal', 'addProductModal', 'quickViewModal'];
      modals.forEach(mId => {{
        const el = document.getElementById(mId);
        if (event.target === el) {{
          el.style.display = 'none';
        }}
      }});
    }};

    // Start App
    window.addEventListener('DOMContentLoaded', initApp);
  </script>
</body>
</html>
'''

with open(PROJECT_DIR / "index.html", "w", encoding="utf-8") as f:
    f.write(INDEX_HTML_CONTENT)

print("Generated fresh index.html successfully!")

# 3. Generate robots.txt
ROBOTS_TXT = """User-agent: *
Allow: /

Sitemap: https://ladieszonepatna.in/sitemap.xml
"""
with open(PROJECT_DIR / "robots.txt", "w", encoding="utf-8") as f:
    f.write(ROBOTS_TXT)

# 4. Generate sitemap.xml
SITEMAP_XML = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://ladieszonepatna.in/</loc>
    <lastmod>2026-10-16</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.00</priority>
  </url>
  <url>
    <loc>https://ladieszone.pages.dev/</loc>
    <lastmod>2026-10-16</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.90</priority>
  </url>
</urlset>
"""
with open(PROJECT_DIR / "sitemap.xml", "w", encoding="utf-8") as f:
    f.write(SITEMAP_XML)

# 5. Generate _headers for Cloudflare Pages
HEADERS = """/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()
  Cache-Control: public, max-age=3600
"""
with open(PROJECT_DIR / "_headers", "w", encoding="utf-8") as f:
    f.write(HEADERS)

# 6. Generate _redirects
REDIRECTS = """/home / 301
"""
with open(PROJECT_DIR / "_redirects", "w", encoding="utf-8") as f:
    f.write(REDIRECTS)

print("All static assets, SEO files & metadata created successfully!")
