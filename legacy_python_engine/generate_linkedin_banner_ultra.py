import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

def generate_ultra_linkedin_banner():
    # 2.5x Ultra-High Definition Scale (3960 x 990 px)
    # Native 4:1 aspect ratio matching LinkedIn, ultra-sharp on 4K/Retina displays
    scale = 2.5
    width = int(1584 * scale)   # 3960 px
    height = int(396 * scale)   # 990 px
    
    # Deep midnight slate background
    bg_color = (10, 15, 29) # #0a0f1d
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # 1. Subtle Background Tech Grid Lines
    grid_color = (19, 28, 50)
    grid_step = int(36 * scale) # 90 px
    for x in range(0, width, grid_step):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=2)
    for y in range(0, height, grid_step):
        draw.line([(0, y), (width, y)], fill=grid_color, width=2)

    # 2. Outer tech accent frame
    m1 = int(16 * scale)
    m2 = int(20 * scale)
    draw.rounded_rectangle([(m1, m1), (width - m1, height - m1)], radius=int(14 * scale), outline=(30, 41, 59), width=3)
    draw.rounded_rectangle([(m2, m2), (width - m2, height - m2)], radius=int(12 * scale), outline=(15, 23, 42), width=2)

    # Load system fonts with ultra-scaled pt sizes
    font_bold = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg = "C:/Windows/Fonts/segoeui.ttf"
    font_mono = "C:/Windows/Fonts/consola.ttf"

    f_top_mono = ImageFont.truetype(font_mono, int(12 * scale))
    f_name = ImageFont.truetype(font_bold, int(44 * scale))
    f_sub = ImageFont.truetype(font_bold, int(20 * scale))
    f_desc = ImageFont.truetype(font_reg, int(15 * scale))
    
    f_badge = ImageFont.truetype(font_mono, int(12 * scale))
    f_card_title = ImageFont.truetype(font_bold, int(15 * scale))
    f_card_sub = ImageFont.truetype(font_reg, int(12 * scale))
    f_url = ImageFont.truetype(font_bold, int(14 * scale))
    f_footer_right = ImageFont.truetype(font_mono, int(12 * scale))

    # Left Profile Photo Safe Zone Offset
    left_x = int(290 * scale) # 725 px

    # 3. Top Header Status Bar
    # Emerald pulse dot & infrastructure text
    dot_x = left_x
    dot_y = int(42 * scale)
    dot_r = int(6 * scale)
    draw.ellipse([(dot_x, dot_y), (dot_x + dot_r * 2, dot_y + dot_r * 2)], fill=(16, 185, 129))
    draw.text((dot_x + int(18 * scale), int(39 * scale)), "PRODUCTION INFRASTRUCTURE // PHOENIX RESILIENCE MESH", font=f_top_mono, fill=(52, 211, 153))

    top_right_info = "AWS MUMBAI (ap-south-1)  |  MTTR: <50ms  |  CLOUDFLARE EDGE"
    draw.text((width - int(480 * scale), int(39 * scale)), top_right_info, font=f_top_mono, fill=(148, 163, 184))

    # Divider line under top bar
    draw.line([(left_x, int(66 * scale)), (width - int(45 * scale), int(66 * scale))], fill=(30, 41, 59), width=2)

    # 4. Main Hero Identity
    draw.text((left_x, int(84 * scale)), "MOHAMMAD REHAN", font=f_name, fill=(255, 255, 255))
    draw.text((left_x, int(145 * scale)), "AI Systems Architect & Tech Lead  •  Retail Operations Manager (4+ Yrs)", font=f_sub, fill=(56, 189, 248))
    draw.text((left_x, int(180 * scale)), "Bridging High-Volume Showroom Sales & Cashflow with Low-Latency Fault-Tolerant Distributed Software", font=f_desc, fill=(148, 163, 184))

    # 5. Core Architectural Highlights (3 Floating Cards)
    card_y1 = int(220 * scale)
    card_y2 = int(328 * scale)
    card_w = int(385 * scale)
    gap = int(20 * scale)
    
    pillars = [
        {
            "tag": "DERIVATIVES SNIPER",
            "tag_color": (52, 211, 153),
            "title": "Indian Options Sniper (AWS)",
            "sub": "Sub-8ms proximity • Spot/VWAP risk guard • 0-DTE theta filter"
        },
        {
            "tag": "FAULT TOLERANCE",
            "tag_color": (34, 211, 238),
            "title": "Project Phoenix Engine",
            "sub": "Sub-50ms MTTR • Ash Ledger WAL • Antifragile Golden Rule"
        },
        {
            "tag": "COMMERCIAL SYSTEMS",
            "tag_color": (168, 85, 247),
            "title": "Retail Operations & Media",
            "sub": "4+ Yrs store management • Custom POS • Autonomous AI video studio"
        }
    ]

    for i, p in enumerate(pillars):
        px1 = left_x + i * (card_w + gap)
        px2 = px1 + card_w
        
        # Draw card container
        draw.rounded_rectangle([(px1, card_y1), (px2, card_y2)], radius=int(10 * scale), fill=(13, 20, 36), outline=(30, 41, 59), width=2)
        
        # Tag & Title
        draw.text((px1 + int(14 * scale), card_y1 + int(12 * scale)), p["tag"], font=f_badge, fill=p["tag_color"])
        draw.text((px1 + int(14 * scale), card_y1 + int(32 * scale)), p["title"], font=f_card_title, fill=(248, 250, 252))
        draw.line([(px1 + int(14 * scale), card_y1 + int(54 * scale)), (px2 - int(14 * scale), card_y1 + int(54 * scale))], fill=(24, 34, 53), width=2)
        draw.text((px1 + int(14 * scale), card_y1 + int(64 * scale)), p["sub"], font=f_card_sub, fill=(148, 163, 184))

    # 6. Bottom Status Line
    draw.line([(left_x, int(346 * scale)), (width - int(45 * scale), int(346 * scale))], fill=(30, 41, 59), width=2)
    
    # Portfolio Link Pill
    draw.text((left_x, int(358 * scale)), "Portfolio: mohammadrehan.pages.dev", font=f_url, fill=(56, 189, 248))
    
    footer_right = "Patna, Bihar 800006  •  BCA Graduate (National Business College)  •  Open for Tech Lead & Architect Roles"
    draw.text((width - int(765 * scale), int(360 * scale)), footer_right, font=f_footer_right, fill=(100, 116, 139))

    # Output paths
    desktop_path = Path("C:/Users/rehan/Desktop/linkedin_banner.png")
    img.save(desktop_path, format="PNG", optimize=True)
    print(f"Saved 4K Ultra-Resolution Banner to Desktop: {desktop_path} ({width}x{height} px, {desktop_path.stat().st_size:,} bytes)")

    out_dir = Path(__file__).resolve().parent / "Deployed_Websites" / "mohammadrehan.pages.dev"
    out_path = out_dir / "linkedin_banner.png"
    img.save(out_path, format="PNG", optimize=True)
    print(f"Saved copy in portfolio dir: {out_path}")

if __name__ == "__main__":
    generate_ultra_linkedin_banner()
