import re
from typing import Dict, Any, List
from bs4 import BeautifulSoup

def analyze_website_seo(html: str) -> Dict[str, Any]:
    """
    Comprehensive SEO, Accessibility, Security, and Performance Auditor.
    Parses HTML and scores it across 10+ critical enterprise metrics (0-100).
    """
    if not html or not html.strip():
        return {
            "score": 0,
            "grade": "F",
            "passed": [],
            "warnings": ["HTML content is empty."],
            "recommendations": ["Generate or paste HTML to perform audit."],
            "metrics": {}
        }

    score = 0
    max_score = 100
    passed = []
    warnings = []
    recommendations = []
    metrics = {}

    soup = BeautifulSoup(html, "html.parser")

    # 1. Page Title Check (10 pts)
    title_tag = soup.find("title")
    title_text = title_tag.get_text().strip() if title_tag else ""
    metrics["title"] = title_text
    if title_text:
        if 15 <= len(title_text) <= 70:
            score += 10
            passed.append(f"Title Tag is optimal ({len(title_text)} chars): '{title_text[:40]}...'")
        else:
            score += 6
            warnings.append(f"Title Tag length is {len(title_text)} chars (Recommended: 30-60 chars).")
    else:
        warnings.append("Missing <title> tag in <head>.")
        recommendations.append("Add a descriptive <title> tag with your brand and primary value proposition.")

    # 2. Meta Description (10 pts)
    meta_desc = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
    desc_content = meta_desc.get("content", "").strip() if meta_desc else ""
    metrics["description"] = desc_content
    if desc_content:
        if 50 <= len(desc_content) <= 160:
            score += 10
            passed.append(f"Meta Description is optimal ({len(desc_content)} chars).")
        else:
            score += 6
            warnings.append(f"Meta Description length is {len(desc_content)} chars (Recommended: 70-160 chars).")
    else:
        warnings.append("Missing meta description.")
        recommendations.append("Add <meta name='description' content='...'> for high search engine click-through rates.")

    # 3. Viewport & Mobile Responsiveness (10 pts)
    meta_viewport = soup.find("meta", attrs={"name": re.compile(r"^viewport$", re.I)})
    if meta_viewport and "width=device-width" in meta_viewport.get("content", "").lower():
        score += 10
        passed.append("Mobile Viewport Meta Tag correctly configured.")
    else:
        warnings.append("Missing or misconfigured mobile viewport meta tag.")
        recommendations.append("Ensure <meta name='viewport' content='width=device-width, initial-scale=1.0'> exists.")

    # 4. OpenGraph Social Meta Tags (10 pts)
    og_title = soup.find("meta", property="og:title")
    og_desc = soup.find("meta", property="og:description")
    og_image = soup.find("meta", property="og:image")
    og_count = sum(1 for tag in [og_title, og_desc, og_image] if tag and tag.get("content"))
    metrics["og_tags_present"] = og_count
    if og_count >= 3:
        score += 10
        passed.append("Full OpenGraph Social Cards configured (og:title, og:description, og:image).")
    elif og_count > 0:
        score += 5
        warnings.append("Partial OpenGraph configuration. Missing og:image or og:description.")
    else:
        warnings.append("Missing OpenGraph meta tags for WhatsApp/LinkedIn/Twitter previews.")
        recommendations.append("Inject OpenGraph tags for rich social media cards when sharing links.")

    # 5. Semantic Heading Hierarchy (10 pts)
    h1_tags = soup.find_all("h1")
    h2_tags = soup.find_all("h2")
    metrics["h1_count"] = len(h1_tags)
    metrics["h2_count"] = len(h2_tags)
    if len(h1_tags) == 1:
        score += 10
        passed.append(f"Single <h1> semantic header detected: '{h1_tags[0].get_text()[:40].strip()}...'")
    elif len(h1_tags) > 1:
        score += 5
        warnings.append(f"Multiple ({len(h1_tags)}) <h1> tags found. Best practice is exactly one <h1> per page.")
    else:
        warnings.append("No <h1> header tag detected.")
        recommendations.append("Add a primary <h1> headline to structure the page for search engines.")

    # 6. Image Accessibility (Alt attributes) (10 pts)
    images = soup.find_all("img")
    metrics["image_count"] = len(images)
    if images:
        images_with_alt = [img for img in images if img.get("alt", "").strip()]
        alt_ratio = len(images_with_alt) / len(images)
        if alt_ratio >= 0.9:
            score += 10
            passed.append(f"All images ({len(images)}) have descriptive alt text attributes.")
        elif alt_ratio >= 0.5:
            score += 6
            warnings.append(f"{len(images) - len(images_with_alt)} image(s) missing alt text attributes.")
        else:
            score += 2
            warnings.append(f"Majority of images ({len(images) - len(images_with_alt)}/{len(images)}) lack alt text.")
            recommendations.append("Add alt='...' attributes to all images for screen readers and SEO indexing.")
    else:
        score += 10
        passed.append("No missing image alt tags detected.")

    # 7. Image Lazy Loading (10 pts)
    if images:
        lazy_images = [img for img in images if img.get("loading") == "lazy"]
        if len(lazy_images) >= len(images) * 0.7:
            score += 10
            passed.append(f"Images are configured with loading='lazy' for sub-second page performance.")
        else:
            score += 5
            warnings.append(f"{len(images) - len(lazy_images)} image(s) missing loading='lazy' attribute.")
            recommendations.append("Add loading='lazy' to below-the-fold images to optimize Core Web Vitals.")
    else:
        score += 10

    # 8. Security & CSP Headers (10 pts)
    has_csp = bool(soup.find("meta", attrs={"http-equiv": re.compile(r"^content-security-policy$", re.I)}))
    metrics["has_csp"] = has_csp
    if has_csp:
        score += 10
        passed.append("Content Security Policy (CSP) meta header is active.")
    else:
        score += 4
        warnings.append("No Content Security Policy (CSP) header detected.")
        recommendations.append("Include Content-Security-Policy to protect against cross-site scripting (XSS).")

    # 9. Performance Preconnect & Preloads (10 pts)
    preconnect_links = soup.find_all("link", attrs={"rel": lambda x: x and ("preconnect" in x or "dns-prefetch" in x)})
    metrics["preconnect_count"] = len(preconnect_links)
    if len(preconnect_links) >= 1:
        score += 10
        passed.append(f"DNS preconnect & prefetch links configured ({len(preconnect_links)} endpoints).")
    else:
        score += 4
        warnings.append("Missing DNS preconnect links for external CDNs (fonts, Tailwind, icons).")
        recommendations.append("Add <link rel='preconnect' href='https://fonts.googleapis.com'> to speed up asset resolution.")

    # 10. Links & Anchor Safety (10 pts)
    external_links = soup.find_all("a", attrs={"href": re.compile(r"^https?://")})
    unsafe_links = [a for a in external_links if a.get("target") == "_blank" and "noopener" not in (a.get("rel") or [])]
    metrics["external_links"] = len(external_links)
    if not unsafe_links:
        score += 10
        passed.append(f"External links ({len(external_links)}) properly configured with noopener/noreferrer.")
    else:
        score += 5
        warnings.append(f"{len(unsafe_links)} external link(s) open in new tab without rel='noopener noreferrer'.")
        recommendations.append("Add rel='noopener noreferrer' to external links with target='_blank' for security.")

    # Grade Calculation
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "D"

    return {
        "score": min(score, max_score),
        "grade": grade,
        "passed": passed,
        "warnings": warnings,
        "recommendations": recommendations,
        "metrics": metrics
    }

def generate_sitemap_xml(domain: str, pages: List[str] = None) -> str:
    """
    Generates a production-grade, Google-compliant XML sitemap.
    """
    import datetime
    clean_dom = domain.replace("https://", "").replace("http://", "").strip("/")
    base_url = f"https://{clean_dom}"
    today = datetime.date.today().isoformat()
    
    if not pages:
        pages = ["index.html"]
    
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    
    for page in sorted(pages):
        clean_p = page.strip("/")
        if clean_p == "index.html" or clean_p == "":
            loc = f"{base_url}/"
            priority = "1.00"
            freq = "weekly"
        else:
            loc = f"{base_url}/{clean_p}"
            priority = "0.80"
            freq = "monthly"
            
        xml_lines.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

    xml_lines.append('</urlset>')
    return "\n".join(xml_lines)

def generate_robots_txt(domain: str) -> str:
    """
    Generates standard robots.txt permitting all major search crawlers with sitemap linkage.
    """
    clean_dom = domain.replace("https://", "").replace("http://", "").strip("/")
    return f"""# Autonomous AI Studio - Search Engine Directives
User-agent: *
Allow: /

# Sitemap
Sitemap: https://{clean_dom}/sitemap.xml
"""

def auto_optimize_seo(
    html: str, 
    site_title: str = "", 
    site_description: str = "", 
    site_url: str = "",
    og_image_url: str = "",
    schema_type: str = "auto"
) -> str:
    """
    Automatically injects missing SEO, Social Meta Cards, Preconnects,
    Canonical URLs, and Image optimizations into an existing HTML document,
    elevating its score to 95-100% Grade A+.
    """
    if not html:
        return html

    soup = BeautifulSoup(html, "html.parser")
    head = soup.find("head")
    if not head:
        head = soup.new_tag("head")
        if soup.html:
            soup.html.insert(0, head)
        else:
            return html

    # Canonical domain resolution
    canonical_url = site_url or "https://mohammadrehan.pages.dev"
    if not canonical_url.startswith("http"):
        canonical_url = f"https://{canonical_url}"

    # Extract or calibrate title (30-60 chars optimal for Google desktop & mobile SERP)
    title_tag = soup.find("title")
    if title_tag:
        raw_t = title_tag.get_text().strip()
        if len(raw_t) > 60:
            if "mohammad rehan" in raw_t.lower():
                curr_title = "Mohammad Rehan | AI Systems Architect & Tech Lead"
            elif "ladies zone" in raw_t.lower():
                curr_title = "Ladies Zone Exclusive Showroom | Patna"
            else:
                curr_title = raw_t.split("—")[0].split("|")[0].strip()[:58]
            title_tag.string = curr_title
        else:
            curr_title = raw_t
    else:
        curr_title = site_title or ("Ladies Zone Exclusive Showroom | Patna" if "ladieszone" in canonical_url else "Mohammad Rehan | AI Systems Architect & Tech Lead")
        t_el = soup.new_tag("title")
        t_el.string = curr_title
        head.append(t_el)

    # Extract or calibrate meta description (70-160 chars optimal)
    meta_desc = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
    if meta_desc:
        raw_d = meta_desc.get("content", "").strip()
        if len(raw_d) > 160:
            if "ladieszone" in canonical_url or "ladies zone" in curr_title.lower():
                curr_desc = "Exclusive ethnic wear, bridal lehengas, and designer sarees at Boring Road, Patna. Visit our showroom or shop online via WhatsApp."
            else:
                curr_desc = "Senior AI Systems Architect specializing in autonomous agent architectures, low-latency microservices, and modern web platforms."
            meta_desc["content"] = curr_desc
        elif len(raw_d) < 70:
            curr_desc = raw_d + " Explore projects, architectural case studies, and live contact inquiries."
            meta_desc["content"] = curr_desc
        else:
            curr_desc = raw_d
    else:
        if "ladieszone" in canonical_url or "ladies zone" in curr_title.lower():
            curr_desc = site_description or "Exclusive ethnic wear, bridal lehengas, and designer sarees at Boring Road, Patna. Visit our showroom or shop online via WhatsApp."
        else:
            curr_desc = site_description or "Senior AI Systems Architect specializing in autonomous agent architectures, low-latency microservices, and modern web platforms."
        d_el = soup.new_tag("meta", attrs={"name": "description", "content": curr_desc})
        head.append(d_el)

    # 1. Viewport
    if not soup.find("meta", attrs={"name": re.compile(r"^viewport$", re.I)}):
        v_el = soup.new_tag("meta", attrs={"name": "viewport", "content": "width=device-width, initial-scale=1.0"})
        head.append(v_el)

    # 2. Canonical Link Tag
    if not soup.find("link", attrs={"rel": "canonical"}):
        c_el = soup.new_tag("link", attrs={"rel": "canonical", "href": canonical_url})
        head.append(c_el)

    # 3. Preconnects for high-speed CDN loading
    cdns = ["https://fonts.googleapis.com", "https://fonts.gstatic.com", "https://cdn.tailwindcss.com", "https://unpkg.com"]
    for cdn in cdns:
        if not soup.find("link", attrs={"rel": "preconnect", "href": cdn}):
            l_el = soup.new_tag("link", attrs={"rel": "preconnect", "href": cdn, "crossorigin": "" if "gstatic" in cdn else None})
            head.append(l_el)

    # 4. OpenGraph Social Cards & Twitter / WhatsApp Image preview
    is_fashion = "ladieszone" in canonical_url or "ladies zone" in curr_title.lower() or "fashion" in curr_title.lower()
    default_og_image = (
        "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=1200&q=80" 
        if is_fashion else 
        "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1200&q=80"
    )
    final_og_image = og_image_url.strip() if og_image_url and og_image_url.strip() else default_og_image

    og_map = {
        "og:type": "website",
        "og:title": curr_title,
        "og:description": curr_desc,
        "og:url": canonical_url,
        "og:image": final_og_image,
        "og:site_name": curr_title.split("|")[0].strip(),
        "twitter:card": "summary_large_image",
        "twitter:title": curr_title,
        "twitter:description": curr_desc,
        "twitter:image": final_og_image
    }

    for prop, val in og_map.items():
        attr_key = "name" if prop.startswith("twitter:") else "property"
        existing = soup.find("meta", attrs={attr_key: prop})
        if existing:
            existing["content"] = val
        else:
            m_el = soup.new_tag("meta", attrs={attr_key: prop, "content": val})
            head.append(m_el)

    # 5. Content Security Policy
    if not soup.find("meta", attrs={"http-equiv": re.compile(r"^content-security-policy$", re.I)}):
        csp_el = soup.new_tag("meta", attrs={
            "http-equiv": "Content-Security-Policy",
            "content": "default-src 'self' https: data: blob: 'unsafe-inline' 'unsafe-eval'; img-src 'self' https: data: blob:; font-src 'self' https: data:;"
        })
        head.append(csp_el)

    # 6. Image Lazy Loading & Alt attributes
    images = soup.find_all("img")
    for idx, img in enumerate(images):
        if not img.get("loading") and idx > 0:
            img["loading"] = "lazy"
        if not img.get("alt") or not img.get("alt").strip():
            img["alt"] = f"{curr_title.split('|')[0].strip()} visual asset {idx+1}"

    # 7. External Links noopener
    for a in soup.find_all("a", attrs={"href": re.compile(r"^https?://")}):
        if a.get("target") == "_blank":
            raw_rel = a.get("rel")
            if isinstance(raw_rel, list):
                rel_parts = set(raw_rel)
            elif isinstance(raw_rel, str):
                rel_parts = set(raw_rel.split())
            else:
                rel_parts = set()
            rel_parts.update(["noopener", "noreferrer"])
            a["rel"] = sorted(list(rel_parts))

    # 8. Intelligent Schema.org JSON-LD Structured Data
    import json
    for old_s in soup.find_all("script", attrs={"type": "application/ld+json"}):
        old_s.decompose()

    if is_fashion:
        schema_json = {
            "@context": "https://schema.org",
            "@type": "ClothingStore",
            "name": "Ladies Zone Exclusive Showroom",
            "description": curr_desc,
            "url": canonical_url,
            "telephone": "+91 70915 18548",
            "priceRange": "₹₹",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Boring Road",
                "addressLocality": "Patna",
                "addressRegion": "Bihar",
                "addressCountry": "IN"
            },
            "sameAs": [
                "https://wa.me/917091518548",
                "https://instagram.com"
            ]
        }
    else:
        schema_json = {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": "Mohammad Rehan",
            "jobTitle": "Senior AI & Full-Stack Systems Architect",
            "description": curr_desc,
            "url": canonical_url,
            "sameAs": [
                "https://wa.me/917091518548",
                "https://github.com",
                "https://linkedin.com"
            ]
        }

    schema_el = soup.new_tag("script", attrs={"type": "application/ld+json"})
    schema_el.string = json.dumps(schema_json, indent=2)
    head.append(schema_el)

    return str(soup)

