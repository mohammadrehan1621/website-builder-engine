import re
from pathlib import Path

portfolio_dir = Path(r"c:\Users\rehan\Desktop\website_builder\Deployed_Websites\mohammadrehan.pages.dev")
projects_file = portfolio_dir / "projects.html"
index_file = portfolio_dir / "index.html"

# New Rich Projects HTML Cards for projects.html
PROJECTS_CARDS = """
            <!-- Project 0: Aegis Crypto Bot (Asynchronous Spot Microstructure Execution Engine) -->
            <div class="project-card bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:border-slate-400 hover:shadow-md transition duration-300 flex flex-col justify-between" data-category="ai">
                <div class="p-8">
                    <div class="flex items-center justify-between mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-semibold border border-blue-200">
                            <span class="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span>
                            Production Microstructure Engine
                        </span>
                        <span class="text-xs text-slate-400 font-medium">Binance 24/7 Spot & Microsecond Telemetry</span>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 tracking-tight">Aegis Crypto Engine — Asynchronous Spot Microstructure Engine</h3>
                    <p class="mt-3 text-slate-600 text-sm sm:text-base leading-relaxed">
                        An asynchronous, ultra-low-latency spot execution engine engineered for continuous 24/7 Binance operation. Features zero-allocation in-memory ring buffers (0.97 µs trade print throughput), 20-level Weighted Order Book Imbalance (9.44 µs WOBI), a mathematically proven 1X Spot capital preservation invariant (0.00% liquidation risk), Brownian noise-filtered ATR stops, 20-minute Time-Decay scratch exits, and SQLite WAL zero-loss persistence.
                    </p>
                    <div class="mt-6 space-y-2">
                        <h4 class="text-xs font-semibold uppercase tracking-wider text-slate-400">Architectural Highlights</h4>
                        <ul class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm text-slate-700">
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Microsecond Order Book WOBI (9.44 µs) & CVD (0.97 µs)
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                1X Pure Spot Model (Strict 0.00% Liquidation Risk)
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Noise-Filtered Dynamic ATR Stops & 20-Min Time-Decay Scratch
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                78/78 Passing Adversarial Invariants & Linux systemd Integration
                            </li>
                        </ul>
                    </div>
                    <div class="mt-6 flex flex-wrap gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Python 3.11+ / AsyncIO</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Binance WebSocket API</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">SQLite WAL Engine</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Systemd Linux Daemon</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Microstructure Math</span>
                    </div>
                </div>
                <div class="px-8 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                    <span class="text-xs text-slate-500 font-medium">Status: Live In-Production Engine</span>
                    <span class="text-xs font-semibold text-blue-700 bg-blue-50 border border-blue-200 px-3 py-1 rounded-lg">Proprietary Quant Engine</span>
                </div>
            </div>

            <!-- Project 1: Indian Trading Bot (Multi-Agent Quant Options Sniper) -->
            <div class="project-card bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:border-slate-400 hover:shadow-md transition duration-300 flex flex-col justify-between" data-category="ai">
                <div class="p-8">
                    <div class="flex items-center justify-between mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 text-indigo-700 text-xs font-semibold border border-indigo-200">
                            <span class="w-2 h-2 rounded-full bg-indigo-500 animate-pulse"></span>
                            Production Quantitative System
                        </span>
                        <span class="text-xs text-slate-400 font-medium">Algorithmic Trading & FinTech</span>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 tracking-tight">Indian Trading Bot — Multi-Agent Options Sniper</h3>
                    <p class="mt-3 text-slate-600 text-sm sm:text-base leading-relaxed">
                        An institutional-grade, multi-agent algorithmic options sniper engineered for Indian derivatives (NIFTY, BANKNIFTY, SENSEX). Features 5-Pillar confluence detection, multi-index basket scanning, sub-second execution, automated iceberg order slicing, a permanent ₹1 Lakh floor dividend sweep mechanism, 4-account family fleet execution, and a 4-layer mathematical stealth armor.
                    </p>
                    <div class="mt-6 space-y-2">
                        <h4 class="text-xs font-semibold uppercase tracking-wider text-slate-400">Architectural Highlights</h4>
                        <ul class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm text-slate-700">
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                5-Pillar Confluence Engine (EMA + VWAP + Delta)
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                ₹1 Lakh Floor Capital Protection & Dividend Sweeps
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                4-Account Multi-Broker Family Fleet Execution
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                4-Layer Mathematical Stealth Armor & Auto-Hedge
                            </li>
                        </ul>
                    </div>
                    <div class="mt-6 flex flex-wrap gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Python 3.12 / AsyncIO</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Kotak Neo API</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Breeze API</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Zero-Lag WebSocket</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Quantitative Risk Engine</span>
                    </div>
                </div>
                <div class="px-8 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                    <span class="text-xs text-slate-500 font-medium">Status: Live In-Production Engine</span>
                    <span class="text-xs font-semibold text-indigo-700 bg-indigo-50 border border-indigo-200 px-3 py-1 rounded-lg">Proprietary Fleet System</span>
                </div>
            </div>

            <!-- Project 2: Apex-Attendance-Vault -->
            <div class="project-card bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:border-slate-400 hover:shadow-md transition duration-300 flex flex-col justify-between" data-category="software">
                <div class="p-8">
                    <div class="flex items-center justify-between mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 text-xs font-semibold border border-emerald-200">
                            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                            Production Enterprise System
                        </span>
                        <span class="text-xs text-slate-400 font-medium">Biometric & Workplace Security</span>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 tracking-tight">Apex-Attendance-Vault — Biometric Audit System</h3>
                    <p class="mt-3 text-slate-600 text-sm sm:text-base leading-relaxed">
                        An enterprise-grade, offline-first biometric & camera attendance ledger built with cryptographic audit logs, honeypot traps against clock-tampering, automated monthly payroll PDF reporting, and hardware camera capture verification. Engineered for high-throughput showroom staff operations.
                    </p>
                    <div class="mt-6 space-y-2">
                        <h4 class="text-xs font-semibold uppercase tracking-wider text-slate-400">Architectural Highlights</h4>
                        <ul class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm text-slate-700">
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Offline-First SQLite Ledger with Zero-Data-Loss
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Hardware Camera Capture & Biometric Check-In
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Cryptographic Integrity & Anti-Spoof Honeypots
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Automated Payroll-Ready PDF Monthly Ledgers
                            </li>
                        </ul>
                    </div>
                    <div class="mt-6 flex flex-wrap gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Python / Tkinter UI</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">OpenCV Camera Vision</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">ReportLab PDF Engine</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Cryptographic Hashes</span>
                    </div>
                </div>
                <div class="px-8 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                    <span class="text-xs text-slate-500 font-medium">Status: Live In-Production</span>
                    <a href="contact.html" class="inline-flex items-center gap-1.5 text-sm font-semibold text-slate-900 hover:text-slate-700 transition">
                        Request Enterprise Demo <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>
            </div>

            <!-- Project 3: FootwearBillingApp & footwear-sales-dashboard -->
            <div class="project-card bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:border-slate-400 hover:shadow-md transition duration-300 flex flex-col justify-between" data-category="software">
                <div class="p-8">
                    <div class="flex items-center justify-between mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-purple-50 text-purple-700 text-xs font-semibold border border-purple-200">
                            <i data-lucide="receipt" class="w-3.5 h-3.5"></i>
                            Enterprise Retail POS
                        </span>
                        <span class="text-xs text-slate-400 font-medium">POS, Ledger & Analytics</span>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 tracking-tight">Footwear POS & Executive Sales Dashboard</h3>
                    <p class="mt-3 text-slate-600 text-sm sm:text-base leading-relaxed">
                        A full-fledged commercial retail Point of Sale (POS), inventory ledger, automated GST billing engine, and real-time sales analytics dashboard. Eliminates inventory discrepancies, tracks dead stock, monitors daily counter turnover, and generates compliant GST invoices.
                    </p>
                    <div class="mt-6 space-y-2">
                        <h4 class="text-xs font-semibold uppercase tracking-wider text-slate-400">Architectural Highlights</h4>
                        <ul class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm text-slate-700">
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Sub-Second Barcode Scanning & Rapid Checkout
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Automated GST Tax Invoicing & Thermal Printing
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Multi-Store Real-Time Sales Velocity Dashboard
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                SKU Reorder Forecasting & Margin Ledger
                            </li>
                        </ul>
                    </div>
                    <div class="mt-6 flex flex-wrap gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Python Desktop App</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">React 18 Analytics</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">SQLite & JSON Ledger</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Thermal Printer Protocol</span>
                    </div>
                </div>
                <div class="px-8 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                    <span class="text-xs text-slate-500 font-medium">Status: Deployed in Active Retail</span>
                    <a href="contact.html" class="inline-flex items-center gap-1.5 text-sm font-semibold text-slate-900 hover:text-slate-700 transition">
                        View System Specs <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>
            </div>

            <!-- Project 4: Ladies Zone Haute Couture Showcase (ladieszonepatna.in) -->
            <div class="project-card bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:border-slate-400 hover:shadow-md transition duration-300 flex flex-col justify-between" data-category="web">
                <div class="p-8">
                    <div class="flex items-center justify-between mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 text-xs font-semibold border border-emerald-200">
                            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                            Live Production Platform
                        </span>
                        <span class="text-xs text-slate-400 font-medium">Global Edge Web Architecture</span>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 tracking-tight">Maison Ladies Zone — Haute Couture Digital Showcase</h3>
                    <p class="mt-3 text-slate-600 text-sm sm:text-base leading-relaxed">
                        A global luxury digital showcase and concierge appointment platform engineered for Ladies Zone Exclusive Showroom (Boring Road, Patna). Designed with editorial aesthetics inspired by Hermès and Louis Vuitton, zero-cart showroom trial bookings, a staff photo curation portal, and protected by a 5-layer mathematical stealth shield.
                    </p>
                    <div class="mt-6 space-y-2">
                        <h4 class="text-xs font-semibold uppercase tracking-wider text-slate-400">Architectural Highlights</h4>
                        <ul class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm text-slate-700">
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                In-Store Showroom Trial Model & WhatsApp Concierge
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Client-Side Curator Photo Upload & Inventory Management
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                5-Layer Mathematical Stealth Shield (crypto_stealth.js)
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                100/100 Grade A+ SEO & Sub-200ms Global Edge Latency
                            </li>
                        </ul>
                    </div>
                    <div class="mt-6 flex flex-wrap gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">HTML5 / Cinzel Haute CSS</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Cloudflare Pages Edge</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Mersenne Prime Integrity Shield</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">WhatsApp API Concierge</span>
                    </div>
                </div>
                <div class="px-8 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                    <span class="text-xs text-slate-500 font-medium">Domain: ladieszonepatna.in</span>
                    <a href="https://ladieszone.pages.dev" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-sm font-medium shadow-sm transition">
                        <span>Visit Live Platform</span>
                        <i data-lucide="external-link" class="w-4 h-4"></i>
                    </a>
                </div>
            </div>

            <!-- Project 5: Autonomous AI Website Builder Studio -->
            <div class="project-card bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:border-slate-400 hover:shadow-md transition duration-300 flex flex-col justify-between" data-category="ai">
                <div class="p-8">
                    <div class="flex items-center justify-between mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-cyan-50 text-cyan-700 text-xs font-semibold border border-cyan-200">
                            <span class="w-2 h-2 rounded-full bg-cyan-500 animate-pulse"></span>
                            AI Development Platform
                        </span>
                        <span class="text-xs text-slate-400 font-medium">Multi-Model AI Software</span>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 tracking-tight">Autonomous AI Website Builder Studio</h3>
                    <p class="mt-3 text-slate-600 text-sm sm:text-base leading-relaxed">
                        A full-stack autonomous web generator engine combining Gemini AI multi-model fallbacks, AST code validation, automated self-healing compilers, lead CRM databases, executive client pitch generators, and 1-click Cloudflare Pages edge deployments.
                    </p>
                    <div class="mt-6 space-y-2">
                        <h4 class="text-xs font-semibold uppercase tracking-wider text-slate-400">Architectural Highlights</h4>
                        <ul class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm text-slate-700">
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Autonomous Multi-Model AI Routing (Flash & Pro)
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                AST Code Self-Healing & Syntax Error Auto-Repair
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Integrated Lead CRM & Autonomous Pitch Generator
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                1-Click Automated Cloudflare Edge API Deployment
                            </li>
                        </ul>
                    </div>
                    <div class="mt-6 flex flex-wrap gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Python 3 / Streamlit</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Google Gemini AI API</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">AST Code Analysis</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Cloudflare API</span>
                    </div>
                </div>
                <div class="px-8 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                    <span class="text-xs text-slate-500 font-medium">Status: Active Development Engine</span>
                    <a href="contact.html" class="inline-flex items-center gap-1.5 text-sm font-semibold text-slate-900 hover:text-slate-700 transition">
                        Explore Platform <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>
            </div>
"""

# Update projects.html
content_p = projects_file.read_text(encoding="utf-8")
grid_start = content_p.find('<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">')
grid_end = content_p.find('<!-- What I Build & Deliver Section -->')

if grid_start != -1 and grid_end != -1:
    new_projects_html = content_p[:grid_start + len('<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">')] + "\n" + PROJECTS_CARDS + "\n            </div>\n        </div>\n    </section>\n    " + content_p[grid_end:]
    projects_file.write_text(new_projects_html, encoding="utf-8")
    print("Updated projects.html successfully!")
else:
    print("Could not find grid boundaries in projects.html")

# Update Aria response in projects.html & index.html
new_aria_response = """response = `Mohammad Rehan has engineered an extraordinary production software suite:
                1. <strong>Aegis Crypto Engine</strong>: Asynchronous spot market microstructure execution engine on Binance with microsecond telemetry and 78 verified invariants.<br>
                2. <strong>Indian Trading Bot</strong>: Multi-agent quantitative options sniper with 5-pillar confluence and 4-account family fleet execution.<br>
                3. <strong>Apex-Attendance-Vault</strong>: Biometric and camera attendance system with cryptographic integrity and automated PDF payroll reporting.<br>
                4. <strong>Footwear POS & Sales Dashboard</strong>: Real-world retail inventory ledger, barcode billing, and sales analytics.<br>
                5. <strong>Maison Ladies Zone (ladieszonepatna.in)</strong>: Luxury boutique digital showcase with 5-layer mathematical stealth armor and WhatsApp concierge.<br>
                6. <strong>Autonomous AI Web Studio</strong>: Multi-model generation engine with AST self-healing and 1-click edge deployment.<br>
                <div class="pt-2"><a href="projects.html" class="inline-block bg-indigo-600 hover:bg-indigo-500 text-white px-3 py-1.5 rounded-lg text-xs font-medium">View All Projects &rarr;</a></div>`;"""

for f in [projects_file, index_file]:
    if f.exists():
        txt = f.read_text(encoding="utf-8")
        # replace aria response if present
        txt = re.sub(r'response\s*=\s*`Mohammad Rehan has built several notable systems:.*?View Projects Page &rarr;</a></div>`;', new_aria_response, txt, flags=re.DOTALL)
        f.write_text(txt, encoding="utf-8")
        print(f"Updated Aria assistant in {f.name}!")
