import os
import re

site_dir = r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev"

# 1. Update contact.html
contact_path = os.path.join(site_dir, "contact.html")
if os.path.exists(contact_path):
    with open(contact_path, "r", encoding="utf-8") as f:
        c = f.read()
    c = c.replace(
        "Institutional Quantitative Execution & Options Sniper Engine",
        "Distributed Systems Engineering & Enterprise Software Architecture"
    )
    with open(contact_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated contact.html")

# 2. Update experience.html
exp_path = os.path.join(site_dir, "experience.html")
if os.path.exists(exp_path):
    with open(exp_path, "r", encoding="utf-8") as f:
        c = f.read()
    # Replace sniper bullet point
    c = re.sub(
        r'<span>Architected and deployed the Indian Quant Options Sniper:.*?\(17/17 Invariant Tests Passed\)\.</span>',
        '<span>Architected and deployed RQL Aegis: distributed deterministic process supervisor with SHA-256 WAL checkpointing (<1µs in-memory state transition), automated kernel heartbeat sentinels, and zero-loss crash recovery.</span>',
        c,
        flags=re.DOTALL
    )
    # Replace chat bot knowledge
    c = c.replace("Indian Quant Options Sniper (systematic options execution on AWS Mumbai with Kotak Neo broker API)", "RQL Aegis Distributed Systems Engine (high-availability deterministic process supervisor)")
    c = c.replace("kotak", "aegis")
    with open(exp_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated experience.html")

# 3. Update index.html
index_path = os.path.join(site_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        c = f.read()
    
    # Replace Project 2 Card in index.html
    old_card_pattern = r'<!-- Project 2: Indian Quant Options Sniper -->.*?<!-- Project 3: Autonomous AI Shorts & Reels Studio -->'
    new_card = '''<!-- Project 2: RQL Aegis Distributed Systems Engine -->
<div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md hover:border-slate-400 transition flex flex-col justify-between" data-project-category="systems">
<div class="p-6 space-y-4">
<div class="flex items-center justify-between">
<span class="bg-indigo-50 text-indigo-700 text-xs font-semibold px-2.5 py-1 rounded-lg">High-Availability Engine</span>
<span class="text-xs text-emerald-600 font-mono font-semibold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">100% Invariants Passed</span>
</div>
<h3 class="text-xl font-bold text-slate-900">RQL Aegis — Process Supervisor</h3>
<p class="text-slate-600 text-sm leading-relaxed">
    Enterprise deterministic process supervisor and high-availability watchdog. Features native SHA-256 WAL state durability, sub-microsecond in-memory state replication (&lt;1µs latency), and automatic multi-zone consensus sentinels.
</p>
<div class="flex flex-wrap gap-1.5 pt-2">
<span class="bg-slate-100 text-slate-700 text-[11px] px-2.5 py-1 rounded-md font-medium">SHA-256 WAL</span>
<span class="bg-slate-100 text-slate-700 text-[11px] px-2.5 py-1 rounded-md font-medium">Rust Core</span>
<span class="bg-slate-100 text-slate-700 text-[11px] px-2.5 py-1 rounded-md font-medium">Sub-Microsecond Dispatch</span>
<span class="bg-slate-100 text-slate-700 text-[11px] px-2.5 py-1 rounded-md font-medium">Multi-AZ Quorum</span>
</div>
</div>
<div class="px-6 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
<a class="text-xs font-semibold text-slate-900 hover:underline flex items-center gap-1.5" href="aegis.html">
<span>View Architecture</span>
<i class="w-3.5 h-3.5" data-lucide="arrow-right"></i>
</a>
<span class="text-[10px] text-indigo-600 font-semibold bg-indigo-50 px-2 py-0.5 rounded">Commercial v1.0</span>
</div>
</div>

<!-- Project 3: Autonomous AI Shorts & Reels Studio -->'''
    c = re.sub(old_card_pattern, new_card, c, flags=re.DOTALL)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated index.html")

# 4. Update projects.html
projects_path = os.path.join(site_dir, "projects.html")
if os.path.exists(projects_path):
    with open(projects_path, "r", encoding="utf-8") as f:
        c = f.read()

    c = c.replace("Indian Trading Bot — Multi-Agent Options Sniper", "RQL Aegis — Distributed Systems & High-Availability Engine")
    c = c.replace("Indian Trading Bot", "RQL Aegis")
    c = c.replace("systematic quant options sniper engines", "distributed high-availability systems engines")
    c = c.replace("Indian Quant Options Sniper", "RQL Aegis Systems Supervisor")
    c = c.replace("Kotak Neo API", "Native Rust Core")
    c = c.replace("Kotak Neo broker API", "High-Performance Systems Architecture")
    c = c.replace("An institutional-grade, multi-agent algorithmic options sniper engineered for Indian derivatives (NIFTY, BANKNIFTY, SENSEX). Features 5-Pillar confluence detection, multi-index basket scanning, sub-second execution, automated iceberg order slicing, a permanent ₹1 Lakh floor dividend sweep mechanism, 4-account family fleet execution, and a 4-layer mathematical stealth armor.",
                  "An institutional-grade, deterministic process supervisor and high-availability engine. Features native SHA-256 WAL state persistence, sub-microsecond in-memory state replication, automated failover sentinels across multi-zone infrastructure, and tamper-evident audit journals.")
    with open(projects_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated projects.html")

print("Website clean-up finished successfully!")
