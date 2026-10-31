import re
import sys
from pathlib import Path

# Set UTF-8 encoding
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PORTFOLIO_DIR = Path(r"C:\Users\rehan\Desktop\website_builder\Deployed_Websites\mohammadrehan.pages.dev")

def update_index_html():
    file_path = PORTFOLIO_DIR / "index.html"
    content = file_path.read_text(encoding="utf-8")
    original_len = len(content)

    # 1. Meta tags
    content = content.replace(
        "Creator of AegisDB (2.62M ops/sec), The Holy Trinity antifragility engine, and live options execution engines on AWS Mumbai.",
        "Developer of AegisDB (2.62M ops/sec), 3-AZ Fault-Tolerant Distributed Quorum, and Systematic Execution Engines on AWS Mumbai."
    )

    # 2. Navigation Telemetry -> Architecture Lab
    content = content.replace(
        '<a class="hover:text-slate-900 transition" href="#interactive-lab">Telemetry</a>',
        '<a class="hover:text-slate-900 transition" href="#interactive-lab">Architecture Lab</a>'
    )
    content = content.replace(
        '<a class="block py-2 px-3 rounded-lg hover:bg-slate-50 text-slate-600 font-medium text-sm" href="#interactive-lab">Telemetry</a>',
        '<a class="block py-2 px-3 rounded-lg hover:bg-slate-50 text-slate-600 font-medium text-sm" href="#interactive-lab">Architecture Lab</a>'
    )

    # 3. Hero metrics and tags
    content = content.replace(
        '<p class="text-2xl font-bold font-mono text-cyan-600">&lt;10µs</p>\n<p class="text-xs text-slate-500 mt-0.5 font-medium">Risk Gate Latency</p>',
        '<p class="text-2xl font-bold font-mono text-cyan-600">&lt;1µs</p>\n<p class="text-xs text-slate-500 mt-0.5 font-medium">In-Memory Compute</p>'
    )
    content = content.replace(
        '<span class="bg-indigo-50/90 text-indigo-900 border border-indigo-200/70 text-[11px] px-2.5 py-1 rounded-lg font-medium transition hover:scale-105">The Holy Trinity Architecture</span>',
        '<span class="bg-indigo-50/90 text-indigo-900 border border-indigo-200/70 text-[11px] px-2.5 py-1 rounded-lg font-medium transition hover:scale-105">3-AZ Fault-Tolerant Quorum</span>'
    )
    content = content.replace(
        '<span class="bg-slate-100 hover:bg-slate-200 text-slate-800 text-[11px] px-2.5 py-1 rounded-lg font-medium transition hover:scale-105">Zero-Loss Ash Ledgers</span>',
        '<span class="bg-slate-100 hover:bg-slate-200 text-slate-800 text-[11px] px-2.5 py-1 rounded-lg font-medium transition hover:scale-105">Deterministic WAL Persistence</span>'
    )

    # 4. Remove phantom PyPI and fix AegisOps description
    content = content.replace(
        'downloadable Python SDK (<code class="text-xs bg-indigo-50 text-indigo-700 px-1.5 py-0.5 rounded font-mono">pip install aegisops</code>)',
        'proprietary Python SDK (<code class="text-xs bg-indigo-50 text-indigo-700 px-1.5 py-0.5 rounded font-mono">internal monorepo SDK</code>)'
    )

    # 5. Fix Options Engine description (distinguish compute vs network latency)
    content = content.replace(
        'Cloud-native execution nodes on AWS Mumbai executing systematic options scalping with connection-pooled WebSockets, deterministic sub-10µs in-memory risk tribunal, and Directional Toxicity intelligence (9/9 Pytest passed).',
        'Cloud-native execution nodes on AWS Mumbai (ap-south-1) executing systematic options strategies with connection-pooled WebSockets, deterministic sub-microsecond (&lt;1µs) in-memory risk bitmask verification (~1.2ms broker wire transit), exchange-native Stop-Loss Limit orders with 1.5% protection buffer, and post-trade audits (17/17 Invariant Tests Passed).'
    )

    # 6. Ash Ledger -> WAL explanation
    content = content.replace(
        'Write-Ahead Micro-Journaling (Ash Ledger):</strong> Every state mutation, trade tick, and customer transaction is pre-journaled with SHA cryptographic checksums before memory commitment, making data loss mathematically impossible.',
        'Write-Ahead Micro-Journaling (WAL):</strong> High-throughput append-only transaction logging with SHA-256 state checkpointing before memory commitment, guaranteeing crash resilience and zero uncommitted state loss.'
    )

    # 7. Metrics row
    content = content.replace(
        '<p class="text-2xl sm:text-3xl font-extrabold text-indigo-400 font-mono">&lt;10µs</p>\n                <p class="text-xs text-slate-400 mt-1 uppercase tracking-wider font-semibold">Deterministic Memory Filter</p>',
        '<p class="text-2xl sm:text-3xl font-extrabold text-indigo-400 font-mono">&lt;1µs</p>\n                <p class="text-xs text-slate-400 mt-1 uppercase tracking-wider font-semibold">In-Memory Compute (&lt;1µs CPU / ~1.2ms Wire)</p>'
    )

    # 8. Founder title
    content = content.replace(
        'Store &amp; Operations Manager (Ladies Zone) | BCA (2025) | Software Architect &amp; Tech Lead',
        'Founder &amp; Operations Lead (Ladies Zone Patna) | Self-Taught Distributed Systems Engineer | BCA (2025)'
    )

    # 9. Simulation Lab rebranding
    content = content.replace(
        '<span>LIVE TELEMETRY &amp; FAULT SIMULATION LAB</span>',
        '<span>INTERACTIVE ARCHITECTURAL SANDBOX &amp; FAULT LAB</span>'
    )
    content = content.replace(
        "Test the actual failure recovery mechanisms in real-time. Trigger simulated process faults, verify Spot/VWAP risk circuits, and inspect your own browser's active Ash Ledger micro-journal.",
        "Interactive client-side architectural simulation: Test real-time failure recovery mechanisms, verify Spot/VWAP risk circuit bitmasks, and inspect the browser-local Write-Ahead Log (WAL) journal simulation."
    )

    # 10. Node 3 & buttons
    content = content.replace(
        '<!-- Node 3: Ash Ledger WAL -->',
        '<!-- Node 3: Append-Only WAL Journal -->'
    )
    content = content.replace(
        '<span>DURABILITY // MMAP_WAL</span>',
        '<span>DURABILITY // MMAP_WAL</span>'
    )
    content = content.replace(
        '🔍 Inspect Ash Ledger',
        '🔍 Inspect WAL State Journal'
    )
    content = content.replace(
        '• Click <strong class="text-cyan-300">"Inspect Ash Ledger"</strong> to query your own browser\'s active write-ahead micro-journal.',
        '• Click <strong class="text-cyan-300">"Inspect WAL State Journal"</strong> to query the browser-local write-ahead journal simulation.'
    )
    content = content.replace(
        '<span>🧬 Run Live Evolution Telemetry</span>',
        '<span>🧬 Simulate Fault &amp; Recovery Loop</span>'
    )
    content = content.replace(
        'Verified by Phoenix Sentinel',
        'Supervised by Systemd Watchdog Protocol'
    )
    content = content.replace(
        '3.02 ms (mmap Ash Ledger Replay)',
        '3.02 ms (mmap WAL Journal Replay)'
    )

    # 11. Projects filter & project names
    content = content.replace(
        '<button class="project-filter-btn px-4 py-2 rounded-xl text-xs font-medium bg-white text-slate-700 border border-slate-200 hover:bg-slate-50 transition" data-filter="phoenix" onclick="filterProjects(\'phoenix\')">The Holy Trinity</button>',
        '<button class="project-filter-btn px-4 py-2 rounded-xl text-xs font-medium bg-white text-slate-700 border border-slate-200 hover:bg-slate-50 transition" data-filter="phoenix" onclick="filterProjects(\'phoenix\')">Antifragile Triad</button>'
    )
    content = content.replace(
        '<h3 class="text-xl font-bold text-slate-900">The Holy Trinity: Aegis • Chaos • Phoenix</h3>',
        '<h3 class="text-xl font-bold text-slate-900">Antifragile Triad Architecture: Aegis Shield • Chaos Invariants • Phoenix Recovery</h3>'
    )
    content = content.replace(
        '<span class="bg-slate-100 text-slate-700 text-[11px] px-2.5 py-1 rounded-md font-medium">Ash Ledger WAL</span>',
        '<span class="bg-slate-100 text-slate-700 text-[11px] px-2.5 py-1 rounded-md font-medium">Append-Only WAL Engine</span>'
    )

    # 12. Indian options card
    content = content.replace(
        '7-Stage Multi-Factor Execution Tribunal (&lt;10µs memory gate)',
        '7-Stage Multi-Factor Execution Tribunal (&lt;1µs in-memory compute, ~1.2ms wire transit)'
    )
    content = content.replace(
        '<span class="bg-slate-100 text-slate-700 text-[11px] px-2.5 py-1 rounded-md font-medium">Sub-10µs Risk Gate</span>',
        '<span class="bg-slate-100 text-slate-700 text-[11px] px-2.5 py-1 rounded-md font-medium">Sub-Microsecond Risk Bitmask</span>'
    )

    # 13. JS simulation console output
    content = content.replace(
        '0 lost bytes in Ash Ledger',
        '0 lost bytes in WAL Journal'
    )

    file_path.write_text(content, encoding="utf-8")
    print(f"Updated index.html: {original_len} -> {len(content)} bytes")

def update_projects_html():
    file_path = PORTFOLIO_DIR / "projects.html"
    content = file_path.read_text(encoding="utf-8")
    original_len = len(content)

    # 1. AegisDB
    content = content.replace(
        "Group Commit Ash Ledger Write-Ahead Logging (WAL)",
        "Deterministic Group Commit Write-Ahead Logging (WAL)"
    )
    content = content.replace(
        "Ash Ledger WAL Group Commit (13.57ms MTTR)",
        "Deterministic WAL Group Commit (13.57ms MTTR)"
    )
    content = content.replace(
        '<span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200 font-mono">Ash Ledger WAL</span>',
        '<span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200 font-mono">Append-Only WAL Engine</span>'
    )

    # 2. AegisOps - eliminate pip install aegisops
    content = content.replace(
        'downloadable client resilience SDK (<code class="text-xs bg-slate-100 px-1 py-0.5 rounded font-mono">pip install aegisops</code>)',
        'client resilience SDK (<code class="text-xs bg-slate-100 px-1 py-0.5 rounded font-mono">git clone / private monorepo SDK</code>)'
    )
    content = content.replace(
        '<span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200 font-mono">pip install aegisops</span>',
        '<span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200 font-mono">Internal Monorepo SDK</span>'
    )

    # 3. Holy Trinity references
    content = content.replace(
        '"The Holy Trinity: Aegis • Chaos • Phoenix (<10ms MTTR)"',
        '"Antifragile Triad: Aegis • Chaos • Phoenix (<10ms MTTR)"'
    )

    file_path.write_text(content, encoding="utf-8")
    print(f"Updated projects.html: {original_len} -> {len(content)} bytes")

def update_experience_html():
    file_path = PORTFOLIO_DIR / "experience.html"
    content = file_path.read_text(encoding="utf-8")
    original_len = len(content)

    # 1. Holy Trinity -> Multi-Node Quorum
    content = content.replace(
        '<span class="text-sm font-bold text-emerald-600 block mt-0.5">The Holy Trinity</span>',
        '<span class="text-sm font-bold text-emerald-600 block mt-0.5">3-AZ Multi-Node Quorum</span>'
    )

    # 2. AegisDB bullets
    content = content.replace(
        "Engineered AegisDB: Microsecond in-memory database achieving 21.4M SIMD ops/sec (0.39µs AVX2 kernel), 2.62M reads/sec, Stoikov micro-pricing, and sub-15ms Ash Ledger WAL recovery (20/20 Pytest Passed).",
        "Engineered AegisDB: In-memory state engine achieving 21.4M SIMD ops/sec (46.69ns AVX2 kernel), 2.62M reads/sec, Stoikov micro-pricing math, and sub-15ms WAL recovery (20/20 Invariant Tests Passed)."
    )

    # 3. Indian Options Sniper bullets
    content = content.replace(
        "Architected and deployed the Indian Quant Options Sniper: systematic options execution engine with sub-10µs in-memory bitmask risk matrix, Directional Toxicity intelligence, and post-trade execution audits on AWS Mumbai (17/17 Pytest Passed).",
        "Architected and deployed the Indian Quant Options Sniper: systematic options execution engine with sub-microsecond in-memory bitmask risk verification (<1µs compute, ~1.2ms AWS Mumbai wire transit), exchange-native Stop-Loss Limit orders with 1.5% protection buffer, and post-trade audits (17/17 Invariant Tests Passed)."
    )

    # 4. Ladies Zone title and experience description
    content = content.replace(
        '<span id="experience-role-rotator">Store Manager &amp; Lead Systems Architect</span>',
        '<span id="experience-role-rotator">Operations Lead &amp; Systems Architect</span>'
    )
    content = content.replace(
        '<h3 class="text-xl font-bold text-slate-900 mt-0.5">Store Manager &amp; Lead Systems Architect</h3>',
        '<h3 class="text-xl font-bold text-slate-900 mt-0.5">Store &amp; Operations Manager</h3>'
    )

    file_path.write_text(content, encoding="utf-8")
    print(f"Updated experience.html: {original_len} -> {len(content)} bytes")

if __name__ == "__main__":
    update_index_html()
    update_projects_html()
    update_experience_html()
    print("ALL HTML FILES SANITIZED TO GRANITE STANDARDS!")
