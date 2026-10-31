import os

path = r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev\projects.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Desktop Nav
nav_needle = '<a class="text-slate-900 font-semibold border-b-2 border-slate-900 pb-1" href="projects.html">Projects</a>'
nav_replace = nav_needle + '\n<a class="hover:text-slate-900 transition flex items-center gap-1 font-bold text-cyan-700 hover:text-cyan-900" href="aegis.html"><span>RQL Aegis™</span><span class="bg-cyan-100 text-cyan-800 text-[10px] px-1.5 py-0.5 rounded-full font-bold">SOFTWARE</span></a>'

# 2. Product Banner above Projects Grid
grid_needle = '<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">'
banner_html = '''
<!-- COMMERCIAL PRODUCT BANNER: RQL AEGIS -->
<div class="mb-10 bg-slate-950 text-white rounded-3xl p-6 sm:p-8 border border-cyan-500/40 shadow-xl relative overflow-hidden">
    <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
        <div class="space-y-2 max-w-2xl">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-950 border border-cyan-500/30 text-cyan-300 text-xs font-semibold">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>FLAGSHIP COMMERCIAL SOFTWARE RELEASE • V1.0</span>
            </div>
            <h3 class="text-2xl font-black text-white tracking-tight">🛡️ RQL Aegis™ — Sovereign On-Premises Trading Risk Middleware</h3>
            <p class="text-slate-300 text-sm leading-relaxed">
                The unkillable execution shield with Non-Newtonian Liquid Armor and SHA-256 Trade WAL. Air-gapped on your PC. Zero cloud leakage. Compatible with Zerodha, IBKR, Dhan, and Fyers.
            </p>
            <div class="flex flex-wrap items-center gap-2 pt-1">
                <span class="bg-slate-900 border border-slate-800 px-2.5 py-1 rounded text-xs text-cyan-300 font-mono">100% Air-Gapped</span>
                <span class="bg-slate-900 border border-slate-800 px-2.5 py-1 rounded text-xs text-emerald-300 font-mono">&lt;1ms Latency</span>
                <span class="bg-slate-900 border border-slate-800 px-2.5 py-1 rounded text-xs text-amber-300 font-mono">Pay Once $249</span>
            </div>
        </div>
        <div class="flex flex-wrap lg:flex-col gap-3 shrink-0 w-full sm:w-auto">
            <a href="aegis.html" class="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-slate-950 font-extrabold text-xs sm:text-sm px-6 py-3 rounded-xl transition text-center shadow-lg shadow-cyan-500/20">
                View Aegis Product Page
            </a>
            <a href="RQL-Aegis-v1.0-Release.zip" download class="bg-slate-800 hover:bg-slate-700 text-white font-semibold text-xs sm:text-sm px-5 py-2.5 rounded-xl border border-slate-700 transition text-center flex items-center justify-center gap-2">
                <i class="w-4 h-4 text-cyan-400" data-lucide="download"></i>
                <span>Download v1.0 ZIP</span>
            </a>
        </div>
    </div>
</div>
'''

assert nav_needle in content, 'Nav needle not found in projects.html'
assert grid_needle in content, 'Grid needle not found in projects.html'

content = content.replace(nav_needle, nav_replace, 1)
content = content.replace(grid_needle, banner_html + '\n' + grid_needle, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully injected Commercial Banner into projects.html!")
