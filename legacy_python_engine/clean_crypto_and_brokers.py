import os
import re

site_dir = r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev"

# 1. Update projects.html - Replace Crypto Engine with Veritas Dossier Compliance Vault
projects_path = os.path.join(site_dir, "projects.html")
if os.path.exists(projects_path):
    with open(projects_path, "r", encoding="utf-8") as f:
        c = f.read()

    old_crypto_card_pattern = r'<!-- Project 0: Aegis Automation Service.*?<!-- Project 1: RQL Aegis Enterprise Systems Supervisor -->'
    new_veritas_card = '''<!-- Project 0: Veritas Dossier Immutable Audit & Compliance Engine -->
            <div class="project-card bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:border-slate-400 hover:shadow-md transition duration-300 flex flex-col justify-between" data-category="systems">
                <div class="p-8">
                    <div class="flex items-center justify-between mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 text-xs font-semibold border border-emerald-200">
                            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                            Production Compliance Engine
                        </span>
                        <span class="text-xs text-slate-400 font-medium">Enterprise Audit &amp; Data Integrity</span>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 tracking-tight">Veritas Dossier™ — Immutable Cryptographic Compliance Vault</h3>
                    <p class="mt-3 text-slate-600 text-sm sm:text-base leading-relaxed">
                        An enterprise-grade, tamper-evident audit logging and regulatory compliance engine. Features sequential SHA-256 cryptographic chain hashing, atomic fsync write durability, zero-knowledge verification proofs, and automated PDF audit report generation under strict evidentiary standards.
                    </p>
                    <div class="mt-6 space-y-2">
                        <h4 class="text-xs font-semibold uppercase tracking-wider text-slate-400">Architectural Highlights</h4>
                        <ul class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm text-slate-700">
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                SHA-256 Merkle-Linked Event Ledger
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Atomic Physical fsync Durability
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                Ed25519 Cryptographic Verification
                            </li>
                            <li class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-slate-900 flex-shrink-0"></i>
                                100% Invariant Validation Suite
                            </li>
                        </ul>
                    </div>
                    <div class="mt-6 flex flex-wrap gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Python 3.14</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">SQLite WAL</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">SHA-256 Ledger</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">ReportLab PDF</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-medium border border-slate-200">Enterprise Security</span>
                    </div>
                </div>
                <div class="px-8 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                    <span class="text-xs text-slate-500 font-medium">Status: Enterprise Production Ready</span>
                    <span class="text-xs font-semibold text-emerald-700 bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-lg">Commercial v2.0</span>
                </div>
            </div>

            <!-- Project 1: RQL Aegis Enterprise Systems Supervisor -->'''

    c = re.sub(old_crypto_card_pattern, new_veritas_card, c, flags=re.DOTALL)
    c = c.replace("4-Account Multi-Broker Family Fleet Execution", "Multi-Instance Distributed Process Swarm Execution")
    with open(projects_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated projects.html (Replaced Crypto Bot with Veritas Dossier)")

# 2. Update index.html
index_path = os.path.join(site_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        c = f.read()

    c = re.sub(
        r'<span><strong>Institutional Quant Derivatives Engines:</strong>.*?</span>',
        '<span><strong>High-Availability Distributed Systems:</strong> Cloud-native execution nodes on AWS Mumbai (ap-south-1) executing deterministic process pipelines with connection-pooled WebSockets, sub-microsecond in-memory state replication, SHA-256 WAL durability, and automated multi-zone consensus sentinels.</span>',
        c,
        flags=re.DOTALL
    )
    c = c.replace("a broker socket disconnection", "a network socket disconnection")
    c = c.replace("Brokers: Zerodha &bull; IBKR &bull; Shared Memory (IPC) &bull; Named Pipes", "Connectors: gRPC &bull; ZeroMQ &bull; Shared Memory (IPC) &bull; Named Pipes")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated index.html")

# 3. Update aegis.html
aegis_path = os.path.join(site_dir, "aegis.html")
if os.path.exists(aegis_path):
    with open(aegis_path, "r", encoding="utf-8") as f:
        c = f.read()
    c = c.replace("re-establishing idempotent broker connection states", "re-establishing idempotent connection states")
    with open(aegis_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated aegis.html")

print("Targeted replacements completed.")
