import os
import sys
import re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PORTFOLIO_DIR = Path(r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev")
ALL_HTML_FILES = ["index.html", "projects.html", "aegis.html", "experience.html", "contact.html", "legal.html"]

# 1. Single Unified Rotating Top Announcement Bar
SINGLE_TOP_BAR = """<!-- Single Unified Institutional Status & Rotating Announcement Bar -->
<div class="bg-slate-950 text-slate-300 text-xs py-1.5 px-4 font-mono tracking-tight border-b border-slate-800/80 relative z-50">
    <div class="max-w-7xl mx-auto w-full flex items-center justify-between gap-4">
        <div id="live-ticker-container" class="flex items-center gap-2 truncate">
            <span class="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-pulse shrink-0"></span>
            <span id="ticker-label" class="text-sky-400 font-bold uppercase text-[10px] tracking-wider shrink-0">⭐ NEW RELEASE:</span>
            <span id="ticker-content" class="text-slate-200 text-xs truncate transition-opacity duration-300">
                <strong>RQL Conduit Bonding Engine™</strong> &bull; Bare-Metal Rust Multi-WAN is <span class="text-sky-400 font-bold">$60 / &#8377;4,999</span>
            </span>
        </div>
        <div class="flex items-center gap-3 shrink-0 text-xs font-sans">
            <a id="ticker-action" href="https://quantify17.gumroad.com/l/RQLConduit" data-gumroad-single-product="true" class="gumroad-button text-sky-400 hover:text-sky-300 font-bold underline transition flex items-center gap-1 font-mono">
                <span>Instant Checkout</span>
                <i class="w-3 h-3" data-lucide="arrow-right"></i>
            </a>
            <span class="text-slate-700 hidden md:inline">|</span>
            <span class="text-slate-400 hidden md:inline font-mono text-[11px]">Sub-3ms Failover &bull; 100% Local-First</span>
        </div>
    </div>
</div>"""

# 2. Desktop Dropdown with EXACT Gumroad URLs & Inbuilt Overlay triggers
DESKTOP_DROPDOWN_LINKS = """                        <!-- Product 1: Deterministic State Kernel -->
                        <a href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE?wanted=true" data-gumroad-single-product="true" class="gumroad-button flex items-start gap-2.5 p-2 rounded-xl hover:bg-emerald-50/80 transition group/item">
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
                        <a href="https://quantify17.gumroad.com/l/rql-aegis/EARLYBIRD?wanted=true" data-gumroad-single-product="true" class="gumroad-button flex items-start gap-2.5 p-2 rounded-xl hover:bg-cyan-50/80 transition group/item">
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
                        <a href="https://quantify17.gumroad.com/l/eucck/VERITAS?wanted=true" data-gumroad-single-product="true" class="gumroad-button flex items-start gap-2.5 p-2 rounded-xl hover:bg-purple-50/80 transition group/item">
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
                        <a href="https://quantify17.gumroad.com/l/ivyiwh/SENTINEL?wanted=true" data-gumroad-single-product="true" class="gumroad-button flex items-start gap-2.5 p-2 rounded-xl hover:bg-amber-50/80 transition group/item">
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
                        <a href="https://quantify17.gumroad.com/l/RQLConduit" data-gumroad-single-product="true" class="gumroad-button flex items-start gap-2.5 p-2 rounded-xl hover:bg-sky-50/80 transition group/item">
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
                        <a href="https://quantify17.gumroad.com/l/ExpressBill" data-gumroad-single-product="true" class="gumroad-button flex items-start gap-2.5 p-2 rounded-xl hover:bg-teal-50/80 transition group/item">
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

# 3. Mobile Navigation Menu with EXACT Gumroad URLs
MOBILE_MENU_LINKS = """        <!-- Product 1: Deterministic State Kernel -->
        <a class="gumroad-button block py-2 px-3 rounded-lg bg-emerald-50 text-emerald-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE?wanted=true" data-gumroad-single-product="true">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-emerald-600" data-lucide="cpu"></i>
                <span>Deterministic State Kernel&trade;</span>
            </div>
            <span class="bg-emerald-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$249</span>
        </a>
        <!-- Product 2: RQL Aegis -->
        <a class="gumroad-button block py-2 px-3 rounded-lg bg-cyan-50 text-cyan-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/rql-aegis/EARLYBIRD?wanted=true" data-gumroad-single-product="true">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-cyan-600" data-lucide="shield"></i>
                <span>RQL Aegis&trade;</span>
            </div>
            <span class="bg-cyan-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$125</span>
        </a>
        <!-- Product 3: Veritas Dossier -->
        <a class="gumroad-button block py-2 px-3 rounded-lg bg-purple-50 text-purple-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/eucck/VERITAS?wanted=true" data-gumroad-single-product="true">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-purple-600" data-lucide="file-check"></i>
                <span>Veritas Dossier&trade;</span>
            </div>
            <span class="bg-purple-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$249</span>
        </a>
        <!-- Product 4: Industrial Fragility Sentinel -->
        <a class="gumroad-button block py-2 px-3 rounded-lg bg-amber-50 text-amber-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/ivyiwh/SENTINEL?wanted=true" data-gumroad-single-product="true">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-amber-600" data-lucide="factory"></i>
                <span>Industrial Fragility Sentinel&trade;</span>
            </div>
            <span class="bg-amber-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$299</span>
        </a>
        <!-- Product 5: RQL Conduit Engine -->
        <a class="gumroad-button block py-2 px-3 rounded-lg bg-sky-50 text-sky-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/RQLConduit" data-gumroad-single-product="true">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-sky-600" data-lucide="network"></i>
                <span>RQL Conduit Engine&trade;</span>
            </div>
            <span class="bg-sky-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$60</span>
        </a>
        <!-- Product 6: ExpressBill POS -->
        <a class="gumroad-button block py-2 px-3 rounded-lg bg-teal-50 text-teal-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/ExpressBill" data-gumroad-single-product="true">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-teal-600" data-lucide="receipt"></i>
                <span>ExpressBill POS&trade;</span>
            </div>
            <span class="bg-teal-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$49</span>
        </a>"""

# 4. RQL Conduit Card for projects.html
PROJECTS_CONDUIT_CARD = """
            <!-- Project: RQL Conduit Bonding Engine™ Bare-Metal Rust Network Multiplexer -->
            <div class="project-card hover-lift-card bg-slate-950 text-white rounded-2xl border-2 border-sky-500/40 overflow-hidden shadow-lg hover:border-sky-400 hover:shadow-xl transition duration-300 flex flex-col justify-between" data-category="network">
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

                    <div class="mb-4 rounded-xl overflow-hidden border border-slate-800 bg-slate-900/60">
                        <img src="05_rql_conduit_bonding_engine_1080p.webp" alt="RQL Conduit Bonding Engine Architecture" class="w-full h-48 sm:h-56 object-cover hover:scale-105 transition duration-500" loading="lazy" />
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
                        <a href="https://quantify17.gumroad.com/l/RQLConduit" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3.5 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                            Product Details
                        </a>
                        <a href="https://quantify17.gumroad.com/l/RQLConduit" data-gumroad-single-product="true" class="gumroad-button text-xs font-bold text-white bg-sky-600 hover:bg-sky-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-sky-600/30 btn-spring shimmer-badge">
                            <i data-lucide="zap" class="w-3.5 h-3.5 text-white"></i>
                            <span>Instant Access ($60)</span>
                        </a>
                    </div>
                </div>
            </div>
"""

# 5. ExpressBill Card for projects.html
PROJECTS_EXPRESSBILL_CARD = """
            <!-- Project: ExpressBill POS™ Offline-First Retail Suite & Mobile PWA -->
            <div class="project-card hover-lift-card bg-slate-950 text-white rounded-2xl border-2 border-teal-500/40 overflow-hidden shadow-lg hover:border-teal-400 hover:shadow-xl transition duration-300 flex flex-col justify-between" data-category="retail">
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

                    <div class="mb-4 rounded-xl overflow-hidden border border-slate-800 bg-slate-900/60">
                        <img src="ExpressBill_POS_Commercial_Hero.webp" alt="ExpressBill POS Commercial Suite" class="w-full h-48 sm:h-56 object-cover hover:scale-105 transition duration-500" loading="lazy" />
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
                        <a href="https://quantify17.gumroad.com/l/ExpressBill" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3.5 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                            Product Details
                        </a>
                        <a href="https://quantify17.gumroad.com/l/ExpressBill" data-gumroad-single-product="true" class="gumroad-button text-xs font-bold text-white bg-teal-600 hover:bg-teal-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-teal-600/30 btn-spring shimmer-badge">
                            <i data-lucide="zap" class="w-3.5 h-3.5 text-white"></i>
                            <span>Claim Lifetime Deal ($49)</span>
                        </a>
                    </div>
                </div>
            </div>
"""

# 6. Flagship Cards for index.html
INDEX_FLAGSHIP_CONDUIT = """
        <!-- Flagship 5: RQL Conduit Bonding Engine™ -->
        <div class="hover-lift-card rounded-2xl bg-gradient-to-br from-slate-950 via-slate-900 to-sky-950 border-2 border-sky-500/50 shadow-xl p-6 sm:p-7 flex flex-col justify-between text-white hover:border-sky-400 transition duration-300 relative overflow-hidden group">
            <div class="absolute -top-24 -right-24 w-48 h-48 bg-sky-500/10 rounded-full blur-2xl group-hover:bg-sky-500/20 transition duration-500 pointer-events-none"></div>
            <div class="space-y-4 relative z-10">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="bg-sky-500/20 text-sky-300 border border-sky-400/50 text-[10px] px-2.5 py-1 rounded-lg font-mono font-bold uppercase tracking-wider flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-sky-400 animate-pulse"></span>
                        Commercial Rust Networking Engine
                    </span>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-mono font-bold text-sky-300 bg-sky-950/90 border border-sky-500/40 px-2 py-0.5 rounded">Live at $60 / &#8377;4,999</span>
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

            <div class="pt-6 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3 mt-4 relative z-10">
                <div class="flex flex-col">
                    <span class="text-xs text-sky-300 font-mono font-bold">Perpetual Lifetime License</span>
                    <span class="text-[10px] text-slate-400 font-mono">Includes Windows Desktop GUI + Rust DLL Core</span>
                </div>
                <div class="flex items-center gap-2">
                    <a href="https://quantify17.gumroad.com/l/RQLConduit" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                        Details
                    </a>
                    <a href="https://quantify17.gumroad.com/l/RQLConduit" data-gumroad-single-product="true" class="gumroad-button text-xs font-bold text-white bg-sky-600 hover:bg-sky-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-sky-600/30 btn-spring shimmer-badge">
                        <i data-lucide="zap" class="w-3.5 h-3.5 text-white"></i>
                        <span>Claim License ($60)</span>
                    </a>
                </div>
            </div>
        </div>
"""

INDEX_FLAGSHIP_EXPRESSBILL = """
        <!-- Flagship 6: ExpressBill POS™ -->
        <div class="hover-lift-card rounded-2xl bg-gradient-to-br from-slate-950 via-slate-900 to-teal-950 border-2 border-teal-500/50 shadow-xl p-6 sm:p-7 flex flex-col justify-between text-white hover:border-teal-400 transition duration-300 relative overflow-hidden group">
            <div class="absolute -top-24 -right-24 w-48 h-48 bg-teal-500/10 rounded-full blur-2xl group-hover:bg-teal-500/20 transition duration-500 pointer-events-none"></div>
            <div class="space-y-4 relative z-10">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="bg-teal-500/20 text-teal-300 border border-teal-400/50 text-[10px] px-2.5 py-1 rounded-lg font-mono font-bold uppercase tracking-wider flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
                        Commercial Offline Retail POS
                    </span>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-mono font-bold text-teal-300 bg-teal-950/90 border border-teal-500/40 px-2 py-0.5 rounded">Live at $49 / &#8377;3,999</span>
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

            <div class="pt-6 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3 mt-4 relative z-10">
                <div class="flex flex-col">
                    <span class="text-xs text-teal-300 font-mono font-bold">Lifetime Store License</span>
                    <span class="text-[10px] text-slate-400 font-mono">Windows EXE + Offline Mobile PWA Suite</span>
                </div>
                <div class="flex items-center gap-2">
                    <a href="https://quantify17.gumroad.com/l/ExpressBill" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                        Details
                    </a>
                    <a href="https://quantify17.gumroad.com/l/ExpressBill" data-gumroad-single-product="true" class="gumroad-button text-xs font-bold text-white bg-teal-600 hover:bg-teal-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-teal-600/30 btn-spring shimmer-badge">
                        <i data-lucide="zap" class="w-3.5 h-3.5 text-white"></i>
                        <span>Claim Lifetime ($49)</span>
                    </a>
                </div>
            </div>
        </div>
"""

def execute_v5_upgrade():
    print("=" * 70)
    print("🚀 EXECUTING V5 MASTER LIVELY OVERHAUL & INBUILT GUMROAD SUITE")
    print("=" * 70)

    for fname in ALL_HTML_FILES:
        fpath = PORTFOLIO_DIR / fname
        if not fpath.exists():
            continue

        content = fpath.read_text(encoding="utf-8")

        # -------------------------------------------------------------
        # STEP 1: FIX DUPLICATE TOP ANNOUNCEMENT BAR
        # -------------------------------------------------------------
        # Find everything between <body...> and <header
        body_m = re.search(r'<body[^>]*>', content)
        header_m = re.search(r'<header[^>]*>', content)
        if body_m and header_m:
            between = content[body_m.end():header_m.start()]
            # Look for any announcement bars inside 'between'
            # Remove all existing announcement bars from 'between'
            cleaned_between = re.sub(r'<!--\s*(?:Single Unified|Unified Top)[^>]*-->\s*<div class="bg-slate-950.*?</div>\s*</div>\s*</div>', '', between, flags=re.DOTALL)
            cleaned_between = re.sub(r'<div class="bg-slate-950 text-slate-300 text-xs py-1.5.*?</div>\s*</div>\s*</div>', '', cleaned_between, flags=re.DOTALL)
            cleaned_between = re.sub(r'<!-- STICKY NAVBAR -->', '', cleaned_between)
            cleaned_between = re.sub(r'<!-- STICKY INSTITUTIONAL NAVBAR -->', '', cleaned_between)
            
            # Now insert EXACTLY ONE single top announcement bar right before <header
            new_between = cleaned_between.strip() + "\n\n" + SINGLE_TOP_BAR + "\n"
            content = content[:body_m.end()] + "\n" + new_between + content[header_m.start():]
            print(f"[{fname}] Fixed top announcement bar (strictly 1 single bar).")

        # -------------------------------------------------------------
        # STEP 2: UPDATE NAVIGATION DROPDOWN & MOBILE MENU
        # -------------------------------------------------------------
        # Update desktop dropdown links
        m_drop = re.search(r'<!-- Product 1: Deterministic State Kernel -->.*?<!-- Product 6: ExpressBill POS -->.*?</a>', content, re.DOTALL)
        if m_drop:
            content = content[:m_drop.start()] + DESKTOP_DROPDOWN_LINKS + content[m_drop.end():]
            print(f"[{fname}] Updated Desktop Dropdown with inbuilt Gumroad links.")

        # Update mobile menu links
        m_mob = re.search(r'<!-- Product 1: Deterministic State Kernel -->.*?<!-- Product 6: ExpressBill POS -->.*?</a>', content[header_m.start():], re.DOTALL)
        if m_mob:
            abs_start = header_m.start() + m_mob.start()
            abs_end = header_m.start() + m_mob.end()
            content = content[:abs_start] + MOBILE_MENU_LINKS + content[abs_end:]
            print(f"[{fname}] Updated Mobile Menu with inbuilt Gumroad links.")

        # -------------------------------------------------------------
        # STEP 3: REPLACE ANY OLD GUMROAD URL CASING
        # -------------------------------------------------------------
        content = content.replace("https://quantify17.gumroad.com/l/rql-conduit", "https://quantify17.gumroad.com/l/RQLConduit")
        content = content.replace("https://quantify17.gumroad.com/l/expressbill", "https://quantify17.gumroad.com/l/ExpressBill")

        # -------------------------------------------------------------
        # STEP 4: INSERT RQL CONDUIT & EXPRESSBILL CARDS IN PROJECTS.HTML
        # -------------------------------------------------------------
        if fname == "projects.html":
            if "Project: RQL Conduit Bonding Engine" not in content:
                # Find AegisDB anchor
                m_aegisdb = re.search(r'<!-- Project: AegisDB In-Memory Engine -->', content)
                if m_aegisdb:
                    content = content[:m_aegisdb.start()] + PROJECTS_CONDUIT_CARD + "\n" + PROJECTS_EXPRESSBILL_CARD + "\n\n" + content[m_aegisdb.start():]
                    print("[projects.html] Inserted RQL Conduit & ExpressBill Project Cards.")
                else:
                    print("[projects.html] Warning: AegisDB anchor not found!")
            else:
                print("[projects.html] RQL Conduit card already in projects.html.")

        # -------------------------------------------------------------
        # STEP 5: INSERT RQL CONDUIT & EXPRESSBILL CARDS IN INDEX.HTML
        # -------------------------------------------------------------
        if fname == "index.html":
            if "Flagship 5: RQL Conduit Bonding Engine" not in content:
                # Find Flagship 4 ending
                m_flag4 = re.search(r'<!-- Flagship 4: Industrial Fragility Sentinel.*?</div>\s*</div>\s*(?=\s*</div>\s*</div>\s*</div>|\s*</section>)', content, re.DOTALL)
                if m_flag4:
                    content = content[:m_flag4.end()] + "\n" + INDEX_FLAGSHIP_CONDUIT + "\n" + INDEX_FLAGSHIP_EXPRESSBILL + "\n" + content[m_flag4.end():]
                    print("[index.html] Inserted Flagship 5 (Conduit) & Flagship 6 (ExpressBill) cards.")
                else:
                    print("[index.html] Warning: Flagship 4 anchor not found!")
            else:
                print("[index.html] Flagship 5 (Conduit) already in index.html.")

        fpath.write_text(content, encoding="utf-8")
        print(f"[{fname}] Saved successfully.")

    print("\n✅ All pages upgraded with single top bar, cards, and inbuilt Gumroad checkouts!")

if __name__ == "__main__":
    execute_v5_upgrade()
