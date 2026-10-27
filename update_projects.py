import os
from pathlib import Path

BASE_DIR = Path(r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev")
proj_path = BASE_DIR / "projects.html"

content = proj_path.read_text(encoding="utf-8")
content_norm = content.replace("\r\n", "\n")

# 1. Desktop Nav
old_nav = """            <a class="text-cyan-800 font-semibold bg-cyan-50/90 border border-cyan-200/80 px-2.5 py-1 rounded-lg flex items-center gap-1.5 shadow-2xs hover:bg-cyan-100/80 transition" href="aegis.html">
                <i class="w-3.5 h-3.5 text-cyan-600" data-lucide="shield"></i>
                <span>RQL Aegis™</span>
                <span class="bg-cyan-200/70 text-cyan-900 text-[9px] px-1.5 py-0.5 rounded font-bold uppercase tracking-wider">Software</span>
            </a>"""

new_nav = """            <a class="text-cyan-800 font-semibold bg-cyan-50/90 border border-cyan-200/80 px-2.5 py-1 rounded-lg flex items-center gap-1.5 shadow-2xs hover:bg-cyan-100/80 transition" href="aegis.html">
                <i class="w-3.5 h-3.5 text-cyan-600" data-lucide="shield"></i>
                <span>RQL Aegis™</span>
                <span class="bg-cyan-200/70 text-cyan-900 text-[9px] px-1.5 py-0.5 rounded font-bold uppercase tracking-wider">$249</span>
            </a>
            <a class="text-emerald-800 font-semibold bg-emerald-50/90 border border-emerald-200/80 px-2.5 py-1 rounded-lg flex items-center gap-1.5 shadow-2xs hover:bg-emerald-100/80 transition" href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE" target="_blank" rel="noopener noreferrer">
                <i class="w-3.5 h-3.5 text-emerald-600" data-lucide="cpu"></i>
                <span>State Kernel™</span>
                <span class="bg-emerald-200/70 text-emerald-900 text-[9px] px-1.5 py-0.5 rounded font-bold uppercase tracking-wider">$249</span>
            </a>"""

# 2. Card Buy Button
old_card_footer = """                <div class="px-8 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                    <span class="text-xs text-slate-500 font-medium">Repository: github.com/rehanquantlab/aegis-db</span>
                    <a href="https://github.com/rehanquantlab/aegis-db" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-indigo-700 bg-indigo-50 border border-indigo-200 px-3 py-1 rounded-lg hover:bg-indigo-100 transition flex items-center gap-1">
                        <span>View Source</span>
                        <i data-lucide="external-link" class="w-3 h-3"></i>
                    </a>
                </div>"""

new_card_footer = """                <div class="px-8 py-4 bg-slate-50 border-t border-slate-100 flex flex-wrap items-center justify-between gap-3">
                    <span class="text-xs text-slate-500 font-medium font-mono">v1.0 (PROD) • Bare-Metal Rust Engine</span>
                    <div class="flex items-center gap-2">
                        <a href="https://github.com/rehanquantlab/aegis-db" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-700 bg-white border border-slate-200 px-3 py-1.5 rounded-lg hover:bg-slate-100 transition flex items-center gap-1">
                            <span>GitHub</span>
                            <i data-lucide="external-link" class="w-3 h-3"></i>
                        </a>
                        <a href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-white bg-emerald-600 hover:bg-emerald-500 px-3.5 py-1.5 rounded-lg transition flex items-center gap-1.5 shadow-xs">
                            <i data-lucide="zap" class="w-3 h-3 text-emerald-200"></i>
                            <span>Buy Kernel License ($249)</span>
                        </a>
                    </div>
                </div>"""

c1 = old_nav in content_norm
c2 = old_card_footer in content_norm

print(f"Matched projects nav: {c1}")
print(f"Matched card footer : {c2}")

if c1:
    content_norm = content_norm.replace(old_nav, new_nav, 1)
if c2:
    content_norm = content_norm.replace(old_card_footer, new_card_footer, 1)

proj_path.write_text(content_norm.replace("\n", "\r\n"), encoding="utf-8")
print("SUCCESS: projects.html updated!")
