import sys
import shutil
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
DESKTOP_PATH = Path("C:/Users/rehan/Desktop/Mohammad_Rehan_Resume.pdf")

resume_md = """
## Executive Summary
Founder & Lead Systems Architect at Rehan Quant Lab™ with 4+ years of hands-on experience bridging commercial enterprise operations and fault-tolerant distributed systems. Creator of AegisDB™ (2.54M ticks/sec @ 0.39µs via LMAX Disruptor cacheline alignment, 21.4M AVX2 SIMD invariant ops/sec @ 46.69ns across 10M operations with 0.000000000000% precision drift), Non-Newtonian Computational Liquid Diamond Armor (dynamic orderbook spread clamping, hydraulic volatility damping), The Holy Trinity Framework (Aegis, Chaos, Phoenix: autonomous antifragile resilience loop with 3 Critical Trap Fortifications), and institutional derivatives execution engines with zero capital leakage on AWS Mumbai.

## Core Competencies & Architecture Stack
- **AegisDB™ In-Memory Engine**: LMAX Disruptor 64-byte cacheline-padded ring buffer (2.54M ticks/sec, 0.39µs latency, zero false sharing across CPU cores), bare-metal RDTSC JIT x86_64 machine code cycle counter (38.04 cycles/op), memory-mapped (mmap) LSM Ash Ledger WAL (3.56M syncs/sec, 0.28µs append, 3.02ms kill -9 hot recovery, ₹0.00 data loss).
- **AVX2 SIMD Vectorized Invariant Engine**: High-throughput vectorized financial boundary evaluation across 10,000,000 operations (21.4M ops/sec, 46.69ns latency), enforcing 35% drawdown clamps, 30% untouchable cash reserve, and 0.000000000000% precision drift.
- **Non-Newtonian Liquid Diamond Armor**: Physical dilatant risk model: peacetime fluid water flow (₹0.05 spread, 100% capacity), dynamic spread clamping (₹1.50 diamond lock), hydraulic volatility damping (exponential sizing compression down to 25% exposure upon +15% VIX spikes before stop-loss touch), and viscosity damping (>=75% depth collapse lockout).
- **7-Agent Autonomous Swarm Tribunal**: Structured 3-round adversarial debate bus with Directional Toxicity Intelligence (VPIN volume-synchronized probability of toxicity + Cumulative Volume Delta supportive sweep validation vs hostile dump vetoes) and post-trade forensic audits.
- **The Holy Trinity Resilience Framework**: Aegis (Static AST Contract Verification, Precision Floor Quantization, 35% Risk Drawdown Ceiling), Chaos Gauntlet (Adversarial Stress Injections: 6 Exchange Disasters, 504 Timeouts, Socket Drops, Contention), Phoenix Engine (Ash Ledger WAL Micro-Journaling, Sub-1ms Hot Process Resurrection, Antifragile Genomic Hardening).
- **FinTech & Algorithmic Trading**: Low-latency multi-agent options execution (NSE NIFTY/BANKNIFTY), Spot/15m VWAP structural stop-loss guards, 13:30 IST 0-DTE theta decay shields, sub-8ms exchange proximity, Kotak Neo v3 orchestrator.
- **Commercial SaaS & Multi-Agent Systems**: Autonomous Agent Supervision, Multi-Agent Fleet Registries, Web Mission Control Telemetry Dashboards, High-Throughput REST APIs, Python SDK distribution, Cost/Token ceiling budgeting.
- **Cloud Infrastructure & Security**: AWS Mumbai (ap-south-1), Cloudflare Pages Edge, Zero-Trust Network Access (ZTNA) via Private WireGuard/Tailscale Mesh, Linux systemd real-time priority tuning (Nice=-10).

## Key Production Systems & Architectures

### AegisDB™ — Distributed Antifragile In-Memory Database (Open-Source MIT)
- Architected an ultra-low-latency in-memory state engine and circular tick ring buffer with 64-byte cacheline padding achieving 2,535,916 ticks/sec at 0.39µs latency with zero false sharing across CPU cores.
- Implemented bare-metal x86_64 machine code JIT timing (RDTSC) reading physical CPU cycles directly in 38.04 cycles per operation.
- Evaluated 10,000,000 extreme market operations in AVX2 SIMD vector chunks at 21,417,114 ops/sec (46.69ns per invariant check) with audited 0.000000000000% mathematical precision drift.
- Built a zero-syscall memory-mapped (mmap) LSM append-only Ash Ledger achieving 3,559,925 syncs/sec (0.28µs append) and 3.02ms kill -9 hot replay recovery with ₹0.00 / 0 bytes data loss.
- Embedded distributed Raft consensus over UDP multicast with sub-millisecond term validation, surviving Jepsen split-brain partition torture with zero double-spend anomalies.

### Indian Quant Options Sniper — Institutional Derivatives Execution Engine
- Engineered an institutional-grade, multi-agent algorithmic options execution engine deployed on AWS Mumbai (ap-south-1) with sub-8ms deterministic fiber proximity to NSE co-location.
- Integrated Non-Newtonian Liquid Diamond Armor: Dynamic Orderbook Spread Clamping (hardens entry shut upon ₹1.50 spread breach) and Hydraulic Volatility Damper (compresses exposure to 25% on VIX spikes).
- Deployed 7-Agent Autonomous Swarm with Directional Toxicity Intelligence (VPIN/CVD) distinguishing aggressive momentum sweeps from hostile seller dumps.
- Embedded AegisDB™ in-memory ring buffer for sub-microsecond (<0.39µs) tick ingestion and active trade state caching, eliminating SQLite lock contention.
- Implemented single direct atomic routing for <=24 lots (390 NIFTY qty), eliminating retail double-brokerage penalties and 500ms market-maker front-running lag.
- Anchored dynamic stop-loss to NIFTY Spot 15m VWAP structure rather than option premium noise, backed by a 35% emergency disaster ceiling and a 30% capital reserve lock.
- Secured live operations under 24/7 systemd autopilot (0.00 load average, 2GB swap protection) isolated behind an encrypted private Tailscale/WireGuard mesh.
- **Broker Integration & Autopilot**: Kotak Neo API v3 multi-session orchestrator with automated TOTP session renewal, sub-5ms heartbeat telemetry, and real-time slippage modeling (<0.02%).

[PAGEBREAK]

### AegisOps: Autonomous AI Agent Operations SaaS — Antifragile Mission Control
- **Commercial Mission Control Platform**: Production multi-tenant B2B SaaS platform commercializing The Holy Trinity resilience engine for developer teams and enterprises deploying autonomous multi-agent swarms.
- **Philosophy**: Enforces Nassim Taleb's Golden Rule of Resilience: Multi-agent systems must never recover to a vulnerable status quo—every auto-heal permanently hardens execution envelopes and advances Genomic Generations.
- **Web Mission Control UI (:8510)**: Real-time agent fleet observability, live health telemetry, token/cost ceiling enforcement, and one-click synthetic chaos injection console.
- **Multi-Agent Fleet Registry**: Centralized supervisor managing agent lifecycles (Idle, Running, Stressed, Resurrecting, Immune), tracking genomic generations and self-healing epochs.
- **High-Throughput Public REST API (:8000)**: Sub-millisecond endpoints for task dispatching, heartbeat reporting, and write-ahead Ash Ledger log synchronization.
- **Downloadable Python SDK (`pip install aegisops`)**: Drop-in resilience client enabling external agents to auto-heal from LLM rate limits (429), hallucinated JSON, and tool hang crashes.
- **Verified Benchmark Metrics**: Sub-10ms Hot-Resurrection MTTR (<10ms), $0.00 Zero-Loss Capital Guarantee, and 25/25 Pytest suites passed with 100% test coverage.

### Autonomous Video & Content Studio — Multi-Modal Programmatic Engine
- Developed an end-to-end automated vertical video (9:16) production studio combining topic-to-script agent workflows, studio neural voiceover, and dynamic B-roll synchronization.
- Engineered a custom ASS subtitle engine compiling word-by-word colored animated subtitle cues (Hormozi style) with automatic background audio ducking.
- Fortified rendering pipeline with Phoenix process supervision, preventing FFmpeg memory leaks, out-of-memory crashes, and Zombie sub-processes during batch renders.
- Autonomously outputs ready-to-publish 1080x1920 Full HD video packages complete with high-CTR titles, SEO descriptions, and automated hashtag generation.

### Footwear Retail POS & High-Volume Inventory Ledger
- Built a commercial Point of Sale (POS) and inventory ledger managing retail store operations, barcode scanning, thermal printing, and GST compliance.
- Features multi-counter SQLite WAL concurrency protection, inventory reorder forecasting, and real-time sales margin dashboards.
- Engineered automated biometric staff attendance logging and stock replenishment forecasting, reducing inventory holding costs by 30%.

## Professional Experience

### Founder & Lead Systems Architect
**Rehan Quant Lab™ — Patna, Bihar, India (Remote Global)** *(January 2023 – Present)*
- Direct independent systems research and software development for ultra-low-latency in-memory databases, autonomous AI swarms, and deterministic quantitative trading infrastructure.
- Engineered AegisDB™, achieving 2.62M reads/sec (0.38µs) and sub-15ms Phoenix WAL crash resurrection with zero-heap garbage collection jitter.
- Architected and deployed the Indian Quant Options Sniper 24/7 on AWS EC2 Mumbai (ap-south-1) with sub-8ms fiber proximity to the NSE.
- Built the Holy Trinity Antifragility Engine implementing Nassim Taleb's Golden Rule of Resilience with continuous evolutionary parameter mutation.

### Store Manager & Lead Systems Architect
**Ladies Zone Exclusive Showroom — Patna, Bihar, India** *(March 2021 – Present)*
- Direct day-to-day operations, inventory replenishment, and customer relationship management for a high-volume retail fashion showroom in Patna, Bihar.
- Architected and deployed in-house biometric attendance audit ledger, retail POS billing software, and custom business workflow automations.
- Bridged physical business requirements with automated software engineering to eliminate operational overhead and inventory discrepancies.
- Managed vendor relations, staff scheduling, commercial margin analysis, and customer dispute resolution with 100% operational continuity.
- Spearheaded inventory digital transformation, cutting dead-stock capital allocation by 25% through real-time stock turnover telemetry.

## Education & Academic Credentials

### Bachelor of Computer Applications (BCA)
**National Business College — Patna, Bihar, India** *(Graduated January 2025)*
- Core coursework: Object-Oriented Software Design, Database Management Systems, Data Structures, Web Technologies, and Network Security.
- Capstone Project: Enterprise Retail Management System with Real-Time Inventory Tracking and POS Integration.

## Technical Environment & Production Safeguards
- **Languages & Frameworks**: Python 3.12, AsyncIO, FastAPI, Streamlit, HTML5/CSS3, Modern JavaScript, Node.js, Shell Scripting.
- **Databases & Protocols**: AegisDB (In-Memory Ring Buffers), SQLite (WAL micro-journaling), PostgreSQL, Redis, RESTful APIs, WebSocket, WireGuard/Tailscale VPN.
- **Architectural Principles**: Antifragile Self-Healing, Zero Capital Leakage, Atomic Single-Route Execution, Adaptive Confluence Stiffening.
- **DevOps & Infrastructure**: AWS Mumbai (ap-south-1), Cloudflare Pages Edge, Linux systemd (Nice=-10), Git, Pytest (100% Passed).
"""

def generate_pdf():
    print(f"Generating Executive Resume PDF...")
    pdf_buffer = create_styled_resume_pdf(
        resume_markdown=resume_md,
        candidate_name="Mohammad Rehan",
        role_title="Founder & Lead Systems Architect @ Rehan Quant Lab™",
        contact_details={
            "email": "founder@rehanquantlab.com",
            "location": "Patna, Bihar, India",
            "phone": "+91 70915 18548",
            "whatsapp": "+91 70915 18548",
            "portfolio": "rehanquantlab.com",
            "github": "github.com/rehanquantlab",
            "linkedin": "linkedin.com/in/mohammad-rehan-tech",
            "logo_path": str(PORTFOLIO_DIR / "emblem.jpg")
        }
    )
    
    pdf_bytes = pdf_buffer.getvalue()
    PDF_PATH.write_bytes(pdf_bytes)
    print(f"✅ Generated Portfolio PDF: {PDF_PATH} ({len(pdf_bytes):,} bytes)")
    
    try:
        shutil.copy2(PDF_PATH, DESKTOP_PATH)
        print(f"✅ Synced to Desktop: {DESKTOP_PATH}")
    except Exception as e:
        print(f"Desktop sync notice: {e}")

if __name__ == "__main__":
    generate_pdf()

