import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

portfolio_dir = r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev"
index_path = os.path.join(portfolio_dir, "index.html")
projects_path = os.path.join(portfolio_dir, "projects.html")

raadha_card = """<!-- Project 6: Raadha Rani Patna Commercial Client Deployment -->
            <div class="project-card hover-lift-card bg-slate-900 text-white rounded-2xl border-2 border-amber-500/40 overflow-hidden shadow-lg hover:border-amber-400 hover:shadow-xl transition duration-300 flex flex-col justify-between" data-category="client retail" data-project-category="client">
                <div class="p-8">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 text-xs font-semibold border border-amber-400/40 font-mono">
                            <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
                            Live Client Deployment &bull; Ashiana-Digha Road, Patna
                        </span>
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-bold text-amber-300 bg-amber-950/90 border border-amber-500/40 px-2.5 py-0.5 rounded font-mono">raadha-rani-patna.pages.dev</span>
                        </div>
                    </div>

                    <div class="mb-4 rounded-xl overflow-hidden border border-slate-800 bg-slate-950">
                        <img src="https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80" alt="Raadha Rani Patna Bridal Mall & Runway" class="w-full h-48 sm:h-56 object-cover hover:scale-105 transition duration-500" loading="lazy" />
                    </div>

                    <h3 class="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>Raadha Rani Patna</span>
                        <span class="text-xs font-mono text-amber-400 font-normal">v2.0-LIVE</span>
                    </h3>
                    <p class="text-xs font-mono text-emerald-400 font-semibold mt-1">Bihar’s 1st Ladies Mall &amp; In-Store Bridal Fashion Runway Showroom</p>
                    <p class="mt-3 text-slate-300 text-sm sm:text-base leading-relaxed">
                        Flagship digital showroom for Bihar’s premier bridal destination. Features an interactive 360° in-store fashion runway catwalk trial booking system, 30 verified customer reviews &amp; playable unboxing videos (Google, Instagram, YouTube, Facebook), 4-tier bridal trousseau curation, zero-bargain haute couture presentation, and a stealth laptop-locked hardware admin console.
                    </p>

                    <div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3 text-center font-mono">
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase">Architecture</div>
                            <div class="text-sm font-bold text-amber-400 mt-0.5">120 FPS</div>
                            <div class="text-[10px] text-slate-500">GPU Composited</div>
                        </div>
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase">Reviews &amp; Videos</div>
                            <div class="text-sm font-bold text-emerald-400 mt-0.5">30 Verified</div>
                            <div class="text-[10px] text-slate-500">Google • Insta • YT</div>
                        </div>
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase">Runway Trials</div>
                            <div class="text-sm font-bold text-purple-400 mt-0.5">Catwalk 360°</div>
                            <div class="text-[10px] text-slate-500">Stage Lights</div>
                        </div>
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                            <div class="text-[10px] text-slate-400 uppercase">Admin Security</div>
                            <div class="text-sm font-bold text-cyan-400 mt-0.5">Hardware Bound</div>
                            <div class="text-[10px] text-slate-500">Owner Laptop Only</div>
                        </div>
                    </div>
                </div>

                <div class="p-8 pt-0 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-4 mt-4">
                    <span class="text-xs text-slate-400 font-mono">Client: Raadha Rani Ladies Mall, Ashiana-Digha Road, Patna</span>
                    <a href="https://raadha-rani-patna.pages.dev" target="_blank" rel="noopener noreferrer" class="text-xs font-bold text-slate-950 bg-amber-400 hover:bg-amber-300 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-amber-950/40">
                        <span>Visit Live Showroom</span>
                        <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                    </a>
                </div>
            </div>
"""

for target_file in [index_path, projects_path]:
    if not os.path.exists(target_file):
        print(f"File not found: {target_file}")
        continue
    
    with open(target_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # 1. Update Ali Mobile address if old
    content = content.replace("Client: Ali Mobile, Sabzibagh, Patna", "Client: Ali Mobile, Satyanarayan Market, Boring Road Chauraha, Patna")
    
    # 2. Insert Raadha Rani card if not already present
    if "raadha-rani-patna.pages.dev" not in content:
        # Insert after Ali Mobile card closing div
        ali_marker = "https://ali-mobile-patna.pages.dev"
        idx = content.find(ali_marker)
        if idx != -1:
            div_close = content.find("</div>", idx)
            if div_close != -1:
                # Find the enclosing card's closing </div>
                next_div = content.find("</div>", div_close + 6)
                if next_div != -1:
                    insert_pos = next_div + 6
                    content = content[:insert_pos] + "\n\n" + raadha_card + content[insert_pos:]
                    print(f"✅ Inserted Raadha Rani card into {os.path.basename(target_file)}")
    else:
        print(f"ℹ️ Raadha Rani card already present in {os.path.basename(target_file)}")

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)

print("🎉 Finished updating portfolio HTML files.")
