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

def generate_linkedin_banner():
    # LinkedIn Recommended Dimensions: 1584 x 396 px
    width = 1584
    height = 396
    
    # Deep midnight slate background
    bg_color = (10, 15, 29) # #0a0f1d
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # 1. Subtle Background Grid (Tech Architecture feel)
    grid_color = (19, 28, 50)
    for x in range(0, width, 36):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(0, height, 36):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)

    # 2. Outer tech accent frame
    draw.rounded_rectangle([(16, 16), (width - 16, height - 16)], radius=14, outline=(30, 41, 59), width=2)
    draw.rounded_rectangle([(20, 20), (width - 20, height - 20)], radius=12, outline=(15, 23, 42), width=1)

    # Load system fonts
    font_bold = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg = "C:/Windows/Fonts/segoeui.ttf"
    font_mono = "C:/Windows/Fonts/consola.ttf"

    f_badge = ImageFont.truetype(font_mono, 12)
    f_name = ImageFont.truetype(font_bold, 44)
    f_sub = ImageFont.truetype(font_bold, 20)
    f_desc = ImageFont.truetype(font_reg, 15)
    f_pill = ImageFont.truetype(font_mono, 12)
    f_url = ImageFont.truetype(font_bold, 14)

    # Left Profile Photo Safe Zone Offset (Profile avatar sits on bottom-left)
    left_x = 290 

    # 3. Top Header Status Bar
    # Emerald pulse dot & infrastructure text
    draw.ellipse([(left_x, 42), (left_x + 10, 52)], fill=(16, 185, 129))
    draw.text((left_x + 18, 40), "PRODUCTION INFRASTRUCTURE // PHOENIX RESILIENCE MESH", font=f_badge, fill=(52, 211, 153))

    top_right_info = "AWS MUMBAI (ap-south-1)  |  MTTR: <50ms  |  CLOUDFLARE EDGE"
    draw.text((width - 490, 40), top_right_info, font=f_badge, fill=(148, 163, 184))

    # Divider line
    draw.line([(left_x, 66), (width - 45, 66)], fill=(30, 41, 59), width=1)

    # 4. Main Hero Identity
    draw.text((left_x, 86), "MOHAMMAD REHAN", font=f_name, fill=(255, 255, 255))
    draw.text((left_x, 146), "AI Systems Architect & Tech Lead  •  Retail Operations Manager (4+ Yrs)", font=f_sub, fill=(56, 189, 248))
    draw.text((left_x, 180), "Bridging High-Volume Showroom Sales & Cashflow with Low-Latency Fault-Tolerant Distributed Software", font=f_desc, fill=(148, 163, 184))

    # 5. Core Architectural Highlights (3 Floating Cards)
    card_y1 = 222
    card_y2 = 330
    card_w = 385
    gap = 20
    
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
        draw.rounded_rectangle([(px1, card_y1), (px2, card_y2)], radius=10, fill=(13, 20, 36), outline=(30, 41, 59), width=1)
        
        # Tag & Title
        draw.text((px1 + 14, card_y1 + 12), p["tag"], font=f_badge, fill=p["tag_color"])
        draw.text((px1 + 14, card_y1 + 32), p["title"], font=ImageFont.truetype(font_bold, 15), fill=(248, 250, 252))
        draw.line([(px1 + 14, card_y1 + 54), (px2 - 14, card_y1 + 54)], fill=(24, 34, 53), width=1)
        draw.text((px1 + 14, card_y1 + 64), p["sub"], font=ImageFont.truetype(font_reg, 12), fill=(148, 163, 184))

    # 6. Bottom Status Line
    draw.line([(left_x, 348), (width - 45, 348)], fill=(30, 41, 59), width=1)
    
    # Portfolio Link Pill
    draw.text((left_x, 360), "Portfolio: mohammadrehan.pages.dev", font=f_url, fill=(56, 189, 248))
    
    footer_right = "Patna, Bihar 800006  •  BCA Graduate (National Business College)  •  Open for Tech Lead & Architect Roles"
    draw.text((width - 770, 362), footer_right, font=f_pill, fill=(100, 116, 139))

    # Output path
    out_dir = Path(__file__).resolve().parent / "Deployed_Websites" / "mohammadrehan.pages.dev"
    out_path = out_dir / "linkedin_banner.png"
    img.save(out_path, format="PNG", optimize=True)
    print(f"LinkedIn Banner Generated: {out_path} ({out_path.stat().st_size:,} bytes)")
    
    # Also save to Desktop for easy drag-and-drop
    desktop_path = Path("C:/Users/rehan/Desktop/linkedin_banner.png")
    img.save(desktop_path, format="PNG", optimize=True)
    print(f"Saved copy to Desktop: {desktop_path}")

if __name__ == "__main__":
    generate_linkedin_banner()
