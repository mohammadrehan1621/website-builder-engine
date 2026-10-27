import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = Path(r"C:\Users\rehan\Desktop\RQL_Product_Showcase_Images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1920
HEIGHT = 1080

FONTS = {
    "title": ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 52),
    "subtitle": ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 26),
    "badge": ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 20),
    "metric_val": ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 46),
    "metric_lbl": ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 18),
    "metric_sub": ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 16),
    "term_title": ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 20),
    "term_code": ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 22),
    "footer": ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 22),
    "footer_bold": ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22),
}

def create_base_canvas(accent_color, bg_gradient_end):
    img = Image.new("RGBA", (WIDTH, HEIGHT), (2, 6, 23, 255)) # slate-950
    draw = ImageDraw.Draw(img)

    # Subtle radial or vertical gradient
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(2 + (bg_gradient_end[0] - 2) * ratio)
        g = int(6 + (bg_gradient_end[1] - 6) * ratio)
        b = int(23 + (bg_gradient_end[2] - 23) * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b, 255))

    # Grid background dots/lines
    grid_spacing = 60
    for x in range(0, WIDTH, grid_spacing):
        for y in range(0, HEIGHT, grid_spacing):
            draw.rectangle([x, y, x+1, y+1], fill=(255, 255, 255, 12))

    # Outer border
    draw.rectangle([12, 12, WIDTH - 13, HEIGHT - 13], outline=(40, 50, 70, 255), width=2)
    # Accent top highlight line
    draw.line([(14, 14), (WIDTH - 15, 14)], fill=accent_color, width=4)

    return img, draw

def render_kernel_image():
    accent = (16, 185, 129, 255) # emerald-500
    accent_dim = (5, 150, 105, 180)
    bg_end = (6, 30, 22)
    img, draw = create_base_canvas(accent, bg_end)

    # Top brand bar
    draw.text((80, 50), "REHAN QUANT LAB  //  SOVEREIGN ARCHITECTURE SUITE", fill=(148, 163, 184), font=FONTS["badge"])
    
    # Version Badge
    draw.rounded_rectangle([WIDTH - 380, 42, WIDTH - 80, 84], radius=8, fill=(6, 78, 59, 150), outline=accent, width=1)
    draw.text((WIDTH - 360, 52), "v1.0 PROD  •  100% AIR-GAPPED", fill=accent, font=FONTS["badge"])

    # Title & Subtitle
    draw.text((80, 105), "Deterministic State Kernel™", fill=(255, 255, 255), font=FONTS["title"])
    draw.text((80, 175), "Bare-Metal Sub-Microsecond State Machine & Cryptographic Write-Ahead Logger", fill=(203, 213, 225), font=FONTS["subtitle"])

    # 4 Metric Cards
    metrics = [
        {"val": "604 ns", "lbl": "CACHED READ LATENCY", "sub": "Direct C-ABI memory-mapped read"},
        {"val": "246,120", "lbl": "WRITES / SECOND", "sub": "4.69μs group commit batching"},
        {"val": "76.99 ms", "lbl": "COLD CRASH REPLAY", "sub": "25,000 frames from SHA-256 log"},
        {"val": "MCA 11(g)", "lbl": "STATUTORY AUDIT LOG", "sub": "Tamper-evident append-only ledger"}
    ]

    card_w = 410
    card_h = 160
    card_y = 235
    spacing = 26
    start_x = 80

    for i, m in enumerate(metrics):
        x = start_x + i * (card_w + spacing)
        # Card background
        draw.rounded_rectangle([x, card_y, x + card_w, card_y + card_h], radius=14, fill=(15, 23, 42, 230), outline=(51, 65, 85, 200), width=1)
        # Left accent pip
        draw.rounded_rectangle([x, card_y + 16, x + 5, card_y + card_h - 16], radius=2, fill=accent)
        # Value
        draw.text((x + 25, card_y + 22), m["val"], fill=accent, font=FONTS["metric_val"])
        # Label
        draw.text((x + 25, card_y + 85), m["lbl"], fill=(255, 255, 255), font=FONTS["metric_lbl"])
        # Subtitle
        draw.text((x + 25, card_y + 115), m["sub"], fill=(148, 163, 184), font=FONTS["metric_sub"])

    # Terminal / Code Execution Frame
    term_x = 80
    term_y = 435
    term_w = WIDTH - 160
    term_h = 515

    draw.rounded_rectangle([term_x, term_y, term_x + term_w, term_y + term_h], radius=14, fill=(9, 13, 24, 250), outline=(30, 41, 59, 255), width=2)
    # Terminal header bar
    draw.rounded_rectangle([term_x, term_y, term_x + term_w, term_y + 48], radius=12, fill=(15, 23, 42, 255))
    # Window buttons
    draw.ellipse([term_x + 20, term_y + 18, term_x + 32, term_y + 30], fill=(239, 68, 68))
    draw.ellipse([term_x + 42, term_y + 18, term_x + 54, term_y + 30], fill=(245, 158, 11))
    draw.ellipse([term_x + 64, term_y + 18, term_x + 76, term_y + 30], fill=(16, 185, 129))
    draw.text((term_x + 95, term_y + 14), "DSE Core Kernel Terminal — [dse_core.dll // dse-kernel-cli.exe]", fill=(148, 163, 184), font=FONTS["term_title"])

    # Terminal logs
    logs = [
        ("> Initializing Deterministic State Kernel v1.0 [Architecture: x86_64-pc-windows-msvc]", (148, 163, 184)),
        ("[SYSTEM] Binding memory-mapped ring buffer: 64 MB locked non-swappable physical RAM", (203, 213, 225)),
        ("[DSE_CORE] Shared C-ABI library linked: dse_core.dll (Exported symbols: 14/14)", accent),
        ("[BENCHMARK] Sequential Read Latency: 604 ns (0.604 μs) — L1/L2 cache residency confirmed", (255, 255, 255)),
        ("[BENCHMARK] Batch Commit Throughput: 246,120 state mutations/sec | Group Commit MTTR: 4.69 μs", (255, 255, 255)),
        ("[WAL_ENGINE] SHA-256 Hardware Checksum verified: 0x8F3D1C44... [Monotonic Frame Seq: #25000]", (56, 189, 248)),
        ("[CRASH_REPLAY] Simulating sudden SIGKILL... Cold recovery executed in 76.99 ms (Zero state loss)", (250, 204, 21)),
        ("[INVARIANTS] 22 / 22 Adversarial Invariant Gates Certified: PASSED (100.0% Green)", accent),
        ("[SECURITY] Outbound network egress: BLOCKED (0 bytes transmitted) • 100% Air-Gapped", (244, 63, 94)),
        ("[STATUS] Kernel ready for institutional HFT execution, broker risk middleware, and statutory ledgering.", (148, 163, 184))
    ]

    log_y = term_y + 70
    for line, color in logs:
        draw.text((term_x + 30, log_y), line, fill=color, font=FONTS["term_code"])
        log_y += 42

    # Bottom Footer Bar
    draw.text((80, HEIGHT - 75), "STANDALONE NATIVE WINDOWS BINARY (.EXE)", fill=accent, font=FONTS["footer_bold"])
    draw.text((540, HEIGHT - 75), "•  Zero Python Runtime Needed  •  Hardware Machine-Locked EULA  •  199 Invariant Gates Passed", fill=(148, 163, 184), font=FONTS["footer"])
    draw.text((WIDTH - 370, HEIGHT - 75), "https://rehanquantlab.com", fill=(203, 213, 225), font=FONTS["footer_bold"])

    out_file = OUTPUT_DIR / "01_deterministic_state_kernel_1080p.png"
    img.save(out_file, "PNG")
    print("Generated:", out_file)

def render_aegis_image():
    accent = (6, 182, 212, 255) # cyan-500
    bg_end = (8, 30, 40)
    img, draw = create_base_canvas(accent, bg_end)

    # Top brand bar
    draw.text((80, 50), "REHAN QUANT LAB  //  SOVEREIGN TRADING DEFENSE", fill=(148, 163, 184), font=FONTS["badge"])
    
    # Version Badge
    draw.rounded_rectangle([WIDTH - 380, 42, WIDTH - 80, 84], radius=8, fill=(8, 51, 68, 150), outline=accent, width=1)
    draw.text((WIDTH - 360, 52), "v1.0 PROD  •  100% AIR-GAPPED", fill=accent, font=FONTS["badge"])

    # Title & Subtitle
    draw.text((80, 105), "RQL Aegis™ Risk Middleware", fill=(255, 255, 255), font=FONTS["title"])
    draw.text((80, 175), "Deterministic On-Premises Trading Risk Engine with Continuous Volatility Clamping", fill=(203, 213, 225), font=FONTS["subtitle"])

    # 4 Metric Cards
    metrics = [
        {"val": "< 0.35 ms", "lbl": "IPC GATING LATENCY", "sub": "Sub-millisecond order intercept"},
        {"val": "σ-Adaptive", "lbl": "VOLATILITY CLAMP", "sub": "Inverse variance position sizing"},
        {"val": "< 60 μs", "lbl": "EMERGENCY BRAKE", "sub": "Atomic memory latch execution"},
        {"val": "Zero Egress", "lbl": "NETWORK PRIVACY", "sub": "100% local workstation execution"}
    ]

    card_w = 410
    card_h = 160
    card_y = 235
    spacing = 26
    start_x = 80

    for i, m in enumerate(metrics):
        x = start_x + i * (card_w + spacing)
        draw.rounded_rectangle([x, card_y, x + card_w, card_y + card_h], radius=14, fill=(15, 23, 42, 230), outline=(51, 65, 85, 200), width=1)
        draw.rounded_rectangle([x, card_y + 16, x + 5, card_y + card_h - 16], radius=2, fill=accent)
        draw.text((x + 25, card_y + 22), m["val"], fill=accent, font=FONTS["metric_val"])
        draw.text((x + 25, card_y + 85), m["lbl"], fill=(255, 255, 255), font=FONTS["metric_lbl"])
        draw.text((x + 25, card_y + 115), m["sub"], fill=(148, 163, 184), font=FONTS["metric_sub"])

    # Terminal Frame
    term_x = 80
    term_y = 435
    term_w = WIDTH - 160
    term_h = 515

    draw.rounded_rectangle([term_x, term_y, term_x + term_w, term_y + term_h], radius=14, fill=(9, 13, 24, 250), outline=(30, 41, 59, 255), width=2)
    draw.rounded_rectangle([term_x, term_y, term_x + term_w, term_y + 48], radius=12, fill=(15, 23, 42, 255))
    draw.ellipse([term_x + 20, term_y + 18, term_x + 32, term_y + 30], fill=(239, 68, 68))
    draw.ellipse([term_x + 42, term_y + 18, term_x + 54, term_y + 30], fill=(245, 158, 11))
    draw.ellipse([term_x + 64, term_y + 18, term_x + 76, term_y + 30], fill=(16, 185, 129))
    draw.text((term_x + 95, term_y + 14), "Aegis Daemon Console — [Interactive Brokers / Zerodha / Dhan / Fyers]", fill=(148, 163, 184), font=FONTS["term_title"])

    logs = [
        ("> Starting RQL Aegis™ Risk Supervisor Daemon v1.0 [Process ID: 4180]", (148, 163, 184)),
        ("[HOOK] Intercepting order routing pipelines: Zerodha Kite, IBKR TWS, Dhan API", (203, 213, 225)),
        ("[VOLATILITY] Instantaneous Realized Volatility: σ = 2.41% (Threshold: 1.80%)", (250, 204, 21)),
        ("[CLAMP_ENGAGED] Volatility scale factor: 0.747x | Dynamically scaling max lot size to 74%", accent),
        ("[CAPITAL_LOCK] Non-negotiable cash reserve: 30.0% untouchable margin locked in memory", (255, 255, 255)),
        ("[SIMULATED_SHOCK] Injecting +4σ flash crash order burst (1,200 orders in 50ms)...", (244, 63, 94)),
        ("[INVARIANT_GATE] Rejecting 410 over-leveraged orders | Pre-trade risk check latency: 0.31 ms", accent),
        ("[HANDBRAKE_TEST] ManualEmergencyBrake.exe triggered: Memory latch set in 58 μs", (239, 68, 68)),
        ("[RECOVERY] All live exchange sockets severed, WAL synced, state immutable on disk.", (56, 189, 248)),
        ("[CERTIFIED] 199 / 199 System-Wide Invariant Tests: 100.0% GREEN", (16, 185, 129))
    ]

    log_y = term_y + 70
    for line, color in logs:
        draw.text((term_x + 30, log_y), line, fill=color, font=FONTS["term_code"])
        log_y += 42

    draw.text((80, HEIGHT - 75), "STANDALONE WINDOWS RISK DAEMON (.EXE)", fill=accent, font=FONTS["footer_bold"])
    draw.text((540, HEIGHT - 75), "•  Hardware SHA-256 Audit Trail  •  Pay Once, Own Forever  •  Zero Cloud Leakage", fill=(148, 163, 184), font=FONTS["footer"])
    draw.text((WIDTH - 370, HEIGHT - 75), "https://rehanquantlab.com", fill=(203, 213, 225), font=FONTS["footer_bold"])

    out_file = OUTPUT_DIR / "02_rql_aegis_risk_middleware_1080p.png"
    img.save(out_file, "PNG")
    print("Generated:", out_file)

def render_veritas_image():
    accent = (168, 85, 247, 255) # purple-500
    bg_end = (30, 15, 45)
    img, draw = create_base_canvas(accent, bg_end)

    # Top brand bar
    draw.text((80, 50), "REHAN QUANT LAB  //  FORENSIC FINANCIAL AUDITING", fill=(148, 163, 184), font=FONTS["badge"])
    
    # Version Badge
    draw.rounded_rectangle([WIDTH - 380, 42, WIDTH - 80, 84], radius=8, fill=(88, 28, 135, 150), outline=accent, width=1)
    draw.text((WIDTH - 360, 52), "v1.0 PROD  •  100% AIR-GAPPED", fill=accent, font=FONTS["badge"])

    # Title & Subtitle
    draw.text((80, 105), "Veritas Dossier™ Forensic Auditor", fill=(255, 255, 255), font=FONTS["title"])
    draw.text((80, 175), "Air-Gapped Private SEBI DRHP Prospectus & Capital Dilution Audit Engine", fill=(203, 213, 225), font=FONTS["subtitle"])

    # 4 Metric Cards
    metrics = [
        {"val": "BVPS Bridge", "lbl": "DILUTION FORMULATION", "sub": "Exact post-issue mathematical delta"},
        {"val": "OFS vs Fresh", "lbl": "CASH DRAIN ISOLATION", "sub": "Promoter cash-out vs growth capex"},
        {"val": "Pledge Scan", "lbl": "PROMOTER ENCUMBRANCE", "sub": "Footnote RPT & debt covenant audit"},
        {"val": "Strict NDA", "lbl": "100% AIR-GAPPED COMPLIANCE", "sub": "Zero public cloud doc uploads"}
    ]

    card_w = 410
    card_h = 160
    card_y = 235
    spacing = 26
    start_x = 80

    for i, m in enumerate(metrics):
        x = start_x + i * (card_w + spacing)
        draw.rounded_rectangle([x, card_y, x + card_w, card_y + card_h], radius=14, fill=(15, 23, 42, 230), outline=(51, 65, 85, 200), width=1)
        draw.rounded_rectangle([x, card_y + 16, x + 5, card_y + card_h - 16], radius=2, fill=accent)
        draw.text((x + 25, card_y + 22), m["val"], fill=accent, font=FONTS["metric_val"])
        draw.text((x + 25, card_y + 85), m["lbl"], fill=(255, 255, 255), font=FONTS["metric_lbl"])
        draw.text((x + 25, card_y + 115), m["sub"], fill=(148, 163, 184), font=FONTS["metric_sub"])

    # Terminal Frame
    term_x = 80
    term_y = 435
    term_w = WIDTH - 160
    term_h = 515

    draw.rounded_rectangle([term_x, term_y, term_x + term_w, term_y + term_h], radius=14, fill=(9, 13, 24, 250), outline=(30, 41, 59, 255), width=2)
    draw.rounded_rectangle([term_x, term_y, term_x + term_w, term_y + 48], radius=12, fill=(15, 23, 42, 255))
    draw.ellipse([term_x + 20, term_y + 18, term_x + 32, term_y + 30], fill=(239, 68, 68))
    draw.ellipse([term_x + 42, term_y + 18, term_x + 54, term_y + 30], fill=(245, 158, 11))
    draw.ellipse([term_x + 64, term_y + 18, term_x + 76, term_y + 30], fill=(16, 185, 129))
    draw.text((term_x + 95, term_y + 14), "Veritas Dossier Forensic Engine — [Offline Intranet Audit Console]", fill=(148, 163, 184), font=FONTS["term_title"])

    logs = [
        ("> Ingesting Draft Red Herring Prospectus (DRHP) PDF [542 Pages, File Size: 18.4 MB]", (148, 163, 184)),
        ("[OFFLINE_PARSER] Extracting Capital Structure, Shareholding Pattern, and Financial Annexures...", (203, 213, 225)),
        ("[DILUTION_BRIDGE] Pre-Issue Shares: 45,000,000 | Fresh Equity Issue: 15,000,000 @ ₹180/share", (255, 255, 255)),
        ("[DILUTION_BRIDGE] Pre-Issue BVPS: ₹68.40  -->  Post-Issue Diluted BVPS: ₹96.30 (+40.8%)", accent),
        ("[OFFER_FOR_SALE] OFS Size: ₹450 Cr (Promoter cash-out: 62.5% of total IPO proceeds)", (244, 63, 94)),
        ("[FORENSIC_ALERT] Related Party Note 34: ₹85 Cr unsecured loan extended to promoter entity", (250, 204, 21)),
        ("[PLEDGE_SCANNER] Promoter Equity Encumbrance: 41.2% shares pledged to non-banking lenders", (239, 68, 68)),
        ("[SECURITY_AUDIT] Outbound Network Telemetry: 0 BYTES (Air-Gapped Private Execution)", (16, 185, 129)),
        ("[DOSSIER_EXPORT] Full Forensic Dilution Audit Sheet generated: veritas_dossier_report.pdf", (56, 189, 248)),
        ("[STATUS] Complete institutional compliance for Chartered Accountants & M&A Advisors.", (148, 163, 184))
    ]

    log_y = term_y + 70
    for line, color in logs:
        draw.text((term_x + 30, log_y), line, fill=color, font=FONTS["term_code"])
        log_y += 42

    draw.text((80, HEIGHT - 75), "STANDALONE FORENSIC AUDITOR (.EXE)", fill=accent, font=FONTS["footer_bold"])
    draw.text((540, HEIGHT - 75), "•  Zero SaaS Subscriptions  •  Client NDA Immunity  •  Perpetual Hardware License", fill=(148, 163, 184), font=FONTS["footer"])
    draw.text((WIDTH - 370, HEIGHT - 75), "https://rehanquantlab.com", fill=(203, 213, 225), font=FONTS["footer_bold"])

    out_file = OUTPUT_DIR / "03_veritas_dossier_audit_engine_1080p.png"
    img.save(out_file, "PNG")
    print("Generated:", out_file)

def render_sentinel_image():
    accent = (245, 158, 11, 255) # amber-500
    bg_end = (35, 25, 8)
    img, draw = create_base_canvas(accent, bg_end)

    # Top brand bar
    draw.text((80, 50), "REHAN QUANT LAB  //  INDUSTRIAL RESILIENCE & TELEMETRY", fill=(148, 163, 184), font=FONTS["badge"])
    
    # Version Badge
    draw.rounded_rectangle([WIDTH - 380, 42, WIDTH - 80, 84], radius=8, fill=(120, 53, 15, 150), outline=accent, width=1)
    draw.text((WIDTH - 360, 52), "v1.0 PROD  •  100% AIR-GAPPED", fill=accent, font=FONTS["badge"])

    # Title & Subtitle
    draw.text((80, 105), "Industrial Fragility Sentinel™", fill=(255, 255, 255), font=FONTS["title"])
    draw.text((80, 175), "On-Premises Shop Floor Uptime & Single-Source Supply Chain Chokepoint Daemon", fill=(203, 213, 225), font=FONTS["subtitle"])

    # 4 Metric Cards
    metrics = [
        {"val": "Fragility Index", "lbl": "SUN TZU 5-FACTOR SCORE", "sub": "Real-time plant vulnerability (0-100)"},
        {"val": "> 50% Threshold", "lbl": "SUPPLY CHOKEPOINT", "sub": "Early single-vendor stockout alarm"},
        {"val": "14.5 Hours", "lbl": "GENERATOR RUNWAY", "sub": "Continuous captive power telemetry"},
        {"val": "Zero Cloud", "lbl": "SHOP FLOOR HARDWARE LOCK", "sub": "Zero leak of proprietary formulas"}
    ]

    card_w = 410
    card_h = 160
    card_y = 235
    spacing = 26
    start_x = 80

    for i, m in enumerate(metrics):
        x = start_x + i * (card_w + spacing)
        draw.rounded_rectangle([x, card_y, x + card_w, card_y + card_h], radius=14, fill=(15, 23, 42, 230), outline=(51, 65, 85, 200), width=1)
        draw.rounded_rectangle([x, card_y + 16, x + 5, card_y + card_h - 16], radius=2, fill=accent)
        draw.text((x + 25, card_y + 22), m["val"], fill=accent, font=FONTS["metric_val"])
        draw.text((x + 25, card_y + 85), m["lbl"], fill=(255, 255, 255), font=FONTS["metric_lbl"])
        draw.text((x + 25, card_y + 115), m["sub"], fill=(148, 163, 184), font=FONTS["metric_sub"])

    # Terminal Frame
    term_x = 80
    term_y = 435
    term_w = WIDTH - 160
    term_h = 515

    draw.rounded_rectangle([term_x, term_y, term_x + term_w, term_y + term_h], radius=14, fill=(9, 13, 24, 250), outline=(30, 41, 59, 255), width=2)
    draw.rounded_rectangle([term_x, term_y, term_x + term_w, term_y + 48], radius=12, fill=(15, 23, 42, 255))
    draw.ellipse([term_x + 20, term_y + 18, term_x + 32, term_y + 30], fill=(239, 68, 68))
    draw.ellipse([term_x + 42, term_y + 18, term_x + 54, term_y + 30], fill=(245, 158, 11))
    draw.ellipse([term_x + 64, term_y + 18, term_x + 76, term_y + 30], fill=(16, 185, 129))
    draw.text((term_x + 95, term_y + 14), "Industrial Sentinel Telemetry Daemon — [Manufacturing Plant Gateway]", fill=(148, 163, 184), font=FONTS["term_title"])

    logs = [
        ("> Initializing Industrial Fragility Sentinel v1.0 [Shop Floor Daemon]", (148, 163, 184)),
        ("[CONFIG] Loaded factory profile: Auto Ancillary & Precision Machining Unit", (203, 213, 225)),
        ("[GRID_MONITOR] State Power Grid Status: NOMINAL (Voltage: 415V, Frequency: 50.02 Hz)", (16, 185, 129)),
        ("[CAPTIVE_POWER] Diesel Generator Fuel Capacity: 82.4% | Fuel Runway: 14.5 hours @ 450 kW load", (255, 255, 255)),
        ("[SUPPLY_SCANNER] Monitoring 12 tier-1 raw material suppliers across 4 corridors...", (56, 189, 248)),
        ("[CHOKEPOINT_DETECTED] Component X-40 alloy single-source concentration at 64.2% (> 50% limit)", (244, 63, 94)),
        ("[SUN_TZU_SCORE] Operational Fragility Index: 42 / 100 (Robust Armor with elevated buffer strain)", accent),
        ("[ALARM_DISPATCH] Sub-microsecond local alert dispatched to plant manager console (Zero cloud)", (250, 204, 21)),
        ("[HARDWARE_LOCK] License bound to physical plant controller MAC: D4-5D-64-8F-11-2B", (148, 163, 184)),
        ("[STATUS] 24/7 shop floor protection active. Zero monthly SaaS subscriptions.", (16, 185, 129))
    ]

    log_y = term_y + 70
    for line, color in logs:
        draw.text((term_x + 30, log_y), line, fill=color, font=FONTS["term_code"])
        log_y += 42

    draw.text((80, HEIGHT - 75), "STANDALONE INDUSTRIAL PLANT DAEMON (.EXE)", fill=accent, font=FONTS["footer_bold"])
    draw.text((540, HEIGHT - 75), "•  Zero Cloud Data Leakage  •  Pay Once, Protect Forever  •  Sun Tzu Asymmetry Engine", fill=(148, 163, 184), font=FONTS["footer"])
    draw.text((WIDTH - 370, HEIGHT - 75), "https://rehanquantlab.com", fill=(203, 213, 225), font=FONTS["footer_bold"])

    out_file = OUTPUT_DIR / "04_industrial_fragility_sentinel_1080p.png"
    img.save(out_file, "PNG")
    print("Generated:", out_file)

if __name__ == "__main__":
    render_kernel_image()
    render_aegis_image()
    render_veritas_image()
    render_sentinel_image()
