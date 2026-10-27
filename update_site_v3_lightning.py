import os
import sys
import re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PORTFOLIO_DIR = Path(r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev")

ALL_HTML_FILES = ["index.html", "projects.html", "aegis.html", "experience.html", "contact.html", "legal.html"]

def optimize_performance_in_file(content):
    # 1. Add preconnect / dns-prefetch if not present
    resource_hints = """
    <!-- Performance Optimization: Resource Hints for Ultra-Fast Initial Render -->
    <link rel="preconnect" href="https://cdn.tailwindcss.com" crossorigin>
    <link rel="preconnect" href="https://unpkg.com" crossorigin>
    <link rel="dns-prefetch" href="https://cdn.tailwindcss.com">
    <link rel="dns-prefetch" href="https://unpkg.com">
    <link rel="dns-prefetch" href="https://gumroad.com">
"""
    if "Resource Hints for Ultra-Fast Initial Render" not in content:
        content = re.sub(r'(<meta content="width=device-width, initial-scale=1.0" name="viewport"/>|<meta name="viewport"[^>]*>)', r'\1' + resource_hints, content, count=1)

    # 2. Add defer to non-critical scripts
    content = content.replace('<script src="https://unpkg.com/lucide@latest"></script>', '<script src="https://unpkg.com/lucide@latest" defer></script>')
    content = content.replace('<script src="phoenix_sentinel.js"></script>', '<script src="phoenix_sentinel.js" defer></script>')
    content = content.replace('<script src="aria_neural_engine.js"></script>', '<script src="aria_neural_engine.js" defer></script>')
    content = content.replace('<script src="https://gumroad.com/js/gumroad.js"></script>', '<script src="https://gumroad.com/js/gumroad.js" defer></script>')

    # 3. Use WebP for favicon and apple touch icon
    content = content.replace('href="emblem.jpg"', 'href="emblem.webp"')
    content = content.replace('type="image/jpeg" href="emblem.webp"', 'type="image/webp" href="emblem.webp"')

    # 4. Use WebP for img tags where applicable
    content = re.sub(r'src="emblem\.jpg"', 'src="emblem.webp" loading="lazy" decoding="async"', content)
    content = re.sub(r'src="logo\.jpg"', 'src="logo.webp" loading="lazy" decoding="async"', content)

    return content

# 6-Product Desktop Dropdown
NEW_DESKTOP_DROPDOWN = """                        <!-- Product 1: Deterministic State Kernel -->
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
                        </a>"""

# Mobile Navbar Menu
NEW_MOBILE_MENU = """        <!-- Product 1: Deterministic State Kernel -->
        <a class="block py-2 px-3 rounded-lg bg-emerald-50 text-emerald-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-emerald-600" data-lucide="cpu"></i>
                <span>Deterministic State Kernel&trade;</span>
            </div>
            <span class="bg-emerald-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$249</span>
        </a>
        <!-- Product 2: RQL Aegis -->
        <a class="block py-2 px-3 rounded-lg bg-cyan-50 text-cyan-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/rql-aegis/EARLYBIRD?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-cyan-600" data-lucide="shield"></i>
                <span>RQL Aegis&trade;</span>
            </div>
            <span class="bg-cyan-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$125</span>
        </a>
        <!-- Product 3: Veritas Dossier -->
        <a class="block py-2 px-3 rounded-lg bg-purple-50 text-purple-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/eucck/VERITAS?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-purple-600" data-lucide="file-check"></i>
                <span>Veritas Dossier&trade;</span>
            </div>
            <span class="bg-purple-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$249</span>
        </a>
        <!-- Product 4: Industrial Fragility Sentinel -->
        <a class="block py-2 px-3 rounded-lg bg-amber-50 text-amber-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/ivyiwh/SENTINEL?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-amber-700" data-lucide="factory"></i>
                <span>Industrial Sentinel&trade;</span>
            </div>
            <span class="bg-amber-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$299</span>
        </a>
        <!-- Product 5: RQL Conduit Engine -->
        <a class="block py-2 px-3 rounded-lg bg-sky-50 text-sky-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/rql-conduit?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-sky-600" data-lucide="network"></i>
                <span>RQL Conduit Engine&trade;</span>
            </div>
            <span class="bg-sky-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$60</span>
        </a>
        <!-- Product 6: ExpressBill POS -->
        <a class="block py-2 px-3 rounded-lg bg-teal-50 text-teal-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/expressbill?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-teal-600" data-lucide="receipt"></i>
                <span>ExpressBill POS&trade;</span>
            </div>
            <span class="bg-teal-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$49</span>
        </a>"""

CONDUIT_PROJECTS_CARD = """
            <!-- Project: RQL Conduit Bonding Engine™ Bare-Metal Rust Network Multiplexer -->
            <div class="project-card bg-slate-950 text-white rounded-2xl border-2 border-sky-500/40 overflow-hidden shadow-lg hover:border-sky-400 hover:shadow-xl transition duration-300 flex flex-col justify-between" data-category="network">
                <div class="p-8">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-sky-500/20 text-sky-300 text-xs font-semibold border border-sky-400/40 font-mono">
                            <span class="w-2 h-2 rounded-full bg-sky-400 animate-pulse"></span>
                            Multi-WAN Socket Multiplexer &bull; Rust Core
                        </span>
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-bold text-sky-300 bg-sky-950/90 border border-sky-500/40 px-2.5 py-0.5 rounded font-mono">Live at $60 / &#8377;4,999</span>
                            <span class="text-xs text-slate-500 line-through font-mono">$120</span>
                        </div>
                    </div>

                    <h3 class="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>RQL Conduit Bonding Engine&trade;</span>
                        <span class="text-xs font-mono text-sky-400 font-normal">v2.0-PROD</span>
                    </h3>
                    <p class="text-xs font-mono text-cyan-400 font-semibold mt-1">Local-First Multi-WAN SOCKS5 Gateway &amp; HTTP Range Slicer</p>
                    <p class="mt-3 text-slate-300 text-sm sm:text-base leading-relaxed">
                        An institutional-grade client-side network socket multiplexing gateway engineered in bare-metal Rust. Bonds Wi-Fi, 5G Mobile Hotspot, and Ethernet concurrently into a single virtual pipe (127.0.0.1:1080). Features sub-3ms zero-drop failover, real-time RTT jitter variance radar, and HTTP range-slicing with 100% local-first privacy. Zero remote VPN servers. Zero subscriptions.
                    </p>

                    <div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Failover Latency</div>
                            <div class="text-sm sm:text-base font-bold text-sky-400 font-mono mt-0.5">Sub-3ms</div>
                            <div class="text-[10px] text-slate-500">Zero Session Drops</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Core Engine</div>
                            <div class="text-sm sm:text-base font-bold text-emerald-400 font-mono mt-0.5">Bare-Metal Rust</div>
                            <div class="text-[10px] text-slate-500">Tokio &amp; Raw Sockets</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Privacy Architecture</div>
                            <div class="text-sm sm:text-base font-bold text-indigo-400 font-mono mt-0.5">100% Local-First</div>
                            <div class="text-[10px] text-slate-500">No Remote VPN Servers</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Pricing Model</div>
                            <div class="text-sm sm:text-base font-bold text-amber-400 font-mono mt-0.5">Perpetual License</div>
                            <div class="text-[10px] text-slate-500">Compare Speedify $90/yr</div>
                        </div>
                    </div>

                    <div class="mt-6 space-y-2 text-xs text-slate-300">
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-sky-400 flex-shrink-0"></i>
                            <span>Sun Tzu Jitter Radar &bull; Continuously estimates RTT variance (2.5&sigma;) to anticipate carrier failure before packet loss occurs</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-sky-400 flex-shrink-0"></i>
                            <span>Multi-WAN SOCKS5 Gateway &bull; Bonds up to 4 simultaneous network interfaces over local loopback (127.0.0.1:1080)</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-sky-400 flex-shrink-0"></i>
                            <span>11-Point Invariant Regression Suite &bull; Comprehensive unit verification validating socket state transition invariants</span>
                        </div>
                    </div>
                </div>

                <div class="p-8 pt-0 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-4 mt-4">
                    <div class="flex flex-col gap-1">
                        <div class="flex items-center gap-2">
                            <span class="text-xs text-slate-400 font-mono">License:</span>
                            <span class="text-xs font-mono font-bold text-sky-400 bg-sky-950/80 border border-sky-500/30 px-2 py-0.5 rounded">Perpetual Single PC ($60) / Studio ($120)</span>
                        </div>
                        <span class="text-[11px] text-sky-400 font-mono">⚡ Zero Recurring Subscriptions &bull; 100% Offline Standalone Binaries</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <a href="https://quantify17.gumroad.com/l/rql-conduit" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3.5 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                            Product Details
                        </a>
                        <a href="https://quantify17.gumroad.com/l/rql-conduit?wanted=true" target="_blank" rel="noopener noreferrer" class="text-xs font-bold text-white bg-sky-600 hover:bg-sky-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-sky-600/20">
                            <i data-lucide="zap" class="w-3.5 h-3.5 text-white"></i>
                            <span>Instant Access ($60)</span>
                        </a>
                    </div>
                </div>
            </div>
"""

EXPRESSBILL_PROJECTS_CARD = """
            <!-- Project: ExpressBill POS™ Offline-First Retail Suite & Mobile PWA -->
            <div class="project-card bg-slate-950 text-white rounded-2xl border-2 border-teal-500/40 overflow-hidden shadow-lg hover:border-teal-400 hover:shadow-xl transition duration-300 flex flex-col justify-between" data-category="retail">
                <div class="p-8">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-teal-500/20 text-teal-300 text-xs font-semibold border border-teal-400/40 font-mono">
                            <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
                            100% Offline Retail POS &bull; Mobile PWA
                        </span>
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-bold text-teal-300 bg-teal-950/90 border border-teal-500/40 px-2.5 py-0.5 rounded font-mono">Live at $49 / &#8377;3,999</span>
                            <span class="text-xs text-slate-500 line-through font-mono">$149</span>
                        </div>
                    </div>

                    <h3 class="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>ExpressBill POS&trade;</span>
                        <span class="text-xs font-mono text-teal-400 font-normal">v2.0-PROD</span>
                    </h3>
                    <p class="text-xs font-mono text-emerald-400 font-semibold mt-1">Offline-First Retail Workstation, Dynamic UPI QR &amp; WhatsApp Invoices</p>
                    <p class="mt-3 text-slate-300 text-sm sm:text-base leading-relaxed">
                        An ultra-fast, offline-first retail billing suite engineered for grocery stores, cafes, pharmacies, and boutiques. Powered by an embedded redb storage engine, ring up 20 items in under 5 seconds with zero internet connection. Features real-time dynamic UPI QR code generation on the checkout counter screen, 1-click WhatsApp itemized tax invoice dispatch, and universal ESC/POS thermal printing.
                    </p>

                    <div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Checkout Speed</div>
                            <div class="text-sm sm:text-base font-bold text-teal-400 font-mono mt-0.5">&lt; 500ms</div>
                            <div class="text-[10px] text-slate-500">Instant Barcode Beep</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Database</div>
                            <div class="text-sm sm:text-base font-bold text-cyan-400 font-mono mt-0.5">Embedded Redb</div>
                            <div class="text-[10px] text-slate-500">100% Private Offline</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Payments</div>
                            <div class="text-sm sm:text-base font-bold text-purple-400 font-mono mt-0.5">Dynamic UPI QR</div>
                            <div class="text-[10px] text-slate-500">Auto-Encodes Amount</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Mobile POS</div>
                            <div class="text-sm sm:text-base font-bold text-amber-400 font-mono mt-0.5">Touch PWA</div>
                            <div class="text-[10px] text-slate-500">iPhone / iPad / Android</div>
                        </div>
                    </div>

                    <div class="mt-6 space-y-2 text-xs text-slate-300">
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-teal-400 flex-shrink-0"></i>
                            <span>Dynamic Real-Time UPI QR &bull; Renders exact bill amount QR on counter screen for instant scan via PhonePe/GPay/Paytm</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-teal-400 flex-shrink-0"></i>
                            <span>1-Click WhatsApp Invoices &bull; Dispatches itemized digital tax invoices directly to customer chat, saving on paper rolls</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-teal-400 flex-shrink-0"></i>
                            <span>Zero Monthly Subscriptions &bull; Pay once, own perpetual workstation license with zero cloud fees or SaaS transaction cuts</span>
                        </div>
                    </div>
                </div>

                <div class="p-8 pt-0 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-4 mt-4">
                    <div class="flex flex-col gap-1">
                        <div class="flex items-center gap-2">
                            <span class="text-xs text-slate-400 font-mono">Deal:</span>
                            <span class="text-xs font-mono font-bold text-teal-400 bg-teal-950/80 border border-teal-500/30 px-2 py-0.5 rounded">Single Counter ($49) / 3-Counter Pack ($89)</span>
                        </div>
                        <span class="text-[11px] text-teal-400 font-mono">🏷️ Lifetime License &bull; Thermal Printer Ready (ESC/POS 58mm/80mm)</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <a href="https://quantify17.gumroad.com/l/expressbill" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3.5 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                            Product Details
                        </a>
                        <a href="https://quantify17.gumroad.com/l/expressbill?wanted=true" target="_blank" rel="noopener noreferrer" class="text-xs font-bold text-white bg-teal-600 hover:bg-teal-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-teal-600/20">
                            <i data-lucide="zap" class="w-3.5 h-3.5 text-white"></i>
                            <span>Claim Lifetime Deal ($49)</span>
                        </a>
                    </div>
                </div>
            </div>
"""

INDEX_CONDUIT_HERO_CARD = """
        <!-- Flagship 3: RQL Conduit Bonding Engine™ -->
        <div class="rounded-2xl bg-gradient-to-br from-slate-950 via-slate-900 to-sky-950 border-2 border-sky-500/50 shadow-xl p-6 sm:p-7 flex flex-col justify-between text-white hover:border-sky-400 transition duration-300">
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="bg-sky-500/20 text-sky-300 border border-sky-400/50 text-[10px] px-2.5 py-1 rounded-lg font-mono font-bold uppercase tracking-wider flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-sky-400 animate-pulse"></span>
                        Commercial Rust Networking Engine
                    </span>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-mono font-bold text-sky-300 bg-sky-950 border border-sky-500/40 px-2 py-0.5 rounded">Live at $60 / &#8377;4,999</span>
                        <span class="text-xs text-slate-500 line-through font-mono">$120</span>
                    </div>
                </div>

                <div>
                    <h3 class="text-xl sm:text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>RQL Conduit Bonding Engine&trade;</span>
                        <span class="text-xs font-mono text-sky-400 font-normal">v2.0 (PROD)</span>
                    </h3>
                    <p class="text-xs font-mono text-cyan-400 font-semibold mt-1">Bare-Metal Rust Multi-WAN SOCKS5 Gateway &bull; Sub-3ms Failover</p>
                </div>

                <p class="text-slate-300 text-sm leading-relaxed">
                    A 100% local-first network socket multiplexer written in bare-metal Rust. Bonds Wi-Fi, 5G Mobile Hotspot, and Ethernet concurrently into a single resilient virtual pipe (<code class="text-sky-300 font-mono">127.0.0.1:1080</code>) with sub-3ms zero-drop failover, real-time RTT jitter variance radar, and HTTP range-slicing. Strictly <b>zero remote VPN servers, zero packet logging, and &#8377;0 recurring SaaS fees</b>.
                </p>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-center pt-1 font-mono">
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Failover</div>
                        <div class="text-sm font-bold text-sky-400 mt-0.5">Sub-3ms</div>
                        <div class="text-[9px] text-slate-500">Zero Drops</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Engine</div>
                        <div class="text-sm font-bold text-emerald-400 mt-0.5">Rust Core</div>
                        <div class="text-[9px] text-slate-500">Tokio Sockets</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Privacy</div>
                        <div class="text-sm font-bold text-indigo-400 mt-0.5">100% Local</div>
                        <div class="text-[9px] text-slate-500">No VPN Clouds</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Pricing</div>
                        <div class="text-sm font-bold text-amber-400 mt-0.5">Perpetual</div>
                        <div class="text-[9px] text-slate-500">No SaaS Fees</div>
                    </div>
                </div>
            </div>

            <div class="pt-6 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3 mt-4">
                <div class="flex flex-col">
                    <span class="text-xs text-sky-300 font-mono font-bold">Perpetual Lifetime License</span>
                    <span class="text-[10px] text-slate-400 font-mono">Includes Windows Desktop GUI + Rust DLL Core</span>
                </div>
                <div class="flex items-center gap-2">
                    <a href="https://quantify17.gumroad.com/l/rql-conduit" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                        Details
                    </a>
                    <a href="https://quantify17.gumroad.com/l/rql-conduit?wanted=true" target="_blank" rel="noopener noreferrer" class="text-xs font-bold text-white bg-sky-600 hover:bg-sky-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-sky-600/20">
                        <i data-lucide="zap" class="w-3.5 h-3.5"></i>
                        <span>Claim License ($60)</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- Flagship 4: ExpressBill POS™ -->
        <div class="rounded-2xl bg-gradient-to-br from-slate-950 via-slate-900 to-teal-950 border-2 border-teal-500/50 shadow-xl p-6 sm:p-7 flex flex-col justify-between text-white hover:border-teal-400 transition duration-300">
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="bg-teal-500/20 text-teal-300 border border-teal-400/50 text-[10px] px-2.5 py-1 rounded-lg font-mono font-bold uppercase tracking-wider flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
                        Commercial Offline Retail POS
                    </span>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-mono font-bold text-teal-300 bg-teal-950 border border-teal-500/40 px-2 py-0.5 rounded">Live at $49 / &#8377;3,999</span>
                        <span class="text-xs text-slate-500 line-through font-mono">$149</span>
                    </div>
                </div>

                <div>
                    <h3 class="text-xl sm:text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>ExpressBill POS&trade;</span>
                        <span class="text-xs font-mono text-teal-400 font-normal">v2.0 (PROD)</span>
                    </h3>
                    <p class="text-xs font-mono text-emerald-400 font-semibold mt-1">100% Offline Retail Suite &bull; Dynamic Real-Time UPI QR &bull; Mobile PWA</p>
                </div>

                <p class="text-slate-300 text-sm leading-relaxed">
                    An ultra-fast checkout counter workstation for retail shops, cafes, pharmacies, and boutiques. Powered by an embedded redb storage engine, ring up 20 items in under 5 seconds with zero internet. Displays dynamic real-time UPI QR codes directly on the customer screen for 1-second PhonePe/GPay scans, sends WhatsApp tax receipts, and prints thermal receipts with strictly <b>&#8377;0 monthly SaaS fees</b>.
                </p>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-center pt-1 font-mono">
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Checkout</div>
                        <div class="text-sm font-bold text-teal-400 mt-0.5">&lt; 500ms</div>
                        <div class="text-[9px] text-slate-500">Barcode Scan</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Storage</div>
                        <div class="text-sm font-bold text-cyan-400 mt-0.5">Embedded Redb</div>
                        <div class="text-[9px] text-slate-500">Offline Local DB</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Payments</div>
                        <div class="text-sm font-bold text-purple-400 mt-0.5">Dynamic UPI</div>
                        <div class="text-[9px] text-slate-500">Instant Scan</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Mobile POS</div>
                        <div class="text-sm font-bold text-amber-400 mt-0.5">Touch PWA</div>
                        <div class="text-[9px] text-slate-500">iOS / Android</div>
                    </div>
                </div>
            </div>

            <div class="pt-6 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3 mt-4">
                <div class="flex flex-col">
                    <span class="text-xs text-teal-300 font-mono font-bold">Lifetime Store License</span>
                    <span class="text-[10px] text-slate-400 font-mono">Windows EXE + Offline Mobile PWA Suite</span>
                </div>
                <div class="flex items-center gap-2">
                    <a href="https://quantify17.gumroad.com/l/expressbill" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                        Details
                    </a>
                    <a href="https://quantify17.gumroad.com/l/expressbill?wanted=true" target="_blank" rel="noopener noreferrer" class="text-xs font-bold text-white bg-teal-600 hover:bg-teal-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-teal-600/20">
                        <i data-lucide="zap" class="w-3.5 h-3.5"></i>
                        <span>Claim Lifetime ($49)</span>
                    </a>
                </div>
            </div>
        </div>
"""

def update_all_html_files():
    print("=" * 70)
    print("⚡ UPDATING PORTFOLIO SUITE: SPEED OPTIMIZATIONS & NEW FLAGSHIP PRODUCTS")
    print("=" * 70)

    for fname in ALL_HTML_FILES:
        fpath = PORTFOLIO_DIR / fname
        if not fpath.exists():
            print(f"Skipping {fname} (not found)")
            continue

        content = fpath.read_text(encoding="utf-8")
        
        # 1. Performance optimization (Resource hints, defer scripts, WebP)
        content = optimize_performance_in_file(content)

        # 2. Update Desktop Navbar Dropdown (replace old 4 products with new 6 products)
        # Find start of dropdown
        m_drop = re.search(r'<!-- Product 1: Deterministic State Kernel -->.*?<!-- Product 4: Industrial Fragility Sentinel -->.*?(?=</div>\s*</div>\s*</div>|\s*<div class="border-t border-slate-100)', content, re.DOTALL)
        if m_drop:
            content = content[:m_drop.start()] + NEW_DESKTOP_DROPDOWN + content[m_drop.end():]
            print(f"[{fname}] Successfully updated Desktop Navigation Dropdown (6 products).")
        else:
            # Try replacing existing new_dropdown if already partially matching
            m_drop2 = re.search(r'<!-- Product 1: Deterministic State Kernel -->.*?(?=<!-- Product 5: RQL Conduit Bonding Engine -->|</div>\s*</div>\s*</div>)', content, re.DOTALL)
            if m_drop2 and "RQL Conduit Engine" not in content[:m_drop2.end() + 500]:
                content = content[:m_drop2.start()] + NEW_DESKTOP_DROPDOWN + content[m_drop2.end():]
                print(f"[{fname}] Updated Desktop Navigation Dropdown via fallback pattern.")

        # 3. Update Mobile Navbar Menu
        m_mob = re.search(r'<!-- Product 1: Deterministic State Kernel -->.*?<!-- Product 4: Industrial Fragility Sentinel -->.*?</a>', content, re.DOTALL)
        if m_mob:
            content = content[:m_mob.start()] + NEW_MOBILE_MENU + content[m_mob.end():]
            print(f"[{fname}] Successfully updated Mobile Navigation Menu (6 products).")

        # 4. In projects.html, insert the two new cards before AegisDB In-Memory Engine
        if fname == "projects.html":
            if "RQL Conduit Bonding Engine" not in content:
                m_proj = re.search(r'<!-- Project: AegisDB In-Memory Engine -->', content)
                if m_proj:
                    content = content[:m_proj.start()] + CONDUIT_PROJECTS_CARD + "\n" + EXPRESSBILL_PROJECTS_CARD + "\n" + content[m_proj.start():]
                    print("[projects.html] Inserted RQL Conduit & ExpressBill product cards.")
                else:
                    print("[projects.html] Warning: could not find AegisDB insertion anchor.")
            else:
                print("[projects.html] RQL Conduit card already present.")

        # 5. In index.html, insert the two new cards into the Flagship grid
        if fname == "index.html":
            if "RQL Conduit Bonding Engine" not in content:
                # Find the end of Flagship 2 (AegisOps) or end of the grid
                # Look for AegisOps card closing
                m_flag = re.search(r'<!-- Flagship 2: AegisOps.*?</div>\s*</div>\s*(?=<!-- Flagship|</div>\s*</div>\s*</section>|\s*<!-- Interactive Quantitative Lab)', content, re.DOTALL)
                if m_flag:
                    content = content[:m_flag.end()] + "\n" + INDEX_CONDUIT_HERO_CARD + "\n" + content[m_flag.end():]
                    print("[index.html] Inserted RQL Conduit & ExpressBill into Flagship Grid.")
                else:
                    # Alternative anchor: inside interactive quantitative lab
                    m_lab = re.search(r'<!-- Project: Deterministic State Kernel.*?</div>\s*</div>\s*(?=<!-- Project: AegisOps|</div>\s*</div>\s*</div>)', content, re.DOTALL)
                    if m_lab:
                        content = content[:m_lab.end()] + "\n" + INDEX_CONDUIT_HERO_CARD + "\n" + content[m_lab.end():]
                        print("[index.html] Inserted RQL Conduit & ExpressBill via Lab Grid anchor.")
            else:
                print("[index.html] RQL Conduit already present in index.html.")

        fpath.write_text(content, encoding="utf-8")
        print(f"[{fname}] Saved with UTF-8 encoding.")

    print("\n✅ All portfolio HTML files upgraded with maximum performance and product updates!")

if __name__ == "__main__":
    update_all_html_files()
