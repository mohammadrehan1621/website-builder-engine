import os
import sys
from pathlib import Path

PORTFOLIO_DIR = Path(r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev")

def update_files():
    # -------------------------------------------------------------
    # Common snippets
    # -------------------------------------------------------------
    # 1. Popover dropdown snippet for Desktop Navigation
    old_dropdown_inner = """                        <!-- Product 1: Deterministic State Kernel -->
                        <a href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE?wanted=true" target="_blank" rel="noopener noreferrer" class="flex items-start gap-2.5 p-2.5 rounded-xl hover:bg-emerald-50/80 transition group/item">
                            <div class="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0 mt-0.5 group-hover/item:bg-emerald-600 group-hover/item:text-white transition">
                                <i class="w-4 h-4" data-lucide="cpu"></i>
                            </div>
                            <div class="flex-1 min-w-0">
                                <div class="flex items-center justify-between gap-1">
                                    <span class="text-xs font-bold text-slate-900 group-hover/item:text-emerald-700 truncate">Deterministic State Kernel&trade;</span>
                                    <span class="text-[9px] font-mono font-bold text-emerald-800 bg-emerald-100 px-1.5 py-0.5 rounded whitespace-nowrap">$249 / &#8377;19k</span>
                                </div>
                                <p class="text-[11px] text-slate-500 mt-0.5 truncate">Rust Bare-Metal &bull; 604ns Reads &bull; SHA-256 WAL</p>
                            </div>
                        </a>
                        <!-- Product 2: RQL Aegis -->
                        <a href="aegis.html" class="flex items-start gap-2.5 p-2.5 rounded-xl hover:bg-cyan-50/80 transition group/item">
                            <div class="w-8 h-8 rounded-lg bg-cyan-100 text-cyan-700 flex items-center justify-center shrink-0 mt-0.5 group-hover/item:bg-cyan-600 group-hover/item:text-white transition">
                                <i class="w-4 h-4" data-lucide="shield"></i>
                            </div>
                            <div class="flex-1 min-w-0">
                                <div class="flex items-center justify-between gap-1">
                                    <span class="text-xs font-bold text-slate-900 group-hover/item:text-cyan-700 truncate">RQL Aegis&trade;</span>
                                    <span class="text-[9px] font-mono font-bold text-cyan-800 bg-cyan-100 px-1.5 py-0.5 rounded whitespace-nowrap">$249</span>
                                </div>
                                <p class="text-[11px] text-slate-500 mt-0.5 truncate">On-Premises Risk Middleware &bull; Volatility Clamp</p>
                            </div>
                        </a>"""

    new_dropdown_inner = """                        <!-- Product 1: Deterministic State Kernel -->
                        <a href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE?wanted=true" target="_blank" rel="noopener noreferrer" class="flex items-start gap-2.5 p-2.5 rounded-xl hover:bg-emerald-50/80 transition group/item">
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
                        <a href="https://quantify17.gumroad.com/l/rql-aegis/EARLYBIRD?wanted=true" target="_blank" rel="noopener noreferrer" class="flex items-start gap-2.5 p-2.5 rounded-xl hover:bg-cyan-50/80 transition group/item">
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
                        <a href="https://quantify17.gumroad.com/l/eucck/VERITAS?wanted=true" target="_blank" rel="noopener noreferrer" class="flex items-start gap-2.5 p-2.5 rounded-xl hover:bg-purple-50/80 transition group/item">
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
                        <a href="https://quantify17.gumroad.com/l/ivyiwh/SENTINEL?wanted=true" target="_blank" rel="noopener noreferrer" class="flex items-start gap-2.5 p-2.5 rounded-xl hover:bg-amber-50/80 transition group/item">
                            <div class="w-8 h-8 rounded-lg bg-amber-100 text-amber-800 flex items-center justify-center shrink-0 mt-0.5 group-hover/item:bg-amber-600 group-hover/item:text-white transition">
                                <i class="w-4 h-4" data-lucide="factory"></i>
                            </div>
                            <div class="flex-1 min-w-0">
                                <div class="flex items-center justify-between gap-1">
                                    <span class="text-xs font-bold text-slate-900 group-hover/item:text-amber-800 truncate">Industrial Fragility Sentinel&trade;</span>
                                    <span class="text-[9px] font-mono font-bold text-amber-800 bg-amber-100 px-1.5 py-0.5 rounded whitespace-nowrap">$299</span>
                                </div>
                                <p class="text-[11px] text-slate-500 mt-0.5 truncate">Factory Uptime &amp; Supply Chokepoint Daemon</p>
                            </div>
                        </a>"""

    # 2. Mobile menu snippet
    old_mobile_inner = """        <div class="pt-2 pb-1 px-3 text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider">Commercial Products</div>
        <a class="block py-2 px-3 rounded-lg bg-emerald-50 text-emerald-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE?wanted=true" target="_blank" rel="noopener noreferrer">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-emerald-600" data-lucide="cpu"></i>
                <span>Deterministic State Kernel&trade;</span>
            </div>
            <span class="bg-emerald-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$249 / &#8377;19,999</span>
        </a>
        <a class="block py-2 px-3 rounded-lg bg-cyan-50 text-cyan-950 font-bold text-sm flex items-center justify-between" href="aegis.html">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-cyan-600" data-lucide="shield"></i>
                <span>RQL Aegis&trade;</span>
            </div>
            <span class="bg-cyan-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$249</span>
        </a>"""

    new_mobile_inner = """        <div class="pt-2 pb-1 px-3 text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider">Commercial Products (Sovereign Suite)</div>
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
        </a>"""

    # Apply to all 3 navigation menus
    for fname in ["projects.html", "index.html", "aegis.html"]:
        fpath = PORTFOLIO_DIR / fname
        content = fpath.read_text(encoding="utf-8")
        
        # Normalize CRLF for matching
        content_norm = content.replace("\r\n", "\n")
        old_drop_norm = old_dropdown_inner.replace("\r\n", "\n")
        new_drop_norm = new_dropdown_inner.replace("\r\n", "\n")
        old_mob_norm = old_mobile_inner.replace("\r\n", "\n")
        new_mob_norm = new_mobile_inner.replace("\r\n", "\n")

        if old_drop_norm in content_norm:
            content_norm = content_norm.replace(old_drop_norm, new_drop_norm)
            print(f"[{fname}] Successfully updated Popover Dropdown.")
        else:
            print(f"[{fname}] Popover Dropdown pattern not found or already updated.")

        if old_mob_norm in content_norm:
            content_norm = content_norm.replace(old_mob_norm, new_mob_norm)
            print(f"[{fname}] Successfully updated Mobile Menu.")
        else:
            print(f"[{fname}] Mobile Menu pattern not found or already updated.")

        # Save back with original CRLF
        fpath.write_text(content_norm.replace("\n", "\r\n"), encoding="utf-8")

    # -------------------------------------------------------------
    # 3. Update projects.html: Upgrade Aegis Card & Insert Veritas + Sentinel Cards
    # -------------------------------------------------------------
    projects_file = PORTFOLIO_DIR / "projects.html"
    p_content = projects_file.read_text(encoding="utf-8").replace("\r\n", "\n")

    old_aegis_footer = """                <div class="p-8 pt-0 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-4 mt-4">
                    <div class="flex items-center gap-2">
                        <span class="text-xs text-slate-400 font-mono">License:</span>
                        <span class="text-xs font-mono font-bold text-cyan-400 bg-cyan-950/80 border border-cyan-500/30 px-2 py-0.5 rounded">Perpetual &bull; Own Forever</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <a href="RQL-Aegis-v1.0-Release.zip" download class="text-xs font-semibold text-slate-300 hover:text-white px-3.5 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition flex items-center gap-1.5">
                            <i data-lucide="download" class="w-3.5 h-3.5 text-cyan-400"></i>
                            <span>Download Standalone (ZIP)</span>
                        </a>
                        <a href="aegis.html" class="text-xs font-bold text-white bg-cyan-600 hover:bg-cyan-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-cyan-600/20">
                            <i data-lucide="shield" class="w-3.5 h-3.5 text-cyan-200"></i>
                            <span>Inspect Engine ($249)</span>
                        </a>
                    </div>
                </div>
            </div>"""

    new_aegis_and_new_cards = """                <div class="p-8 pt-0 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-4 mt-4">
                    <div class="flex flex-col gap-1">
                        <div class="flex items-center gap-2">
                            <span class="text-xs text-slate-400 font-mono">Promo:</span>
                            <span class="text-xs font-mono font-bold text-cyan-400 bg-cyan-950/80 border border-cyan-500/30 px-2 py-0.5 rounded">EARLYBIRD (50% Off)</span>
                        </div>
                        <span class="text-[11px] text-amber-400 font-mono">🔥 Exclusive to First 20 Buyers &bull; Standard: $249</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <a href="aegis.html" class="text-xs font-semibold text-slate-300 hover:text-white px-3.5 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                            Details
                        </a>
                        <a href="https://quantify17.gumroad.com/l/rql-aegis/EARLYBIRD?wanted=true" target="_blank" rel="noopener noreferrer" class="text-xs font-bold text-white bg-cyan-600 hover:bg-cyan-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-cyan-600/20">
                            <i data-lucide="zap" class="w-3.5 h-3.5 text-cyan-200"></i>
                            <span>Claim Early Pass ($125)</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Project: Veritas Dossier™ Air-Gapped Private DRHP & Capital Dilution Auditor -->
            <div class="project-card bg-slate-950 text-white rounded-2xl border-2 border-purple-500/40 overflow-hidden shadow-lg hover:border-purple-400 hover:shadow-xl transition duration-300 flex flex-col justify-between" data-category="quant">
                <div class="p-8">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-purple-500/20 text-purple-300 text-xs font-semibold border border-purple-400/40 font-mono">
                            <span class="w-2 h-2 rounded-full bg-purple-400 animate-pulse"></span>
                            Air-Gapped Forensic Dilution Engine
                        </span>
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-bold text-purple-300 bg-purple-950/90 border border-purple-500/40 px-2.5 py-0.5 rounded font-mono">Live at $249</span>
                            <span class="text-xs text-slate-500 line-through font-mono">$499</span>
                        </div>
                    </div>

                    <h3 class="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>Veritas Dossier&trade;</span>
                        <span class="text-xs font-mono text-purple-400 font-normal">v1.0 (PROD)</span>
                    </h3>
                    <p class="text-xs font-mono text-purple-400 font-semibold mt-1">Air-Gapped Private DRHP &amp; Capital Dilution Auditor</p>
                    <p class="mt-3 text-slate-300 text-sm sm:text-base leading-relaxed">
                        An institutional-grade, air-gapped forensic audit engine designed for Chartered Accountants, Merchant Bankers, IPO Advisors, and Equity Analysts. Runs 100% locally on your office PC or intranet server to audit 500+ page SEBI DRHPs, unlisted cap tables, and merger filings with zero cloud dependencies and 100% strict client NDA compliance.
                    </p>

                    <div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Dilution Bridge</div>
                            <div class="text-sm sm:text-base font-bold text-purple-400 font-mono mt-0.5">Post-Issue BVPS</div>
                            <div class="text-[10px] text-slate-500">Exact % Dilution</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Data Privacy</div>
                            <div class="text-sm sm:text-base font-bold text-emerald-400 font-mono mt-0.5">Air-Gapped</div>
                            <div class="text-[10px] text-slate-500">Zero Cloud Leaks</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Forensic Scan</div>
                            <div class="text-sm sm:text-base font-bold text-amber-400 font-mono mt-0.5">Pledge &amp; RPT</div>
                            <div class="text-[10px] text-slate-500">Promoter Siphon</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Binary Package</div>
                            <div class="text-sm sm:text-base font-bold text-indigo-400 font-mono mt-0.5">9.2 MB EXE</div>
                            <div class="text-[10px] text-slate-500">Zero Python Needed</div>
                        </div>
                    </div>

                    <div class="mt-6 space-y-2 text-xs text-slate-300">
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-purple-400 flex-shrink-0"></i>
                            <span>OFS vs Fresh Issue Isolation &bull; Instant visual breakdown of promoter cash-out vs growth capex</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-purple-400 flex-shrink-0"></i>
                            <span>Air-gapped on-premises execution &bull; Complete NDA immunity for unlisted IPO filings</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-purple-400 flex-shrink-0"></i>
                            <span>Machine-locked perpetual license &bull; Pay once, own forever with zero recurring monthly SaaS fees</span>
                        </div>
                    </div>
                </div>

                <div class="p-8 pt-0 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-4 mt-4">
                    <div class="flex flex-col gap-1">
                        <div class="flex items-center gap-2">
                            <span class="text-xs text-slate-400 font-mono">Promo:</span>
                            <span class="text-xs font-mono font-bold text-purple-400 bg-purple-950/80 border border-purple-500/30 px-2 py-0.5 rounded">VERITAS (50% Off)</span>
                        </div>
                        <span class="text-[11px] text-amber-400 font-mono">🔥 Exclusive to First 20 Buyers &bull; Standard: $499</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <a href="https://quantify17.gumroad.com/l/eucck" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3.5 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                            Product Details
                        </a>
                        <a href="https://quantify17.gumroad.com/l/eucck/VERITAS?wanted=true" target="_blank" rel="noopener noreferrer" class="text-xs font-bold text-white bg-purple-600 hover:bg-purple-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-purple-600/20">
                            <i data-lucide="zap" class="w-3.5 h-3.5 text-white"></i>
                            <span>Claim Early Pass ($249)</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Project: Industrial Fragility Sentinel™ On-Premises Factory Uptime & Chokepoint Sentinel -->
            <div class="project-card bg-slate-950 text-white rounded-2xl border-2 border-amber-500/40 overflow-hidden shadow-lg hover:border-amber-400 hover:shadow-xl transition duration-300 flex flex-col justify-between" data-category="resilience">
                <div class="p-8">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 text-xs font-semibold border border-amber-400/40 font-mono">
                            <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
                            Shop Floor Resilience Sentinel
                        </span>
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-bold text-amber-300 bg-amber-950/90 border border-amber-500/40 px-2.5 py-0.5 rounded font-mono">Live at $299</span>
                            <span class="text-xs text-slate-500 line-through font-mono">$599</span>
                        </div>
                    </div>

                    <h3 class="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>Industrial Fragility Sentinel&trade;</span>
                        <span class="text-xs font-mono text-amber-400 font-normal">v1.0 (PROD)</span>
                    </h3>
                    <p class="text-xs font-mono text-amber-400 font-semibold mt-1">On-Premises Factory Uptime &amp; Chokepoint Sentinel</p>
                    <p class="mt-3 text-slate-300 text-sm sm:text-base leading-relaxed">
                        An institutional-grade plant resilience daemon built on Sun Tzu's Art of War (&ldquo;Terrain &amp; Asymmetry&rdquo;) and John Gall's Law. Runs 24/7 on a dedicated factory PC or shop floor industrial server to eliminate surprise single-vendor supply bottlenecks, power grid drops, and machine downtime with zero recurring monthly cloud bills.
                    </p>

                    <div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Fragility Index</div>
                            <div class="text-sm sm:text-base font-bold text-amber-400 font-mono mt-0.5">0 to 100 Score</div>
                            <div class="text-[10px] text-slate-500">5-Factor Asymmetry</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Supply Chokepoint</div>
                            <div class="text-sm sm:text-base font-bold text-emerald-400 font-mono mt-0.5">&gt;50% Detection</div>
                            <div class="text-[10px] text-slate-500">Early Vendor Alarm</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Captive Power</div>
                            <div class="text-sm sm:text-base font-bold text-cyan-400 font-mono mt-0.5">Generator Telemetry</div>
                            <div class="text-[10px] text-slate-500">Fuel Runway Guard</div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase font-mono">Binary Package</div>
                            <div class="text-sm sm:text-base font-bold text-indigo-400 font-mono mt-0.5">9.16 MB EXE</div>
                            <div class="text-[10px] text-slate-500">Zero Cloud Egress</div>
                        </div>
                    </div>

                    <div class="mt-6 space-y-2 text-xs text-slate-300">
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-amber-400 flex-shrink-0"></i>
                            <span>Captive Power &amp; Fuel Runway Telemetry &bull; Guarantees zero furnace or production line freezes</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-amber-400 flex-shrink-0"></i>
                            <span>100% on-premises offline operation &bull; Zero data leakage of proprietary plant formulas or metrics</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-4 h-4 text-amber-400 flex-shrink-0"></i>
                            <span>Machine-locked perpetual license &bull; Pay once, protect your factory forever</span>
                        </div>
                    </div>
                </div>

                <div class="p-8 pt-0 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-4 mt-4">
                    <div class="flex flex-col gap-1">
                        <div class="flex items-center gap-2">
                            <span class="text-xs text-slate-400 font-mono">Promo:</span>
                            <span class="text-xs font-mono font-bold text-amber-400 bg-amber-950/80 border border-amber-500/30 px-2 py-0.5 rounded">SENTINEL (50% Off)</span>
                        </div>
                        <span class="text-[11px] text-amber-400 font-mono">🔥 Exclusive to First 20 Buyers &bull; Standard: $599</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <a href="https://quantify17.gumroad.com/l/ivyiwh" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3.5 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                            Product Details
                        </a>
                        <a href="https://quantify17.gumroad.com/l/ivyiwh/SENTINEL?wanted=true" target="_blank" rel="noopener noreferrer" class="text-xs font-bold text-slate-950 bg-amber-400 hover:bg-amber-300 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-amber-400/20">
                            <i data-lucide="zap" class="w-3.5 h-3.5 text-slate-950"></i>
                            <span>Claim Early Pass ($299)</span>
                        </a>
                    </div>
                </div>
            </div>"""

    if old_aegis_footer in p_content:
        p_content = p_content.replace(old_aegis_footer, new_aegis_and_new_cards)
        projects_file.write_text(p_content.replace("\n", "\r\n"), encoding="utf-8")
        print("[projects.html] Successfully inserted Veritas Dossier & Industrial Fragility Sentinel cards!")
    else:
        print("[projects.html] Aegis footer pattern not matched for card insertion.")

    # -------------------------------------------------------------
    # 4. Update index.html: Add Flagship 3 & 4 Cards to Homepage
    # -------------------------------------------------------------
    index_file = PORTFOLIO_DIR / "index.html"
    i_content = index_file.read_text(encoding="utf-8").replace("\r\n", "\n")

    old_idx_flagship_end = """            <div class="pt-5 mt-5 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3">
                <div class="text-xs font-mono">
                    <span class="text-amber-400 font-bold bg-amber-950/70 border border-amber-500/40 px-2 py-0.5 rounded text-[11px]">🔥 FIRST 20 BUYERS ONLY: 50% OFF</span>
                    <div class="text-[11px] text-slate-400 mt-1">Standard: <span class="line-through text-slate-500">$249</span> &bull; Promo: <span class="text-cyan-400 font-bold">EARLYBIRD</span></div>
                </div>
                <div class="flex items-center gap-2">
                    <a href="aegis.html" class="text-xs font-semibold text-slate-300 hover:text-white px-3 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                        Details
                    </a>
                    <a href="https://quantify17.gumroad.com/l/rql-aegis/EARLYBIRD?wanted=true" target="_blank" rel="noopener noreferrer" class="bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-cyan-600/20">
                        <i data-lucide="zap" class="w-3.5 h-3.5 text-cyan-200"></i>
                        <span>Claim Early Pass ($125 / &#8377;11,820)</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>"""

    new_idx_flagship_end = """            <div class="pt-5 mt-5 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3">
                <div class="text-xs font-mono">
                    <span class="text-amber-400 font-bold bg-amber-950/70 border border-amber-500/40 px-2 py-0.5 rounded text-[11px]">🔥 FIRST 20 BUYERS ONLY: 50% OFF</span>
                    <div class="text-[11px] text-slate-400 mt-1">Standard: <span class="line-through text-slate-500">$249</span> &bull; Promo: <span class="text-cyan-400 font-bold">EARLYBIRD</span></div>
                </div>
                <div class="flex items-center gap-2">
                    <a href="aegis.html" class="text-xs font-semibold text-slate-300 hover:text-white px-3 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                        Details
                    </a>
                    <a href="https://quantify17.gumroad.com/l/rql-aegis/EARLYBIRD?wanted=true" target="_blank" rel="noopener noreferrer" class="bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-cyan-600/20">
                        <i data-lucide="zap" class="w-3.5 h-3.5 text-cyan-200"></i>
                        <span>Claim Early Pass ($125 / &#8377;11,820)</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- Flagship 3: Veritas Dossier™ -->
        <div class="rounded-2xl bg-gradient-to-br from-slate-950 via-slate-900 to-purple-950 border-2 border-purple-500/50 shadow-xl p-6 sm:p-7 flex flex-col justify-between text-white hover:border-purple-400 transition duration-300">
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="bg-purple-500/20 text-purple-300 border border-purple-400/50 text-[10px] px-2.5 py-1 rounded-lg font-mono font-bold uppercase tracking-wider flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-purple-400 animate-pulse"></span>
                        Air-Gapped Forensic Dilution Engine
                    </span>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-bold text-amber-300 bg-amber-950/80 border border-amber-500/40 px-2.5 py-1 rounded-lg font-mono">First 20 Only: $249</span>
                        <span class="text-xs text-slate-400 font-mono line-through">$499</span>
                    </div>
                </div>

                <div>
                    <h3 class="text-xl sm:text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>Veritas Dossier&trade;</span>
                        <span class="text-xs font-mono text-purple-400 font-normal">v1.0 (PROD)</span>
                    </h3>
                    <p class="text-xs font-mono text-purple-400 font-semibold mt-1">Air-Gapped Private DRHP &amp; Capital Dilution Auditor</p>
                </div>

                <p class="text-slate-300 text-sm leading-relaxed">
                    Air-gapped on-premises forensic audit engine designed for Chartered Accountants, Merchant Bankers, and Equity Analysts. Audits 500+ page SEBI DRHPs, unlisted cap tables, and post-issue dilution bridges with 100% strict client NDA compliance and zero cloud telemetry.
                </p>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center font-mono">
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Dilution Bridge</div>
                        <div class="text-xs sm:text-sm font-bold text-purple-400 mt-0.5">Post-Issue BVPS</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Data Privacy</div>
                        <div class="text-xs sm:text-sm font-bold text-emerald-400 mt-0.5">Air-Gapped</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Forensic Scan</div>
                        <div class="text-xs sm:text-sm font-bold text-amber-400 mt-0.5">Pledge &amp; RPT</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Packaging</div>
                        <div class="text-xs sm:text-sm font-bold text-indigo-400 mt-0.5">9.2 MB EXE</div>
                    </div>
                </div>

                <div class="space-y-1.5 text-xs text-slate-300">
                    <div class="flex items-center gap-2">
                        <i data-lucide="check-circle-2" class="w-4 h-4 text-purple-400 flex-shrink-0"></i>
                        <span>OFS vs Fresh Issue Isolation &bull; Instant visual breakdown of promoter cash-out</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <i data-lucide="check-circle-2" class="w-4 h-4 text-purple-400 flex-shrink-0"></i>
                        <span>Zero cloud dependencies &bull; Hardware machine-lock perpetual commercial license</span>
                    </div>
                </div>
            </div>

            <div class="pt-5 mt-5 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3">
                <div class="text-xs font-mono">
                    <span class="text-amber-400 font-bold bg-amber-950/70 border border-amber-500/40 px-2 py-0.5 rounded text-[11px]">🔥 FIRST 20 BUYERS ONLY: 50% OFF</span>
                    <div class="text-[11px] text-slate-400 mt-1">Standard: <span class="line-through text-slate-500">$499</span> &bull; Promo: <span class="text-purple-400 font-bold">VERITAS</span></div>
                </div>
                <div class="flex items-center gap-2">
                    <a href="https://quantify17.gumroad.com/l/eucck" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                        Details
                    </a>
                    <a href="https://quantify17.gumroad.com/l/eucck/VERITAS?wanted=true" target="_blank" rel="noopener noreferrer" class="bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-purple-600/20">
                        <i data-lucide="zap" class="w-3.5 h-3.5 text-white"></i>
                        <span>Claim Early Pass ($249 / &#8377;23,689)</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- Flagship 4: Industrial Fragility Sentinel™ -->
        <div class="rounded-2xl bg-gradient-to-br from-slate-950 via-slate-900 to-amber-950 border-2 border-amber-500/50 shadow-xl p-6 sm:p-7 flex flex-col justify-between text-white hover:border-amber-400 transition duration-300">
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="bg-amber-500/20 text-amber-300 border border-amber-400/50 text-[10px] px-2.5 py-1 rounded-lg font-mono font-bold uppercase tracking-wider flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
                        Shop Floor Resilience Sentinel
                    </span>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-bold text-amber-300 bg-amber-950/80 border border-amber-500/40 px-2.5 py-1 rounded-lg font-mono">First 20 Only: $299</span>
                        <span class="text-xs text-slate-400 font-mono line-through">$599</span>
                    </div>
                </div>

                <div>
                    <h3 class="text-xl sm:text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>Industrial Fragility Sentinel&trade;</span>
                        <span class="text-xs font-mono text-amber-400 font-normal">v1.0 (PROD)</span>
                    </h3>
                    <p class="text-xs font-mono text-amber-400 font-semibold mt-1">On-Premises Factory Uptime &amp; Chokepoint Sentinel</p>
                </div>

                <p class="text-slate-300 text-sm leading-relaxed">
                    Air-gapped plant resilience daemon implementing Sun Tzu's Art of War and Gall's Law. Runs 24/7 on shop floor industrial hardware to eliminate single-vendor supply chokepoints, power drops, and machine downtime with zero recurring monthly cloud SaaS bills.
                </p>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center font-mono">
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Fragility Index</div>
                        <div class="text-xs sm:text-sm font-bold text-amber-400 mt-0.5">0 to 100 Score</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Chokepoints</div>
                        <div class="text-xs sm:text-sm font-bold text-emerald-400 mt-0.5">&gt;50% Single Vendor</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Power Telemetry</div>
                        <div class="text-xs sm:text-sm font-bold text-cyan-400 mt-0.5">Fuel Runway</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Packaging</div>
                        <div class="text-xs sm:text-sm font-bold text-indigo-400 mt-0.5">9.16 MB EXE</div>
                    </div>
                </div>

                <div class="space-y-1.5 text-xs text-slate-300">
                    <div class="flex items-center gap-2">
                        <i data-lucide="check-circle-2" class="w-4 h-4 text-amber-400 flex-shrink-0"></i>
                        <span>Captive Power &amp; Fuel Runway Telemetry &bull; Zero furnace or line freezes</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <i data-lucide="check-circle-2" class="w-4 h-4 text-amber-400 flex-shrink-0"></i>
                        <span>100% on-premises offline operation &bull; Pay once, protect your factory forever</span>
                    </div>
                </div>
            </div>

            <div class="pt-5 mt-5 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3">
                <div class="text-xs font-mono">
                    <span class="text-amber-400 font-bold bg-amber-950/70 border border-amber-500/40 px-2 py-0.5 rounded text-[11px]">🔥 FIRST 20 BUYERS ONLY: 50% OFF</span>
                    <div class="text-[11px] text-slate-400 mt-1">Standard: <span class="line-through text-slate-500">$599</span> &bull; Promo: <span class="text-amber-400 font-bold">SENTINEL</span></div>
                </div>
                <div class="flex items-center gap-2">
                    <a href="https://quantify17.gumroad.com/l/ivyiwh" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                        Details
                    </a>
                    <a href="https://quantify17.gumroad.com/l/ivyiwh/SENTINEL?wanted=true" target="_blank" rel="noopener noreferrer" class="bg-amber-400 hover:bg-amber-300 text-slate-950 font-bold text-xs px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-amber-400/20">
                        <i data-lucide="zap" class="w-3.5 h-3.5 text-slate-950"></i>
                        <span>Claim Early Pass ($299 / &#8377;28,427)</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>"""

    if old_idx_flagship_end in i_content:
        i_content = i_content.replace(old_idx_flagship_end, new_idx_flagship_end)
        index_file.write_text(i_content.replace("\n", "\r\n"), encoding="utf-8")
        print("[index.html] Successfully inserted Veritas Dossier & Industrial Fragility Sentinel cards!")
    else:
        print("[index.html] Flagship end pattern not matched for homepage.")

if __name__ == "__main__":
    update_files()
