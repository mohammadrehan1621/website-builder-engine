import sys
from pathlib import Path
from pdf_generator import create_styled_resume_pdf

# Configure Windows UTF-8 stdout
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent
PORTFOLIO_DIR = BASE_DIR / "Deployed_Websites" / "mohammadrehan.pages.dev"
PDF_PATH = PORTFOLIO_DIR / "Mohammad_Rehan_Resume.pdf"

resume_md = """
## Executive Summary
High-impact Software Architect and Operations Leader with 4+ years of hands-on experience bridging commercial enterprise operations and fault-tolerant distributed systems. Architect of The Holy Trinity: Aegis, Chaos, Phoenix (autonomous antifragile resilience framework), institutional-grade algorithmic trading systems with zero capital leakage, and commercial enterprise POS architectures.

## Core Competencies & Architecture Stack
- **The Holy Trinity Resilience Framework**: Aegis (Predictive Immunity, AST Poison Quarantine, WireGuard ZTNA, 35% Risk Drawdown Ceiling), Chaos (Level-5 Doomsday Gauntlet, 50-Thread Concurrent Stampedes, 800MB Heap Shockwaves, 100% Defense Certification), Phoenix (Ash Ledger WAL Micro-Journaling, Sub-50ms MTTR Hot Process Resurrection, EvolutionaryHardener Epoch Progression).
- **Distributed Systems & Fault Tolerance**: Write-Ahead Logging (WAL) Micro-Journaling, Continuous Chaos Engineering, Sub-50ms Process Supervision, Dynamic AST Poison Quarantine, Multi-State Circuit Breakers.
- **FinTech & Algorithmic Trading**: Low-latency multi-agent derivatives execution (NSE NIFTY/BANKNIFTY), Spot/15m VWAP structural stop-loss guards, 0-DTE theta decay shields, sub-8ms exchange proximity.
- **Full-Stack & POS Development**: Python 3.12, AsyncIO, SQLite, Streamlit, HTML5/CSS3, Modern JavaScript, Thermal Printer Protocol, ReportLab PDF Engine.
- **Cloud Infrastructure & Security**: AWS Mumbai (ap-south-1), Cloudflare Pages Edge, Zero-Trust Network Access (ZTNA) via Private WireGuard Mesh, Linux systemd real-time priority tuning (Nice=-10).

## Key Production Systems & Architectures

### The Holy Trinity: Aegis • Chaos • Phoenix — Autonomous Antifragile Resilience Framework & Sentinel
- Architected an institutional-grade, 5-step closed-loop antifragile lifecycle enforcing the Golden Rule of Resilience: auto-healing into a permanently evolved, hardened state.
- **Step 1 (Aegis Pre-Audit)**: Static AST contract and reflection audit scanning codebase to guarantee zero syntax traps, zero unpacking mismatches (validate_order), and precision floor quantization.
- **Step 2 (Chaos Gauntlet)**: Continuous adversarial shock engine bombarding nodes with 8 real exchange disasters (WebSocket severing, Binance HTTP 429 rate-limit spikes, -5% flash crashes, SQLite lock contention, toxic wicks).
- **Step 3 (Phoenix & Antifragile Evolution)**: Sub-500ms auto-heal with $0.00 capital impact, triggering Genomic Generation advancement (+25% adaptive parameter stiffening, Gen 1 -> Gen 2) and elevated Immunity Score.
- **Step 4 (Aegis Post-Audit)**: Mathematical re-verification guaranteeing zero precision drift, zero race conditions, and 100% wallet profit retention.
- **Step 5 (Perpetual Hardening)**: Continuous closed-loop iteration resulting in titanium immunity against unforeseen exchange and runtime anomalies.

### Indian Quant Options Sniper — Institutional Derivatives Execution Engine
- Engineered an institutional-grade, multi-agent algorithmic options execution engine deployed on AWS Mumbai (ap-south-1) with sub-8ms deterministic fiber proximity to NSE co-location.
- Implemented single direct atomic routing for <=24 lots (390 NIFTY qty), eliminating retail double-brokerage penalties and 500ms market-maker front-running lag.
- Anchored dynamic stop-loss to NIFTY Spot 15m VWAP structure rather than option premium noise, backed by a 35% emergency disaster ceiling and a 30% capital reserve lock.
- Automated a 13:30 IST Expiry Day Theta Filter to eliminate 0-DTE time decay slaughter, automatically routing breakout momentum to next-week contracts.
- Secured live operations under 24/7 systemd autopilot (0.00 load average, 2GB swap protection) isolated behind an encrypted private WireGuard mesh (ZTNA).

### Autonomous Video & Content Studio — Multi-Modal Programmatic Engine
- Developed an end-to-end automated vertical video (9:16) production studio combining topic-to-script agent workflows, studio neural voiceover, and dynamic B-roll synchronization.
- Engineered a custom ASS subtitle engine compiling word-by-word colored animated subtitle cues (Hormozi style) with automatic background audio ducking.
- Fortified rendering pipeline with Phoenix process supervision, preventing FFmpeg memory leaks and out-of-memory crashes during batch renders.
- Autonomously outputs ready-to-publish 1080x1920 Full HD video packages complete with high-CTR titles, SEO descriptions, and tags.

### Footwear Retail POS & Executive Sales Dashboard
- Built a commercial Point of Sale (POS) and inventory ledger managing retail store operations, barcode scanning, thermal printing, and GST compliance.
- Features multi-counter concurrency protection, inventory reorder forecasting, and real-time sales margin dashboards.

### Maison Ladies Zone — Haute Couture Digital Showcase
- Architected a luxury digital showroom platform (ladieszonepatna.in) with appointment trial concierge workflows, client-side curator photo management, and a 5-layer mathematical stealth shield.
- Achieved Grade A+ 100/100 SEO optimization and sub-200ms global edge delivery on Cloudflare Pages.

## Professional Experience

### Store Manager & Lead Systems Architect
**Ladies Zone Exclusive Showroom — Patna, Bihar, India** *(March 2021 – Present)*
- Direct day-to-day operations, inventory replenishment, and customer relationship management for a high-volume retail fashion showroom.
- Architected and deployed in-house biometric attendance audit ledger, retail POS billing software, and custom business workflow automations.
- Bridged physical business requirements with automated software engineering to eliminate operational overhead and inventory discrepancies.

## Education

### Bachelor of Computer Applications (BCA)
**National Business College — Patna, Bihar, India** *(Graduated January 2025)*
- Core coursework: Object-Oriented Software Design, Database Management Systems, Data Structures, Web Technologies, and Network Security.
"""

def generate_pdf():
    print(f"Generating Executive Resume PDF...")
    pdf_buffer = create_styled_resume_pdf(
        resume_markdown=resume_md,
        candidate_name="Mohammad Rehan",
        role_title="Software Architect & Tech Lead",
        contact_details={
            "email": "rehankhan20871621@gmail.com",
            "location": "Patna, Bihar, India",
            "phone": "+91 70915 18548",
            "whatsapp": "+91 70915 18548",
            "portfolio": "mohammadrehan.pages.dev",
            "github": "github.com/mohammadrehan1621",
            "linkedin": "linkedin.com/in/mohammad-rehan-tech"
        }
    )
    
    pdf_bytes = pdf_buffer.getvalue()
    PDF_PATH.write_bytes(pdf_bytes)
    print(f"✅ Generated: {PDF_PATH} ({len(pdf_bytes):,} bytes)")

if __name__ == "__main__":
    generate_pdf()
