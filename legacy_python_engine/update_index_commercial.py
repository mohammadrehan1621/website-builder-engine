import os

path = r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Desktop Nav
nav_needle = '<a class="hover:text-slate-900 transition" href="projects.html">Projects</a>'
nav_replace = nav_needle + '\n<a class="hover:text-slate-900 transition flex items-center gap-1 font-bold text-cyan-700 hover:text-cyan-900" href="aegis.html"><span>RQL Aegis™</span><span class="bg-cyan-100 text-cyan-800 text-[10px] px-1.5 py-0.5 rounded-full font-bold">SOFTWARE</span></a>'

# 2. Mobile Nav
mob_needle = '<a class="block py-2 px-3 rounded-lg hover:bg-slate-50 text-slate-600 font-medium text-sm" href="projects.html">Projects</a>'
mob_replace = mob_needle + '\n<a class="block py-2 px-3 rounded-lg hover:bg-slate-50 text-cyan-700 font-semibold text-sm flex items-center justify-between" href="aegis.html"><span>RQL Aegis™ (Trading Risk Middleware)</span><span class="bg-cyan-100 text-cyan-800 text-[10px] px-2 py-0.5 rounded-full font-bold">$249</span></a>'

# 3. Commercial Section
comm_section = '''
<!-- COMMERCIAL SYSTEMS & PRODUCTS (RQL AEGIS) -->
<section class="py-14 sm:py-16 bg-slate-950 text-white border-t border-slate-800 relative overflow-hidden" id="commercial-systems">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
            <div>
                <span class="text-xs font-bold uppercase tracking-widest text-cyan-400 bg-cyan-950/80 border border-cyan-500/30 px-3 py-1 rounded-full">Commercial Software Suite</span>
                <h2 class="text-3xl font-extrabold text-white tracking-tight mt-3">Production Trading Systems &amp; Risk Middleware</h2>
            </div>
            <a class="inline-flex items-center gap-2 text-sm font-semibold text-cyan-400 hover:text-cyan-300 transition" href="aegis.html">
                <span>View Product Dossier &amp; Architecture</span>
                <i class="w-4 h-4" data-lucide="arrow-right"></i>
            </a>
        </div>

        <div class="bg-gradient-to-br from-slate-900 to-slate-950 border border-cyan-500/40 rounded-3xl p-6 sm:p-10 shadow-2xl relative overflow-hidden">
            <div class="absolute -right-20 -top-20 w-80 h-80 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center relative z-10">
                <div class="lg:col-span-7 space-y-4">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-950/60 border border-cyan-500/30 text-cyan-300 text-xs font-semibold">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                        <span>SOVEREIGN ON-PREMISES RISK ENGINE</span>
                    </div>

                    <h3 class="text-2xl sm:text-3xl font-black text-white tracking-tight">
                        🛡️ RQL Aegis™ — Sovereign Trading Risk Middleware
                    </h3>

                    <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
                        The unkillable execution shield with <strong>Non-Newtonian Liquid Armor</strong> and <strong>SHA-256 Trade WAL</strong>. 
                        Air-gapped on your local PC. Zero cloud leakage. Zero recurring subscription bleed. 
                        Compatible with Zerodha Kite, Interactive Brokers (IBKR), Dhan &amp; Fyers.
                    </p>

                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2">
                        <div class="bg-slate-950/80 border border-slate-800 rounded-xl p-2.5 text-center">
                            <span class="text-xs font-bold text-cyan-400 block">100% Air-Gapped</span>
                            <span class="text-[10px] text-slate-400">Zero Cloud Leaks</span>
                        </div>
                        <div class="bg-slate-950/80 border border-slate-800 rounded-xl p-2.5 text-center">
                            <span class="text-xs font-bold text-emerald-400 block">&lt; 1ms Latency</span>
                            <span class="text-[10px] text-slate-400">Native Windows Binary</span>
                        </div>
                        <div class="bg-slate-950/80 border border-slate-800 rounded-xl p-2.5 text-center">
                            <span class="text-xs font-bold text-amber-400 block">SHA-256 WAL</span>
                            <span class="text-[10px] text-slate-400">Crash Recovery</span>
                        </div>
                        <div class="bg-slate-950/80 border border-slate-800 rounded-xl p-2.5 text-center">
                            <span class="text-xs font-bold text-indigo-400 block">Pay Once</span>
                            <span class="text-[10px] text-slate-400">Perpetual Rights</span>
                        </div>
                    </div>

                    <div class="flex flex-wrap items-center gap-3 pt-4">
                        <a href="RQL-Aegis-v1.0-Release.zip" download class="bg-slate-800 hover:bg-slate-700 text-white text-xs sm:text-sm font-semibold px-5 py-3 rounded-xl border border-slate-700 transition flex items-center gap-2">
                            <i class="w-4 h-4 text-cyan-400" data-lucide="download"></i>
                            <span>Download Standalone v1.0 (ZIP)</span>
                        </a>
                        <a href="aegis.html#pricing" class="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-slate-950 font-extrabold text-xs sm:text-sm px-6 py-3 rounded-xl shadow-lg shadow-cyan-500/20 transition flex items-center gap-2">
                            <i class="w-4 h-4" data-lucide="zap"></i>
                            <span>Buy Perpetual License — $249</span>
                        </a>
                    </div>
                </div>

                <div class="lg:col-span-5 bg-slate-950/90 border border-slate-800 rounded-2xl p-5 font-mono text-xs text-slate-300 space-y-2.5 shadow-inner">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                        <span class="text-cyan-400 font-bold">RQL-Aegis.exe // Terminal Runtime</span>
                        <span class="text-[10px] text-emerald-400 font-bold bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/30">ARMED</span>
                    </div>
                    <div class="text-slate-400">
                        &gt; Initializing Non-Newtonian Armor...<br />
                        &gt; VIX Volatility Clamping: <span class="text-emerald-400">ACTIVE</span><br />
                        &gt; Cryptographic SHA-256 WAL: <span class="text-emerald-400">SEALED (os.fsync)</span><br />
                        &gt; 3-Second Resurrection Sentinel: <span class="text-emerald-400">ARMED</span><br />
                        &gt; Machine Hardware ID: <span class="text-amber-300">[0B78F950D49FE5C5]</span><br />
                        &gt; Broker Connectors: Zerodha Kite, IBKR, Dhan, Fyers<br />
                        &gt; Port: 127.0.0.1:9099 [Sub-Millisecond Engine]
                    </div>
                    <div class="pt-2 border-t border-slate-800 flex items-center justify-between text-[11px]">
                        <span class="text-slate-400">Support Desk:</span>
                        <a href="mailto:founder@rehanquantlab.com" class="text-cyan-400 hover:underline">founder@rehanquantlab.com</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
'''

target_sec = '<!-- WHAT I BUILD & FEATURED PROJECTS TEASER -->'
assert nav_needle in content, 'Desktop nav needle not found'
assert mob_needle in content, 'Mobile nav needle not found'
assert target_sec in content, 'Projects teaser section not found'

content = content.replace(nav_needle, nav_replace, 1)
content = content.replace(mob_needle, mob_replace, 1)
content = content.replace(target_sec, comm_section + '\n' + target_sec, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully injected Commercial Systems into index.html!')
