import os
from pathlib import Path

BASE_DIR = Path(r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev")
index_path = BASE_DIR / "index.html"

content = index_path.read_text(encoding="utf-8")

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

# 2. Mobile Nav
old_mob = """        <a class="block py-2 px-3 rounded-lg bg-cyan-50 text-cyan-900 font-bold text-sm flex items-center justify-between" href="aegis.html">
            <span>RQL Aegis™ (Commercial Middleware)</span>
            <span class="bg-cyan-200 text-cyan-950 text-[10px] px-2 py-0.5 rounded-full font-bold">$249</span>
        </a>"""

new_mob = """        <a class="block py-2 px-3 rounded-lg bg-cyan-50 text-cyan-900 font-bold text-sm flex items-center justify-between" href="aegis.html">
            <span>RQL Aegis™ (Risk Middleware)</span>
            <span class="bg-cyan-200 text-cyan-950 text-[10px] px-2 py-0.5 rounded-full font-bold">$249</span>
        </a>
        <a class="block py-2 px-3 rounded-lg bg-emerald-50 text-emerald-900 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE" target="_blank" rel="noopener noreferrer">
            <span>Deterministic State Kernel™ (Rust)</span>
            <span class="bg-emerald-200 text-emerald-950 text-[10px] px-2 py-0.5 rounded-full font-bold">$249</span>
        </a>"""

# 3. Hero Card
old_card = """<!-- RQL Aegis™ Production Risk Engine Showcase Card -->
<div class="mt-7 p-4 sm:p-5 rounded-2xl bg-white border border-slate-200 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 max-w-xl">
    <div class="flex items-start sm:items-center gap-3.5">
        <div class="w-10 h-10 rounded-xl bg-slate-900 border border-slate-800 text-cyan-400 flex items-center justify-center shrink-0 shadow-sm">
            <i class="w-5 h-5" data-lucide="shield"></i>
        </div>
        <div>
            <div class="flex flex-wrap items-center gap-2">
                <span class="font-bold text-slate-900 text-sm sm:text-base">RQL Aegis™ — On-Premises Trading Risk Engine</span>
                <span class="bg-cyan-100 text-cyan-900 border border-cyan-200 text-[10px] px-2 py-0.5 rounded font-mono font-bold uppercase tracking-wider">v1.0 (PROD)</span>
            </div>
            <p class="text-xs text-slate-600 mt-1">Continuous Volatility Clamping (&sigma;-Adaptive) • SHA-256 WAL • &lt;1µs Latency</p>
        </div>
    </div>
    <div class="flex items-center gap-2 shrink-0 w-full sm:w-auto justify-end">
        <a href="aegis.html" class="w-full sm:w-auto bg-slate-900 hover:bg-slate-800 text-white font-semibold text-xs px-4 py-2.5 rounded-xl transition flex items-center justify-center gap-1.5 whitespace-nowrap">
            <span>Inspect Engine ($249)</span>
            <i class="w-3.5 h-3.5 text-cyan-400" data-lucide="arrow-right"></i>
        </a>
    </div>
</div>"""

kernel_card = """

<!-- Deterministic State Kernel™ Rust Bare-Metal Showcase Card -->
<div class="mt-3.5 p-4 sm:p-5 rounded-2xl bg-white border border-slate-200 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 max-w-xl">
    <div class="flex items-start sm:items-center gap-3.5">
        <div class="w-10 h-10 rounded-xl bg-slate-900 border border-slate-800 text-emerald-400 flex items-center justify-center shrink-0 shadow-sm">
            <i class="w-5 h-5" data-lucide="cpu"></i>
        </div>
        <div>
            <div class="flex flex-wrap items-center gap-2">
                <span class="font-bold text-slate-900 text-sm sm:text-base">Deterministic State Kernel™ — Rust Bare-Metal Engine</span>
                <span class="bg-emerald-100 text-emerald-900 border border-emerald-200 text-[10px] px-2 py-0.5 rounded font-mono font-bold uppercase tracking-wider">v1.0 (PROD)</span>
            </div>
            <p class="text-xs text-slate-600 mt-1">MCA Rule 11(g) Compliant • &gt;240k Writes/sec • 604ns Read Latency • SHA-256 WAL</p>
        </div>
    </div>
    <div class="flex items-center gap-2 shrink-0 w-full sm:w-auto justify-end">
        <a href="https://quantify17.gumroad.com/l/deterministic-state-kernel/ENTERPRISE" target="_blank" rel="noopener noreferrer" class="w-full sm:w-auto bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs px-4 py-2.5 rounded-xl transition flex items-center justify-center gap-1.5 whitespace-nowrap shadow-sm">
            <span>Acquire License ($249)</span>
            <i class="w-3.5 h-3.5 text-emerald-200" data-lucide="arrow-right"></i>
        </a>
    </div>
</div>"""

new_card = old_card + kernel_card

# Normalizing line breaks for replace
content_norm = content.replace("\r\n", "\n")
old_nav_norm = old_nav.replace("\r\n", "\n")
new_nav_norm = new_nav.replace("\r\n", "\n")
old_mob_norm = old_mob.replace("\r\n", "\n")
new_mob_norm = new_mob.replace("\r\n", "\n")
old_card_norm = old_card.replace("\r\n", "\n")
new_card_norm = new_card.replace("\r\n", "\n")

c1 = old_nav_norm in content_norm
c2 = old_mob_norm in content_norm
c3 = old_card_norm in content_norm

print(f"Matched desktop nav: {c1}")
print(f"Matched mobile nav : {c2}")
print(f"Matched hero card  : {c3}")

if c1:
    content_norm = content_norm.replace(old_nav_norm, new_nav_norm, 1)
if c2:
    content_norm = content_norm.replace(old_mob_norm, new_mob_norm, 1)
if c3:
    content_norm = content_norm.replace(old_card_norm, new_card_norm, 1)

# Write back with CRLF
index_path.write_text(content_norm.replace("\n", "\r\n"), encoding="utf-8")
print("SUCCESS: index.html updated with Deterministic State Kernel!")
