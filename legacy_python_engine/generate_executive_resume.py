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
CODING_AGENTS_PATH = Path(r"C:\Users\rehan\Desktop\Coding Agents\Mohammad_Rehan_Resume.pdf")
WEBSITE_REPO_PATH = Path(r"C:\Users\rehan\Desktop\Rehan_Quant_Lab\Website_RehanQuantLab\Mohammad_Rehan_Resume.pdf")
DESKTOP_PATH = Path("C:/Users/rehan/Desktop/Mohammad_Rehan_Resume.pdf")

resume_md = """## Executive Summary
Founder & Lead Systems Architect at Rehan Quant Lab with 4+ years of hands-on experience bridging mission-critical commercial operations, forensic cybersecurity, and fault-tolerant distributed systems. Creator of RQL DocumentShield™ (forensic destructive PDF redactor & court-admissible SHA-256 compliance vault), Deterministic State Kernel (bare-metal Rust engine with >240,000 writes/sec, 604ns reads, hardware SHA-256 WAL, and MCA Rule 11(g) compliance), and AegisDB (2.54M ticks/sec @ 0.39µs via LMAX Disruptor cacheline alignment, 21.4M AVX2 SIMD invariant ops/sec @ 46.69ns). Architect of 17 commercial air-gapped sovereign desktop software suites across 4 Flagship Master Fleets distributed globally on Gumroad with 78% US enterprise traffic.

## Core Competencies & Architecture Stack
- **Enterprise Forensic Security & Air-Gapped Redaction**: True destructive vector/bytecode purging directly from PDF object streams (zero residual text, layer-peel immune), automated multi-pattern regex scanners (SSN, EIN, PAN, contact PII), XMP deep metadata stripping, and court-admissible SHA-256 Chain-of-Custody compliance certification (HIPAA Safe Harbor, EU GDPR Art. 17, ABA Formal Opinion 06-442).
- **Deterministic State Kernel (Rust Bare-Metal Engine)**: 100% on-premises, air-gapped state invariants engine compiled into native C-ABI dynamic library (`dse_core.dll`) via Fat LTO. Delivers >240k writes/sec (4.69µs commit), 604ns cached reads (<1µs), hardware SHA-256 Write-Ahead Log (WAL), and cold crash replay of 25,000 frames in 76.99ms with zero cloud leaks.
- **Commercial Desktop Software Architecture & Master Fleets**: Architect of 17 standalone enterprise software suites packaged into 4 dedicated 1-Click Master Setup Wizards (`Setup.exe`), EULA contract acceptance, dedicated GUI Uninstallers registered in Windows Settings (`HKCU`), High-DPI ClearType UI typography, and 100% air-gapped machine privacy.
- **The Antifragile Triad & Invariant Principles**: Aegis Shield pre-audit contract verification, Chaos Gauntlet adversarial fault injection (8 market disaster simulations), and Phoenix Autonomous Recovery (<500ms self-healing with ₹0.00 capital loss). Non-Newtonian liquid risk armor and volatility-adaptive position sizing.
- **AegisDB In-Memory Engine**: LMAX Disruptor 64-byte cacheline-padded ring buffer (2.54M ticks/sec, 0.39µs latency, zero false sharing across CPU cores), bare-metal RDTSC JIT x86_64 cycle counter (38.04 cycles/op), memory-mapped LSM WAL (3.56M syncs/sec, 3.02ms kill -9 hot recovery).
- **AVX2 SIMD Vectorized Invariant Engine**: High-throughput vectorized financial boundary evaluation across 10,000,000 operations (21.4M ops/sec, 46.69ns latency), enforcing 35% drawdown clamps, 30% untouchable cash reserve, and 0.000000000000% precision drift.
- **Multi-WAN Network Bonding & SCADA Telemetry**: RQL Conduit bare-metal link bonding with round-trip health heartbeats, automatic sub-10ms packet failover, and industrial sensor telemetry daemons.
- **Cloud Infrastructure & Security**: AWS Mumbai (ap-south-1), Cloudflare Pages Edge, Zero-Trust Network Access (ZTNA) via Private WireGuard/Tailscale Mesh, Linux systemd real-time priority tuning (Nice=-10).

## Key Production Systems & Architectures

### RQL DocumentShield™ — Enterprise Forensic PDF Redaction & Metadata Purge OS
- Architected an enterprise air-gapped PDF forensic sanitizer physically destroying underlying bytecode, vector streams, and font glyphs from raw PDF cross-reference tables (XREF), rendering documents immune to copy-paste, OCR reconstruction, or layer-peeling attacks.
- Engineered automated high-speed multi-pattern regex scanners detecting US Social Security Numbers (SSN), Credit Cards (16-digit PAN), Employer Identification Numbers (EIN), and confidential contact coordinates across high-volume document bundles.
- Implemented deep metadata and XML XMP stream purges, stripping author credentials, modification histories, and hidden camera EXIF data.
- Built automated SHA-256 cryptographic pre/post state hashing generating official, court-admissible Certificates of Forensic Sanitization aligned with US HIPAA Safe Harbor (45 CFR § 164.514), EU GDPR Art. 17, and ABA Formal Opinion 06-442. Packaged with custom 1-click Windows Master Setup and GUI Uninstaller.

### Deterministic State Kernel — Sub-Microsecond Rust State & Risk Engine
- Engineered a commercial bare-metal Rust state invariants engine compiled with Fat LTO (`opt-level = 3`, `codegen-units = 1`, `panic = "abort"`) producing a compact 1.06 MB C-ABI dynamic library (`dse_core.dll`) and 475 KB CLI (`dse-kernel-cli.exe`).
- Benchmarked write throughput exceeding 240,000 writes/sec (4.69µs commit latency) and read throughput exceeding 1,570,000 reads/sec (604ns cached latency).
- Implemented hardware SHA-256 Write-Ahead Logging with cold crash replay of 25,000 state frames in 76.99ms with zero data drift, satisfying MCA Rule 11(g) and SEBI quant audit trail requirements. Universal Python `ctypes` FFI bridge achieving >124,000 writes/sec without GIL contention.

[PAGEBREAK]

### RQL Sovereign Software Fleet — 17 Enterprise Desktop Applications & 4 Master Fleets
- Architected, compiled, and published 17 commercial air-gapped desktop suites on Gumroad (`quantify17.gumroad.com`), achieving organic international distribution with 78% customer acquisition from the United States.
- **Forensic & Compliance Fleet**: Engineered *RQL DocumentShield™* (true destructive PDF vector burn) and *Veritas Dossier™* (deterministic MCA Rule 11(g) statutory audit trail vault).
- **CA & Tax Automation Fleet**: Developed *TaxMatrix™ CA Reconciler* (automated GSTR-2B matching cross-referencing 100k+ invoices in <1s) and *LedgerGuard™* (automated Tally/SAP financial ledger variance reconciliation).
- **High-Performance Infrastructure Fleet**: Built *Deterministic State Kernel* (Rust DLL >240k writes/sec), *AegisDB™* (2.54M ticks/sec), *RQL Conduit™* (multi-WAN failover bonding), and *Industrial Sentinel™* (SCADA telemetry).
- **Retail POS & Logistics Fleet**: Deployed *StoreFlow™ POS Workstation*, *ExpressBill™*, *StockAudit™* (inventory barcode scanner), *TagMaster™* (thermal labeling engine), and *LocalMesh™* (offline LAN multi-counter sync).

### AegisDB — Distributed Antifragile In-Memory Database (Open-Source MIT)
- Architected an ultra-low-latency in-memory state engine and circular tick ring buffer with 64-byte cacheline padding achieving 2,535,916 ticks/sec at 0.39µs latency with zero false sharing across CPU cores.
- Implemented bare-metal x86_64 machine code JIT timing (RDTSC) reading physical CPU cycles directly in 38.04 cycles per operation.
- Evaluated 10,000,000 extreme market operations in AVX2 SIMD vector chunks at 21,417,114 ops/sec (46.69ns per invariant check) with audited 0.000000000000% mathematical precision drift.
- Built a zero-syscall memory-mapped (mmap) LSM append-only Write-Ahead Log (WAL) achieving 3,559,925 syncs/sec (0.28µs append) and 3.02ms kill -9 hot replay recovery with ₹0.00 / 0 bytes data loss.

### Commercial Retail POS & High-Volume Inventory Ledger (StoreFlow™ & ExpressBill™)
- Engineered commercial offline Point of Sale (POS) and inventory ledger managing retail store operations, thermal barcode generation, and multi-counter LAN synchronization.
- Features multi-counter SQLite WAL concurrency protection, real-time margin analytics, and automated stock replenishment forecasting, reducing inventory holding costs by 30%.

## Professional Experience

### Founder & Lead Systems Architect
**Rehan Quant Lab™ — Patna, Bihar, India (Remote Global)** *(January 2023 – Present)*
- Direct independent systems research and commercial software engineering across low-latency financial systems, deterministic kernels, and enterprise forensic cybersecurity suites.
- Engineered and launched 17 commercial desktop software suites and 4 1-Click Master Setup Fleets on Gumroad (`quantify17.gumroad.com`), generating qualified organic traffic with 78% customer discovery from the United States.
- Architected `RQL DocumentShield™` ($199–$799) and `Deterministic State Kernel` ($249) as standalone high-margin commercial releases.
- Directed end-to-end product architecture, bare-metal C/Rust compilation, PyMuPDF forensic engines, and international Cloudflare Pages edge deployment.

### Store & Operations Manager
**Ladies Zone Exclusive Showroom — Patna, Bihar, India** *(March 2021 – Present)*
- Direct day-to-day operations, inventory replenishment, and customer relationship management for a high-volume retail fashion showroom in Patna, Bihar.
- Architected and deployed in-house biometric attendance audit ledger, retail POS billing software, and custom business workflow automations.
- Bridged physical business requirements with automated software engineering to eliminate operational overhead and inventory discrepancies.
- Managed vendor relations, staff scheduling, commercial margin analysis, and customer dispute resolution with 100% operational continuity.

## Education & Academic Credentials

### Bachelor of Computer Applications (BCA)
**National Business College — Patna, Bihar, India** *(Graduated January 2025)*
- Core coursework: Object-Oriented Software Design, Database Management Systems, Data Structures, Web Technologies, and Network Security.
- Capstone Project: Enterprise Retail Management System with Real-Time Inventory Tracking and POS Integration.

## Technical Environment & Production Safeguards
- **Languages & Core Systems**: Rust (Bare-Metal C-ABI FFI, Fat LTO), C (AVX2 SIMD), Python 3.14/3.12, PyMuPDF, AsyncIO, FastAPI, Streamlit, Modern JavaScript.
- **Databases & Protocols**: AegisDB (In-Memory Ring Buffers), Deterministic State Kernel (Rust WAL), SQLite (WAL micro-journaling), RESTful APIs, WebSocket, WireGuard/Tailscale VPN.
- **Architectural Principles**: Antifragile Triad (Aegis-Chaos-Phoenix), Zero Capital Leakage, True Destructive Redaction, 100% Air-Gapped Machine Sovereignty, Pure Native .EXE.
- **DevOps & Infrastructure**: AWS Mumbai (ap-south-1), Cloudflare Pages Edge, Linux systemd (Nice=-10), Git, 250+ Unit & Invariant Tests (100% Passed).
"""

def generate_pdf():
    print("Generating Executive Resume PDF...")
    logo_path = str(PORTFOLIO_DIR / "emblem.jpg")
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
            "logo_path": logo_path if Path(logo_path).exists() else None
        }
    )
    
    pdf_bytes = pdf_buffer.getvalue()
    PDF_PATH.write_bytes(pdf_bytes)
    print(f"✅ Generated Portfolio PDF: {PDF_PATH} ({len(pdf_bytes):,} bytes)")
    
    for dest in [CODING_AGENTS_PATH, WEBSITE_REPO_PATH, DESKTOP_PATH]:
        try:
            dest.write_bytes(pdf_bytes)
            print(f"✅ Synced to: {dest}")
        except Exception as e:
            print(f"Sync notice for {dest}: {e}")

if __name__ == "__main__":
    generate_pdf()
