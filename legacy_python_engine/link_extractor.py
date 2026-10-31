import re
import json
import requests
from typing import Dict, Any, Optional

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

def extract_youtube_video_id(url: str) -> Optional[str]:
    """Extracts 11-character YouTube video ID from various URL formats."""
    patterns = [
        r'(?:v=|\/v\/|youtu\.be\/|\/embed\/|\/shorts\/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/watch\?.*v=([a-zA-Z0-9_-]{11})',
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return None

def extract_source_data(url: str) -> Dict[str, Any]:
    """
    Autonomously extracts structured data, media assets, and embeds from YouTube, Instagram, or any website link.
    """
    clean_url = url.strip()
    if not clean_url:
        return {"success": False, "message": "No URL provided"}

    if not clean_url.startswith("http://") and not clean_url.startswith("https://"):
        clean_url = f"https://{clean_url}"

    url_lower = clean_url.lower()

    # 1. YouTube Ingestion
    if "youtube.com" in url_lower or "youtu.be" in url_lower:
        vid_id = extract_youtube_video_id(clean_url)
        oembed_url = f"https://www.youtube.com/oembed?url={clean_url}&format=json"
        try:
            resp = requests.get(oembed_url, timeout=8, headers={"User-Agent": USER_AGENT})
            if resp.status_code == 200:
                data = resp.json()
                title = data.get("title", "YouTube Video")
                author = data.get("author_name", "YouTube Creator")
                author_url = data.get("author_url", "")
                thumb = data.get("thumbnail_url", f"https://img.youtube.com/vi/{vid_id}/maxresdefault.jpg" if vid_id else "")
                
                embed_html = ""
                if vid_id:
                    embed_html = f'''<div class="aspect-video w-full max-w-4xl mx-auto rounded-2xl overflow-hidden shadow-2xl border border-indigo-500/20 my-8">
    <iframe class="w-full h-full" src="https://www.youtube.com/embed/{vid_id}" title="{title}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>'''

                context_summary = f"""### Source: YouTube
- **Video Title:** {title}
- **Channel / Creator:** {author}
- **Channel URL:** {author_url}
- **Video URL:** {clean_url}
- **Video ID:** {vid_id or 'N/A'}
- **Thumbnail Asset:** {thumb}
- **Embed Directive:** Embed the responsive YouTube video player directly into the hero or featured media section of the website using Video ID '{vid_id}'."""

                return {
                    "success": True,
                    "platform": "YouTube",
                    "title": title,
                    "author": author,
                    "author_url": author_url,
                    "thumbnail": thumb,
                    "video_id": vid_id,
                    "embed_code": embed_html,
                    "context_summary": context_summary,
                    "raw_url": clean_url
                }
        except Exception as e:
            pass

        # Fallback if oembed fails but video ID was parsed
        if vid_id:
            thumb = f"https://img.youtube.com/vi/{vid_id}/hqdefault.jpg"
            embed_html = f'''<div class="aspect-video w-full max-w-4xl mx-auto rounded-2xl overflow-hidden shadow-2xl border border-indigo-500/20 my-8">
    <iframe class="w-full h-full" src="https://www.youtube.com/embed/{vid_id}" title="Featured Video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>'''
            return {
                "success": True,
                "platform": "YouTube",
                "title": f"YouTube Video ({vid_id})",
                "author": "Creator",
                "author_url": clean_url,
                "thumbnail": thumb,
                "video_id": vid_id,
                "embed_code": embed_html,
                "context_summary": f"### Source: YouTube Video (ID: {vid_id})\nEmbed the video player directly using Video ID '{vid_id}' with thumbnail {thumb}.",
                "raw_url": clean_url
            }

    # 2. Instagram Ingestion
    elif "instagram.com" in url_lower:
        handle_match = re.search(r'instagram\.com\/([a-zA-Z0-9_\.]+)', clean_url)
        handle = handle_match.group(1) if handle_match else "brand"
        if handle in ["p", "reel", "stories", "tv"]:
            handle = "instagram_creator"

        title = f"@{handle} on Instagram"
        desc = ""
        img_url = ""
        try:
            resp = requests.get(clean_url, headers={"User-Agent": USER_AGENT}, timeout=8)
            if resp.status_code == 200:
                html_text = resp.text
                og_title = re.search(r'<meta property="og:title" content="([^"]+)"', html_text)
                og_desc = re.search(r'<meta property="og:description" content="([^"]+)"', html_text)
                og_img = re.search(r'<meta property="og:image" content="([^"]+)"', html_text)
                if og_title:
                    title = og_title.group(1)
                if og_desc:
                    desc = og_desc.group(1)
                if og_img:
                    img_url = og_img.group(1)
        except Exception:
            pass

        embed_widget = f'''<!-- Instagram Feed & Social Proof Showcase -->
<div class="p-6 rounded-3xl bg-gradient-to-br from-pink-500/10 via-purple-500/10 to-indigo-500/10 border border-pink-500/20 text-center my-8">
    <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-gradient-to-r from-pink-500 to-purple-600 text-white text-xs font-bold mb-4">
        <i data-lucide="instagram" class="w-4 h-4"></i> Official Instagram
    </div>
    <h3 class="text-2xl font-bold text-white mb-2">Follow @{handle}</h3>
    <p class="text-sm text-slate-300 max-w-md mx-auto mb-6">{desc or 'Join our thriving Instagram community for daily updates, exclusive BTS, and fitness tips.'}</p>
    <a href="https://instagram.com/{handle}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-pink-600 via-purple-600 to-indigo-600 hover:opacity-90 text-white font-bold text-sm shadow-lg shadow-pink-500/25 transition">
        <i data-lucide="instagram" class="w-4 h-4"></i> View on Instagram &rarr;
    </a>
</div>'''

        context_summary = f"""### Source: Instagram Profile / Post
- **Instagram Handle:** @{handle}
- **Profile / Content Title:** {title}
- **Bio / Description:** {desc or f'Official Instagram community of @{handle}'}
- **Profile Image Asset:** {img_url or 'N/A'}
- **Profile URL:** https://instagram.com/{handle}
- **Integration Directive:** Feature an interactive Instagram social proof section, follow button linking to https://instagram.com/{handle}, and showcase social highlights."""

        return {
            "success": True,
            "platform": "Instagram",
            "title": title,
            "author": f"@{handle}",
            "author_url": f"https://instagram.com/{handle}",
            "thumbnail": img_url,
            "description": desc,
            "embed_code": embed_widget,
            "context_summary": context_summary,
            "raw_url": clean_url
        }

    # 3. General Website Ingestion
    else:
        try:
            resp = requests.get(clean_url, headers={"User-Agent": USER_AGENT}, timeout=8)
            if resp.status_code == 200:
                html = resp.text
                title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
                title = title_match.group(1).strip() if title_match else clean_url

                desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', html, re.IGNORECASE)
                if not desc_match:
                    desc_match = re.search(r'<meta[^>]*property=["\']og:description["\'][^>]*content=["\'](.*?)["\']', html, re.IGNORECASE)
                desc = desc_match.group(1).strip() if desc_match else ""

                img_match = re.search(r'<meta[^>]*property=["\']og:image["\'][^>]*content=["\'](.*?)["\']', html, re.IGNORECASE)
                img_url = img_match.group(1).strip() if img_match else ""

                # Extract h1/h2 headings for business offerings
                headings = re.findall(r'<h[1-2][^>]*>(.*?)</h[1-2]>', html, re.IGNORECASE)
                cleaned_headings = [re.sub(r'<[^>]+>', '', h).strip() for h in headings[:6] if h.strip()]

                context_summary = f"""### Source: Website Reference ({clean_url})
- **Page Title:** {title}
- **Brand / Business Description:** {desc}
- **Hero Image Asset:** {img_url or 'N/A'}
- **Core Value Highlights / Headings:** {', '.join(cleaned_headings) if cleaned_headings else 'Custom Architecture'}
- **Integration Directive:** Autonomously map the extracted branding, copy style, and offerings from this source into a modern high-converting layout."""

                return {
                    "success": True,
                    "platform": "Website",
                    "title": title,
                    "description": desc,
                    "thumbnail": img_url,
                    "headings": cleaned_headings,
                    "context_summary": context_summary,
                    "raw_url": clean_url
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"Could not fetch data from link: {e}"
            }

    return {"success": False, "message": "Unsupported or unreachable link format"}
