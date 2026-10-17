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
High-impact AI Systems Architect and Operations Manager with 4+ years of hands-on leadership bridging commercial retail operations and fault-tolerant software engineering. Architect of institutional-grade algorithmic trading systems with zero capital leakage, autonomous self-healing engines with sub-50ms MTTR, multi-modal generative AI pipelines, and commercial enterprise POS architectures.

## Core Competencies & Architecture Stack
- **Distributed Systems & Fault Tolerance**: Write-Ahead Logging (WAL) Micro-Journaling, Continuous Chaos Engineering, Sub-50ms Process Supervision, Dynamic AST Poison Quarantine, Circuit Breakers.
- **Algorithmic Trading & FinTech**: Low-latency multi-agent derivatives execution (NIFTY/BANKNIFTY/SENSEX), Spot/15m VWAP structural stop-loss guards, 0-DTE theta decay shields, sub-8ms exchange proximity.
- **Generative AI & Media Engineering**: Autonomous LLM agent routing, Neural TTS voice synthesis, FFmpeg programmatic video composition, ASS animated subtitle engines.
- **Cloud Infrastructure & Security**: AWS Mumbai (ap-south-1), Cloudflare Pages Edge, Zero-Trust Network Access (ZTNA) via Private WireGuard Mesh, Linux systemd real-time priority tuning (Nice=-10).
- **Full-Stack & POS Development**: Python 3.12, AsyncIO, SQLite, Streamlit, HTML5/CSS3, Modern JavaScript, Thermal Printer Protocol, ReportLab PDF Engine.

## Key Production Systems & Architectures

### Indian Quant Options Sniper — Institutional Derivatives Execution Engine
- Engineered an institutional-grade, multi-agent algorithmic options execution engine deployed on AWS Mumbai (ap-south-1) with sub-8ms deterministic fiber proximity to NSE co-location.
- Implemented single direct atomic routing for <=24 lots (390 NIFTY qty), eliminating retail double-brokerage penalties and 500ms market-maker front-running lag.
- Anchored dynamic stop-loss to NIFTY Spot 15m VWAP structure rather than option premium noise, backed by a 35% emergency disaster ceiling and a 30% capital reserve lock.
- Automated a 13:30 IST Expiry Day Theta Filter to eliminate 0-DTE time decay slaughter, automatically routing breakout momentum to next-week contracts.
- Secured live operations under 24/7 systemd autopilot (0.00 load average, 2GB swap protection) isolated behind an encrypted private WireGuard mesh (ZTNA).

### Project Phoenix — Autonomous Fault-Tolerant Resilience Engine & 24/7 Chaos Sentinel
- Architected an antifragile self-healing framework enforcing the Golden Rule of Resilience: auto-healing into a permanently evolved, stronger state rather than vulnerable status-quo recovery.
- Implemented EvolutionaryHardener: automatic generation Epoch progression, SHA-256 perimeter signature quarantine, and +25% adaptive parameter stiffening.
- Certified sub-50ms MTTR (11ms–60ms) hot process resurrection with Ash Ledger write-ahead micro-journaling preventing zero state loss.
- Validated via automated Level-5 Doomsday Chaos Gauntlet: withstood 50-thread concurrent stampedes, 800MB heap shockwaves, ReDoS bombs, and disk sector corruption with 100.0% defense.
- Operates as a permanent 24/7 background sentinel running autonomous hourly resilience drills.

### Autonomous AI Shorts & Reels Studio — Multi-Modal Video Production Engine
- Developed an end-to-end automated vertical video (9:16) production studio combining topic-to-script LLM generation, studio neural voiceover, and dynamic B-roll synchronization.
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
        role_title="Senior AI Systems Architect & Tech Lead",
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
