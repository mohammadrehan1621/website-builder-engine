"""
Fresh, luxurious, from-scratch website generator for Ladies Zone Exclusive Showroom.
Generates a complete modern standalone boutique web application with:
1. Editorial luxury design (Playfair Display + Plus Jakarta Sans, rose gold / burgundy / warm cream palette)
2. 5 Master Categories (Heels & Sandals, Bridal Footwear, Ethnic Mojari & Jutti, Suits & Ethnic Wear, Western Dresses)
3. Zero online checkout — strictly showroom showcase + instant WhatsApp trial inquiry
4. Staff Admin Panel with Photo Upload & Delete Products (saves to localStorage & IndexedDB)
5. Showroom Visit & Google Maps section for Boring Road, S.K. Puri, Patna
6. Schema.org ClothingStore/ShoeStore SEO markup, sitemap.xml, robots.txt
"""

import os
import json
import base64
from pathlib import Path
from PIL import Image
import io

PROJECT_DIR = Path(r"C:\Users\rehan\Desktop\website_builder\projects\ladies_zone")
PROJECT_DIR.mkdir(parents=True, exist_ok=True)
ASSETS_DIR = PROJECT_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# 1. Process Logo
SRC_LOGO = Path(r"C:\Users\rehan\Downloads\Programs\fashion-shop\assets\logo-banner.png")
if SRC_LOGO.exists():
    with open(SRC_LOGO, "rb") as f:
        raw_logo = f.read()
    logo_b64 = "data:image/png;base64," + base64.b64encode(raw_logo).decode('utf-8')
    with open(ASSETS_DIR / "logo.png", "wb") as f:
        f.write(raw_logo)
else:
    logo_b64 = ""

print(f"Logo ready (size: {len(logo_b64)} chars)")

# 2. Curated Starter Catalog with High Fashion Imagery across all 5 Categories
STARTER_PRODUCTS = [
    # Heels & Sandals
    {
        "id": "LZ-HS-01",
        "name": "Rose Gold Metallic Stiletto Heels",
        "category": "heels",
        "categoryName": "Heels & Sandals",
        "price": 1899,
        "mrp": 2999,
        "image": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=800&q=80",
        "tag": "Trending",
        "sizes": ["36", "37", "38", "39", "40"],
        "description": "Exquisite rose-gold 3.5-inch pencil heels with memory foam insole for comfortable evening and party wear."
    },
    {
        "id": "LZ-HS-02",
        "name": "Nude Strappy Kitten Heel Sandals",
        "category": "heels",
        "categoryName": "Heels & Sandals",
        "price": 1499,
        "mrp": 2299,
        "image": "https://images.unsplash.com/photo-1515347619252-60a4bf4fff4f?auto=format&fit=crop&w=800&q=80",
        "tag": "Bestseller",
        "sizes": ["36", "37", "38", "39", "40", "41"],
        "description": "Ultra-versatile 2-inch kitten heels with delicate criss-cross ankle straps. Perfect for long office days or evening dinners."
    },
    {
        "id": "LZ-HS-03",
        "name": "Pearl-Embellished Block Heel Sandal",
        "category": "heels",
        "categoryName": "Heels & Sandals",
        "price": 1699,
        "mrp": 2599,
        "image": "https://images.unsplash.com/photo-1596704017254-9b121068fb31?auto=format&fit=crop&w=800&q=80",
        "tag": "New Arrival",
        "sizes": ["37", "38", "39", "40"],
        "description": "Hand-stitched faux pearls on lustrous champagne straps with sturdy 2.5-inch block heel for effortless balance."
    },
    # Bridal Footwear
    {
        "id": "LZ-BR-01",
        "name": "Royal Zardozi Handcrafted Bridal Heels",
        "category": "bridal",
        "categoryName": "Bridal Footwear",
        "price": 3299,
        "mrp": 4999,
        "image": "https://images.unsplash.com/photo-1535043934128-cf0b28d52f95?auto=format&fit=crop&w=800&q=80",
        "tag": "Bridal Special",
        "sizes": ["36", "37", "38", "39", "40"],
        "description": "Rich crimson silk base hand-embroidered with dabka, gota patti, and zardozi threadwork. Features dual-cushioned sole for wedding ceremonies."
    },
    {
        "id": "LZ-BR-02",
        "name": "Golden Crystal Shimmer Bridal Wedges",
        "category": "bridal",
        "categoryName": "Bridal Footwear",
        "price": 2799,
        "mrp": 3999,
        "image": "https://images.unsplash.com/photo-1560343090-f0409e92791a?auto=format&fit=crop&w=800&q=80",
        "tag": "Bestseller",
        "sizes": ["36", "37", "38", "39", "40", "41"],
        "description": "Glamorous crystal-encrusted front strap on comfortable 3-inch platform wedge. Ideal for sangeet and reception dances."
    },
    {
        "id": "LZ-BR-03",
        "name": "Embellished Wedding Half-Shoe Mules",
        "category": "bridal",
        "categoryName": "Bridal Footwear",
        "price": 2499,
        "mrp": 3499,
        "image": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=800&q=80",
        "tag": "New Arrival",
        "sizes": ["37", "38", "39", "40"],
        "description": "Slip-on pointed toe bridal mules with mirror and beadwork. Elegant, comfortable, and easy to slip off during rituals."
    },
    # Ethnic Mojari & Jutti
    {
        "id": "LZ-MJ-01",
        "name": "Mirror-Work Velvet Royal Jutti",
        "category": "mojari",
        "categoryName": "Ethnic Mojari & Jutti",
        "price": 1299,
        "mrp": 1999,
        "image": "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?auto=format&fit=crop&w=800&q=80",
        "tag": "Bestseller",
        "sizes": ["36", "37", "38", "39", "40"],
        "description": "Hand-stitched genuine leather sole with deep wine velvet upper adorned with miniature cut-glass mirrors and resham embroidery."
    },
    {
        "id": "LZ-MJ-02",
        "name": "Punjabi Floral Threadwork Mojari",
        "category": "mojari",
        "categoryName": "Ethnic Mojari & Jutti",
        "price": 1199,
        "mrp": 1799,
        "image": "https://images.unsplash.com/photo-1582533561751-ef6f6ab93a2e?auto=format&fit=crop&w=800&q=80",
        "tag": "Festive",
        "sizes": ["36", "37", "38", "39", "40", "41"],
        "description": "Pastel floral threadwork on soft ivory base. Bite-free padded leather lining ensures all-day comfort without blisters."
    },
    {
        "id": "LZ-MJ-03",
        "name": "Golden Tilla Hand-Embroidered Jutti",
        "category": "mojari",
        "categoryName": "Ethnic Mojari & Jutti",
        "price": 1399,
        "mrp": 2199,
        "image": "https://images.unsplash.com/photo-1562273138-f46be4ebdf33?auto=format&fit=crop&w=800&q=80",
        "tag": "Trending",
        "sizes": ["37", "38", "39", "40"],
        "description": "Intricate antique gold zari tilla work crafted by master artisans. Classic curved silhouette suitable for all ethnic ensembles."
    },
    # Suits & Ethnic Wear
    {
        "id": "LZ-ST-01",
        "name": "Pastel Peach Organza Anarkali Suit Set",
        "category": "suits",
        "categoryName": "Suits & Ethnic Wear",
        "price": 3899,
        "mrp": 5999,
        "image": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=800&q=80",
        "tag": "Bestseller",
        "sizes": ["M", "L", "XL", "XXL"],
        "description": "3-Piece designer set featuring fine organza flared Anarkali with intricate gota patti border, matching pants, and hand-painted dupatta."
    },
    {
        "id": "LZ-ST-02",
        "name": "Banarasi Silk Festive Kurta & Pant Set",
        "category": "suits",
        "categoryName": "Suits & Ethnic Wear",
        "price": 3299,
        "mrp": 4899,
        "image": "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=800&q=80",
        "tag": "Festive Special",
        "sizes": ["S", "M", "L", "XL"],
        "description": "Royal emerald green Banarasi silk weave kurta featuring antique gold motifs, paired with straight trousers and a contrasting woven dupatta."
    },
    {
        "id": "LZ-ST-03",
        "name": "Hand-Embroidered Chanderi Salwar Suit",
        "category": "suits",
        "categoryName": "Suits & Ethnic Wear",
        "price": 2899,
        "mrp": 4299,
        "image": "https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?auto=format&fit=crop&w=800&q=80",
        "tag": "New Arrival",
        "sizes": ["M", "L", "XL"],
        "description": "Soft breathable Chanderi silk suit with fine zardozi neck yoke, comfortable cotton silk salwar, and scalloped organza dupatta."
    },
    # Western Dresses
    {
        "id": "LZ-WD-01",
        "name": "Rose Gold Satin Wrap Midi Dress",
        "category": "western",
        "categoryName": "Western Dresses",
        "price": 1999,
        "mrp": 3199,
        "image": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=800&q=80",
        "tag": "Trending",
        "sizes": ["S", "M", "L"],
        "description": "Silky satin wrap silhouette with flattering V-neckline, self-tie sash, and tulip hem. Tailored for cocktail events and dinners."
    },
    {
        "id": "LZ-WD-02",
        "name": "Pleated Floral Chiffon A-Line Dress",
        "category": "western",
        "categoryName": "Western Dresses",
        "price": 1799,
        "mrp": 2799,
        "image": "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?auto=format&fit=crop&w=800&q=80",
        "tag": "Bestseller",
        "sizes": ["XS", "S", "M", "L", "XL"],
        "description": "Lightweight botanical print chiffon dress with micro-pleated skirt and subtle balloon sleeves. Lined with soft breathable viscose."
    },
    {
        "id": "LZ-WD-03",
        "name": "Emerald Velvet Evening Cocktail Dress",
        "category": "western",
        "categoryName": "Western Dresses",
        "price": 2399,
        "mrp": 3699,
        "image": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?auto=format&fit=crop&w=800&q=80",
        "tag": "New Arrival",
        "sizes": ["S", "M", "L"],
        "description": "Luxe stretch velvet bodycon midi featuring sweetheart neckline and side slit. Crafted for glamorous party and celebration nights."
    }
]

catalog_json_str = json.dumps(STARTER_PRODUCTS, indent=2)

print(f"Generated {len(STARTER_PRODUCTS)} starter products across 5 categories.")
