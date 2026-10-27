import os
import sys
import re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PORTFOLIO_DIR = Path(r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev")
ALL_HTML_FILES = ["index.html", "projects.html", "aegis.html", "experience.html", "contact.html", "legal.html"]

CANONICAL_HEADER = """<header class="sticky top-0 z-40 w-full border-b border-slate-200/80 glass-panel bg-white/90 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        <!-- Brand Logo -->
        <a class="flex items-center gap-3 group shrink-0" href="index.html">
            <img src="emblem.webp" loading="lazy" decoding="async" alt="Rehan Quant Lab" class="w-9 h-9 rounded-xl object-cover shadow-sm group-hover:scale-105 transition border border-slate-700/50" />
            <div>
                <span class="font-bold text-slate-900 tracking-tight text-base block">Mohammad Rehan</span>
                <span class="text-[10px] text-slate-500 font-medium block -mt-1">Founder @ Rehan Quant Lab</span>
            </div>
        </a>

        <!-- Desktop Navigation Links (Clean, Balanced & Breathable) -->
        <nav class="hidden md:flex items-center gap-6 lg:gap-7 text-sm font-medium text-slate-600">
            <a class="hover:text-slate-900 transition font-semibold" href="index.html">Home</a>
            <a class="hover:text-slate-900 transition" href="projects.html">Projects</a>

            <!-- Interactive Products Dropdown -->
            <div class="relative group">
                <button class="flex items-center gap-1.5 text-slate-600 group-hover:text-slate-900 transition font-medium focus:outline-none py-1">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span>Products</span>
                    <i class="w-3.5 h-3.5 text-slate-400 group-hover:text-slate-600 transition group-hover:rotate-180 duration-200" data-lucide="chevron-down"></i>
                </button>

                <!-- Popover Menu -->
                <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 w-80 opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto transition-all duration-200 ease-out z-50">
                    <div class="bg-white/95 backdrop-blur-xl rounded-2xl shadow-xl border border-slate-200 p-2 space-y-1">
                        <!-- Product 1: Deterministic State Kernel -->
                        <a href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE?wanted=true" target="_blank" rel="noopener noreferrer" class="flex items-start gap-2.5 p-2 rounded-xl hover:bg-emerald-50/80 transition group/item">
                            <div class="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0 mt-0.5 group-hover/item:bg-emerald-600 group-hover/item:text-white transition">
                                <i class="w-4 h-4" data-lucide="cpu"></i>
                            </div>
                            <div class="flex-1 min-w-0">
                                <div class="flex items-center justify-between gap-1">
                                    <span class="text-xs font-bold text-slate-900 group-hover/item:text-emerald-700 truncate">Deterministic State Kernel&trade;</span>
                                    <span class="text-[9px] font-mono font-bold text-emerald-800 bg-emerald-100 px-1.5 py-0.5 rounded whitespace-nowrap">$249</span>
                                </div>
                                <p class="text-[11px] text-slate-500 mt-0.5 truncate">Rust Bare-Metal &bull; 604ns Reads &bull; SHA-256 WAL</p>
                            </div>
                        </a>
                        <!-- Product 2: RQL Aegis -->
                        <a href="https://quantify17.gumroad.com/l/rql-aegis/EARLYBIRD?wanted=true" target="_blank" rel="noopener noreferrer" class="flex items-start gap-2.5 p-2 rounded-xl hover:bg-cyan-50/80 transition group/item">
                            <div class="w-8 h-8 rounded-lg bg-cyan-100 text-cyan-700 flex items-center justify-center shrink-0 mt-0.5 group-hover/item:bg-cyan-600 group-hover/item:text-white transition">
                                <i class="w-4 h-4" data-lucide="shield"></i>
                            </div>
                            <div class="flex-1 min-w-0">
                                <div class="flex items-center justify-between gap-1">
                                    <span class="text-xs font-bold text-slate-900 group-hover/item:text-cyan-700 truncate">RQL Aegis&trade;</span>
                                    <span class="text-[9px] font-mono font-bold text-cyan-800 bg-cyan-100 px-1.5 py-0.5 rounded whitespace-nowrap">$125</span>
                                </div>
                                <p class="text-[11px] text-slate-500 mt-0.5 truncate">On-Premises Risk Middleware &bull; Volatility Clamp</p>
                            </div>
                        </a>
                        <!-- Product 3: Veritas Dossier -->
                        <a href="https://quantify17.gumroad.com/l/eucck/VERITAS?wanted=true" target="_blank" rel="noopener noreferrer" class="flex items-start gap-2.5 p-2 rounded-xl hover:bg-purple-50/80 transition group/item">
                            <div class="w-8 h-8 rounded-lg bg-purple-100 text-purple-700 flex items-center justify-center shrink-0 mt-0.5 group-hover/item:bg-purple-600 group-hover/item:text-white transition">
                                <i class="w-4 h-4" data-lucide="file-check"></i>
                            </div>
                            <div class="flex-1 min-w-0">
                                <div class="flex items-center justify-between gap-1">
                                    <span class="text-xs font-bold text-slate-900 group-hover/item:text-purple-700 truncate">Veritas Dossier&trade;</span>
                                    <span class="text-[9px] font-mono font-bold text-purple-800 bg-purple-100 px-1.5 py-0.5 rounded whitespace-nowrap">$249</span>
                                </div>
                                <p class="text-[11px] text-slate-500 mt-0.5 truncate">Air-Gapped Private DRHP &amp; Dilution Auditor</p>
                            </div>
                        </a>
                        <!-- Product 4: Industrial Fragility Sentinel -->
                        <a href="https://quantify17.gumroad.com/l/ivyiwh/SENTINEL?wanted=true" target="_blank" rel="noopener noreferrer" class="flex items-start gap-2.5 p-2 rounded-xl hover:bg-amber-50/80 transition group/item">
                            <div class="w-8 h-8 rounded-lg bg-amber-100 text-amber-800 flex items-center justify-center shrink-0 mt-0.5 group-hover/item:bg-amber-600 group-hover/item:text-white transition">
                                <i class="w-4 h-4" data-lucide="factory"></i>
                            </div>
                            <div class="flex-1 min-w-0">
                                <div class="flex items-center justify-between gap-1">
                                    <span class="text-xs font-bold text-slate-900 group-hover/item:text-amber-800 truncate">Industrial Sentinel&trade;</span>
                                    <span class="text-[9px] font-mono font-bold text-amber-800 bg-amber-100 px-1.5 py-0.5 rounded whitespace-nowrap">$299</span>
                                </div>
                                <p class="text-[11px] text-slate-500 mt-0.5 truncate">Shop Floor Uptime Daemon &bull; Sun Tzu Asymmetry</p>
                            </div>
                        </a>
                        <!-- Product 5: RQL Conduit Bonding Engine -->
                        <a href="https://quantify17.gumroad.com/l/rql-conduit?wanted=true" target="_blank" rel="noopener noreferrer" class="flex items-start gap-2.5 p-2 rounded-xl hover:bg-sky-50/80 transition group/item">
                            <div class="w-8 h-8 rounded-lg bg-sky-100 text-sky-700 flex items-center justify-center shrink-0 mt-0.5 group-hover/item:bg-sky-600 group-hover/item:text-white transition">
                                <i class="w-4 h-4" data-lucide="network"></i>
                            </div>
                            <div class="flex-1 min-w-0">
                                <div class="flex items-center justify-between gap-1">
                                    <span class="text-xs font-bold text-slate-900 group-hover/item:text-sky-700 truncate">RQL Conduit Engine&trade;</span>
                                    <span class="text-[9px] font-mono font-bold text-sky-800 bg-sky-100 px-1.5 py-0.5 rounded whitespace-nowrap">$60</span>
                                </div>
                                <p class="text-[11px] text-slate-500 mt-0.5 truncate">Rust Multi-WAN Bonding &bull; Sub-3ms Failover</p>
                            </div>
                        </a>
                        <!-- Product 6: ExpressBill POS -->
                        <a href="https://quantify17.gumroad.com/l/expressbill?wanted=true" target="_blank" rel="noopener noreferrer" class="flex items-start gap-2.5 p-2 rounded-xl hover:bg-teal-50/80 transition group/item">
                            <div class="w-8 h-8 rounded-lg bg-teal-100 text-teal-700 flex items-center justify-center shrink-0 mt-0.5 group-hover/item:bg-teal-600 group-hover/item:text-white transition">
                                <i class="w-4 h-4" data-lucide="receipt"></i>
                            </div>
                            <div class="flex-1 min-w-0">
                                <div class="flex items-center justify-between gap-1">
                                    <span class="text-xs font-bold text-slate-900 group-hover/item:text-teal-700 truncate">ExpressBill POS&trade;</span>
                                    <span class="text-[9px] font-mono font-bold text-teal-800 bg-teal-100 px-1.5 py-0.5 rounded whitespace-nowrap">$49</span>
                                </div>
                                <p class="text-[11px] text-slate-500 mt-0.5 truncate">Offline Retail Suite &bull; Dynamic UPI &bull; PWA</p>
                            </div>
                        </a>
                    </div>
                </div>
            </div>

            <a class="hover:text-slate-900 transition" href="experience.html">Experience</a>
            <a class="hover:text-indigo-600 transition flex items-center gap-1 text-slate-600" href="https://rehanquantlab.substack.com" target="_blank" rel="noopener noreferrer">
                Research <i class="w-3 h-3" data-lucide="external-link"></i>
            </a>
            <a class="hover:text-slate-900 transition" href="contact.html">Contact</a>
        </nav>

        <!-- Right CTAs (Balanced & Light) -->
        <div class="hidden lg:flex items-center gap-2.5 shrink-0">
            <a class="p-2 text-slate-500 hover:text-slate-900 hover:bg-slate-100 rounded-xl transition" href="https://x.com/rehanquantlab" target="_blank" rel="noopener noreferrer" title="Follow on X (@rehanquantlab)">
                <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
            </a>

            <!-- Resume Ghost Button -->
            <a class="text-xs font-semibold text-slate-700 hover:text-slate-900 px-3 py-2 rounded-xl hover:bg-slate-100 transition flex items-center gap-1.5" href="Mohammad_Rehan_Resume.pdf" download>
                <i class="w-3.5 h-3.5 text-slate-500" data-lucide="file-down"></i>
                <span>Resume</span>
            </a>

            <!-- Primary Action Button -->
            <a class="inline-flex items-center gap-1.5 bg-slate-900 hover:bg-slate-800 text-white text-xs font-semibold px-4 py-2 rounded-xl transition shadow-xs group" href="contact.html#schedule-briefing">
                <i class="w-3.5 h-3.5 text-emerald-400" data-lucide="terminal"></i>
                <span>Schedule Briefing</span>
            </a>
        </div>

        <!-- Mobile Menu Toggle Button -->
        <button class="md:hidden p-2 text-slate-700 hover:text-slate-900 focus:outline-none" id="mobile-menu-btn" aria-label="Toggle Navigation">
            <i class="w-6 h-6" data-lucide="menu"></i>
        </button>
    </div>

    <!-- Mobile Menu Dropdown -->
    <div class="hidden md:hidden border-t border-slate-200 bg-white/98 backdrop-blur-xl px-4 pt-3 pb-5 space-y-2 shadow-xl" id="mobile-menu">
        <a class="block py-2 px-3 rounded-lg hover:bg-slate-50 text-slate-800 font-semibold text-sm" href="index.html">Home</a>
        <a class="block py-2 px-3 rounded-lg hover:bg-slate-50 text-slate-800 font-medium text-sm" href="projects.html">Projects</a>

        <div class="pt-2 pb-1 px-3 text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider">Commercial Products (Sovereign Suite)</div>
        <a class="block py-2 px-3 rounded-lg bg-emerald-50 text-emerald-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-emerald-600" data-lucide="cpu"></i>
                <span>Deterministic State Kernel&trade;</span>
            </div>
            <span class="bg-emerald-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$249</span>
        </a>
        <a class="block py-2 px-3 rounded-lg bg-cyan-50 text-cyan-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/rql-aegis/EARLYBIRD?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-cyan-600" data-lucide="shield"></i>
                <span>RQL Aegis&trade;</span>
            </div>
            <span class="bg-cyan-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$125</span>
        </a>
        <a class="block py-2 px-3 rounded-lg bg-purple-50 text-purple-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/eucck/VERITAS?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-purple-600" data-lucide="file-check"></i>
                <span>Veritas Dossier&trade;</span>
            </div>
            <span class="bg-purple-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$249</span>
        </a>
        <a class="block py-2 px-3 rounded-lg bg-amber-50 text-amber-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/ivyiwh/SENTINEL?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-amber-600" data-lucide="factory"></i>
                <span>Industrial Fragility Sentinel&trade;</span>
            </div>
            <span class="bg-amber-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$299</span>
        </a>
        <a class="block py-2 px-3 rounded-lg bg-sky-50 text-sky-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/rql-conduit?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-sky-600" data-lucide="network"></i>
                <span>RQL Conduit Engine&trade;</span>
            </div>
            <span class="bg-sky-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$60</span>
        </a>
        <a class="block py-2 px-3 rounded-lg bg-teal-50 text-teal-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/expressbill?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-teal-600" data-lucide="receipt"></i>
                <span>ExpressBill POS&trade;</span>
            </div>
            <span class="bg-teal-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$49</span>
        </a>

        <a class="block py-2 px-3 rounded-lg hover:bg-slate-50 text-slate-800 font-medium text-sm" href="experience.html">Experience</a>
        <a class="block py-2 px-3 rounded-lg hover:bg-slate-50 text-indigo-600 font-semibold text-sm flex items-center justify-between" href="https://rehanquantlab.substack.com" target="_blank" rel="noopener noreferrer">
            <span>Technical Research (Substack)</span>
            <i class="w-4 h-4" data-lucide="external-link"></i>
        </a>
        <a class="block py-2 px-3 rounded-lg hover:bg-slate-50 text-slate-800 font-medium text-sm" href="contact.html">Contact</a>

        <div class="pt-3 border-t border-slate-100 flex items-center gap-2">
            <a class="flex-1 bg-slate-900 text-white text-center text-xs font-semibold py-2.5 rounded-xl shadow-xs" href="contact.html#schedule-briefing">Schedule Briefing</a>
            <a class="flex-1 bg-slate-100 hover:bg-slate-200 text-slate-800 text-center text-xs font-semibold py-2.5 rounded-xl border border-slate-200" href="Mohammad_Rehan_Resume.pdf" download>Resume (PDF)</a>
        </div>
    </div>
</header>"""

SECURITY_META_TAGS = """
    <!-- 🛡️ Institutional Security & HTTPS Enforcement Headers -->
    <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests; default-src 'self' https: data: 'unsafe-inline' 'unsafe-eval'; img-src 'self' data: https:; font-src 'self' https: data:;">
    <meta http-equiv="Strict-Transport-Security" content="max-age=31536000; includeSubDomains; preload">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta http-equiv="X-Frame-Options" content="DENY">
    <meta name="referrer" content="strict-origin-when-cross-origin">
"""

CLOUDFLARE_HEADERS_CONTENT = """/*
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  X-XSS-Protection: 1; mode=block
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()
  Content-Security-Policy: upgrade-insecure-requests; default-src 'self' https: data: 'unsafe-inline' 'unsafe-eval'; img-src 'self' data: https:; font-src 'self' https: data:;
"""

def execute_security_and_header_fix():
    print("=" * 70)
    print("🔒 FIXING NAVIGATION HEADER & ENFORCING MAXIMUM SECURITY")
    print("=" * 70)

    # 1. Create Cloudflare Pages _headers file
    headers_file = PORTFOLIO_DIR / "_headers"
    headers_file.write_text(CLOUDFLARE_HEADERS_CONTENT, encoding="utf-8")
    print("✅ Created Cloudflare Pages _headers file with HSTS + CSP.")

    # 2. Iterate each HTML file and cleanly replace header + security meta
    for fname in ALL_HTML_FILES:
        fpath = PORTFOLIO_DIR / fname
        if not fpath.exists():
            continue

        content = fpath.read_text(encoding="utf-8")

        # Replace the entire <header ... </header> block
        m_header = re.search(r'<header[^>]*>.*?</header>', content, re.DOTALL)
        if m_header:
            content = content[:m_header.start()] + CANONICAL_HEADER + content[m_header.end():]
            print(f"[{fname}] Replaced <header> block with 100% clean canonical header.")
        else:
            print(f"[{fname}] ⚠️ Warning: Could not locate <header> block!")

        # Replace old CSP meta tag with clean institutional security meta tags
        content = re.sub(r'<meta content="default-src [^>]*http-equiv="Content-Security-Policy"[^>]*>', '', content)
        content = re.sub(r'<meta http-equiv="Content-Security-Policy"[^>]*>', '', content)
        content = re.sub(r'<meta http-equiv="Strict-Transport-Security"[^>]*>', '', content)
        content = re.sub(r'<meta http-equiv="X-Content-Type-Options"[^>]*>', '', content)
        content = re.sub(r'<meta http-equiv="X-Frame-Options"[^>]*>', '', content)
        content = re.sub(r'<meta name="referrer"[^>]*>', '', content)

        # Insert security meta tags after viewport meta
        if "Institutional Security & HTTPS Enforcement Headers" not in content:
            content = re.sub(r'(<meta content="width=device-width, initial-scale=1.0" name="viewport"/>|<meta name="viewport"[^>]*>)', r'\1' + SECURITY_META_TAGS, content, count=1)

        fpath.write_text(content, encoding="utf-8")
        print(f"[{fname}] Saved with strict security headers.")

    print("\n✅ All pages fixed and secured successfully!")

if __name__ == "__main__":
    execute_security_and_header_fix()
