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

def generate_og_card():
    width = 1200
    height = 630
    
    # Solid RGB canvas (Zero transparent clipping artifacts)
    bg_color = (10, 15, 29) # Slate 950 deep navy
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # 1. Subtle Background Tech Grid Lines
    grid_color = (18, 26, 47)
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)

    # 2. Tech Panel Backing (Slightly lighter dark panel to pop over the grid)
    draw.rounded_rectangle([(24, 24), (width - 24, height - 24)], radius=18, fill=(8, 12, 22), outline=(30, 41, 59), width=2)
    draw.rounded_rectangle([(28, 28), (width - 28, height - 28)], radius=15, outline=(15, 23, 42), width=1)

    # Fonts
    font_bold = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg = "C:/Windows/Fonts/segoeui.ttf"
    font_mono = "C:/Windows/Fonts/consola.ttf"

    f_top_mono = ImageFont.truetype(font_mono, 14)
    f_title = ImageFont.truetype(font_bold, 50)
    f_subtitle = ImageFont.truetype(font_bold, 22)
    f_desc = ImageFont.truetype(font_reg, 16)
    
    f_card_badge = ImageFont.truetype(font_mono, 11)
    f_card_title = ImageFont.truetype(font_bold, 17)
    f_card_sub = ImageFont.truetype(font_reg, 13)
    f_footer = ImageFont.truetype(font_mono, 13)

    # 3. Top Header Status Bar
    # Emerald pulse dot & status text
    draw.ellipse([(52, 54), (64, 66)], fill=(16, 185, 129))
    draw.text((74, 52), "PRODUCTION INFRASTRUCTURE // PHOENIX RESILIENCE MESH", font=f_top_mono, fill=(52, 211, 153))
    
    top_right_text = "MTTR: <50ms | CLOUDFLARE EDGE"
    draw.text((width - 330, 52), top_right_text, font=f_top_mono, fill=(148, 163, 184))

    # Divider line under top bar
    draw.line([(50, 80), (width - 50, 80)], fill=(30, 41, 59), width=1)

    # 4. Hero Identity Section
    draw.text((50, 108), "MOHAMMAD REHAN", font=f_title, fill=(255, 255, 255))
    draw.text((50, 175), "AI Systems Architect & Tech Lead", font=f_subtitle, fill=(56, 189, 248)) # Cyan sky
    draw.text((50, 212), "Bridging 4+ Years Real-World Retail Operations with Distributed Fault-Tolerant Engineering", font=f_desc, fill=(148, 163, 184))

    # 5. Golden Rule Axiom Banner
    axiom_box = [(50, 256), (width - 50, 316)]
    draw.rounded_rectangle(axiom_box, radius=10, fill=(15, 23, 42), outline=(99, 102, 241), width=1)
    draw.text((68, 268), "THE GOLDEN RULE OF RESILIENCE // FIRST PRINCIPLE", font=f_card_badge, fill=(129, 140, 248))
    draw.text((68, 287), '"A system should never just heal back to its old vulnerable state—every auto-heal must evolve and become permanently stronger."', font=f_card_sub, fill=(226, 232, 240))

    # 6. Three Core System Cards
    card_y1 = 338
    card_y2 = 540
    card_w = 353
    gap = 20
    start_x = 50

    cards_data = [
        {
            "badge": "FAULT TOLERANCE",
            "badge_color": (34, 211, 238), # Cyan
            "title": "Project Phoenix Engine",
            "bullets": [
                "• Sub-50ms MTTR hot process resurrection",
                "• Ash Ledger SHA-256 micro-journaling",
                "• Dynamic AST poison quarantine sandbox",
                "• Autonomous hourly background drills"
            ]
        },
        {
            "badge": "DERIVATIVES SNIPER",
            "badge_color": (52, 211, 153), # Emerald
            "title": "Indian Quant Engine (AWS)",
            "bullets": [
                "• AWS Mumbai sub-8ms exchange proximity",
                "• Spot/15m VWAP structural risk guards",
                "• 13:30 0-DTE theta shield & 30% reserve",
                "• 24/7 systemd wireguard dark mesh"
            ]
        },
        {
            "badge": "COMMERCIAL SYSTEMS",
            "badge_color": (168, 85, 247), # Purple
            "title": "Retail POS & AI Media Studio",
            "bullets": [
                "• 4+ Yrs store management (Ladies Zone)",
                "• Autonomous 9:16 vertical video studio",
                "• Offline GST billing & SQLite WAL ledger",
                "• BCA Graduate (National Business College)"
            ]
        }
    ]

    for i, c in enumerate(cards_data):
        cx1 = start_x + i * (card_w + gap)
        cx2 = cx1 + card_w
        
        # Draw card container
        draw.rounded_rectangle([(cx1, card_y1), (cx2, card_y2)], radius=12, fill=(13, 20, 36), outline=(30, 41, 59), width=1)
        
        # Badge
        draw.text((cx1 + 18, card_y1 + 16), c["badge"], font=f_card_badge, fill=c["badge_color"])
        
        # Title
        draw.text((cx1 + 18, card_y1 + 36), c["title"], font=f_card_title, fill=(248, 250, 252))
        
        # Line under card title
        draw.line([(cx1 + 18, card_y1 + 64), (cx2 - 18, card_y1 + 64)], fill=(24, 34, 53), width=1)

        # Bullet points
        by = card_y1 + 76
        for b in c["bullets"]:
            draw.text((cx1 + 18, by), b, font=f_card_sub, fill=(148, 163, 184))
            by += 25

    # 7. Bottom Footer Status Bar
    draw.line([(50, 562), (width - 50, 562)], fill=(30, 41, 59), width=1)
    draw.text((50, 580), "mohammadrehan.pages.dev", font=f_footer, fill=(56, 189, 248))
    
    footer_right = "Patna, Bihar 800006  •  Cloudflare Global Edge  •  WireGuard Dark ZTNA"
    draw.text((width - 555, 580), footer_right, font=f_footer, fill=(100, 116, 139))

    # Save image
    out_dir = Path(__file__).resolve().parent / "Deployed_Websites" / "mohammadrehan.pages.dev"
    out_path = out_dir / "og_preview.png"
    img.save(out_path, format="PNG", optimize=True)
    print(f"OpenGraph Card Generated Successfully: {out_path} ({out_path.stat().st_size:,} bytes)")

if __name__ == "__main__":
    generate_og_card()
