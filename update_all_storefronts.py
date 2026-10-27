import os
import sys
import re
from pathlib import Path

# Configure Windows UTF-8 stdout
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PORTFOLIO_DIR = Path(r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev")

GUMROAD_MAPPING = {
    # Conduit
    r"https://quantify17\.gumroad\.com/l/RQLConduit(\?wanted=true)?": "https://quantify17.gumroad.com/l/RQLConduitBondingEngine",
    # State Kernel
    r"https://quantify17\.gumroad\.com/l/deterministic-state-kernel(/ENTERPRISE)?(\?wanted=true)?": "https://quantify17.gumroad.com/l/DeterministicStateKernel",
    # Aegis
    r"https://quantify17\.gumroad\.com/l/rql-aegis(/EARLYBIRD)?(\?wanted=true)?": "https://quantify17.gumroad.com/l/RQLAegisRiskMiddleware",
    # Veritas
    r"https://quantify17\.gumroad\.com/l/eucck(/VERITAS)?(\?wanted=true)?": "https://quantify17.gumroad.com/l/VeritasDossierForensicAuditor",
    # Sentinel
    r"https://quantify17\.gumroad\.com/l/ivyiwh(/SENTINEL)?(\?wanted=true)?": "https://quantify17.gumroad.com/l/IndustrialFragilitySentinel",
    # ExpressBill
    r"https://quantify17\.gumroad\.com/l/ExpressBill(\?wanted=true)?": "https://quantify17.gumroad.com/l/ExpressBillPOS",
}

def update_file_links(file_path):
    print(f"Updating Gumroad links in: {file_path.name}")
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    original = content

    for pattern, replacement in GUMROAD_MAPPING.items():
        content = re.sub(pattern, replacement, content)

    # Update ExpressBill image to new 1080p cover if present
    content = content.replace("ExpressBill_POS_Commercial_Hero.webp", "06_ExpressBill_POS_Cover_1080p.png")
    content = content.replace("ExpressBill_POS_Commercial_Hero.jpg", "06_ExpressBill_POS_Cover_1080p.png")
    content = content.replace("05_rql_conduit_bonding_engine_1080p.webp", "01_RQL_Conduit_Cover_1080p.png")
    content = content.replace("05_rql_conduit_bonding_engine_1080p.png", "01_RQL_Conduit_Cover_1080p.png")

    # Update menu prices
    content = content.replace("$249</span>\n        </a>\n        <!-- Product 2: RQL Aegis -->", "$149</span>\n        </a>\n        <!-- Product 2: RQL Aegis -->")
    content = content.replace("$125</span>\n        </a>\n        <!-- Product 3: Veritas Dossier -->", "$199</span>\n        </a>\n        <!-- Product 3: Veritas Dossier -->")
    content = content.replace("$249</span>\n        </a>\n        <!-- Product 4: Industrial Fragility Sentinel -->", "$149</span>\n        </a>\n        <!-- Product 4: Industrial Fragility Sentinel -->")
    content = content.replace("$299</span>\n        </a>\n        <!-- Product 5: RQL Conduit Engine -->", "$179</span>\n        </a>\n        <!-- Product 5: RQL Conduit Engine -->")
    content = content.replace("$60</span>\n        </a>\n        <!-- Product 6: ExpressBill POS -->", "$59</span>\n        </a>\n        <!-- Product 6: ExpressBill POS -->")

    # Add Sovereign Suite to the nav dropdown if not already present
    if "SovereignSuiteMasterBundle" not in content and "<!-- Product 6: ExpressBill POS -->" in content:
        suite_item = """        <!-- Product 7: Sovereign Suite Master Bundle -->
        <a class="gumroad-button block py-2 px-3 rounded-lg bg-amber-50 text-amber-950 font-bold text-sm flex items-center justify-between" href="https://quantify17.gumroad.com/l/SovereignSuiteMasterBundle" data-gumroad-single-product="true">
            <div class="flex items-center gap-2">
                <i class="w-4 h-4 text-amber-600" data-lucide="crown"></i>
                <span>Sovereign Suite™ Master</span>
            </div>
            <span class="bg-amber-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">$499</span>
        </a>"""
        content = content.replace("<!-- Product 6: ExpressBill POS -->", suite_item + "\n        <!-- Product 6: ExpressBill POS -->")

    # Update ExpressBill direct download button in projects.html
    if "projects.html" in file_path.name:
        # Check if direct download button is in the actions bar
        old_actions = """<a href="https://quantify17.gumroad.com/l/ExpressBillPOS" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-400 hover:text-white px-2.5 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                            <span>Gumroad</span>
                        </a>"""
        new_actions = """<a href="/downloads/ExpressBill-Setup.exe" download class="text-xs font-bold text-white bg-slate-800 hover:bg-slate-700 px-3 py-2 rounded-xl border border-emerald-500/40 hover:border-emerald-400 transition flex items-center gap-1.5 shadow-sm">
                            <i data-lucide="download" class="w-3.5 h-3.5 text-emerald-400"></i>
                            <span>Download Setup (.EXE)</span>
                        </a>
                        <a href="https://quantify17.gumroad.com/l/ExpressBillPOS" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-400 hover:text-white px-2.5 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                            <span>Gumroad</span>
                        </a>"""
        if old_actions in content and "/downloads/ExpressBill-Setup.exe" not in content:
            content = content.replace(old_actions, new_actions)

    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Saved updates to: {file_path.name}")

def update_deployer_manifest():
    deployer_path = Path(r"C:\Users\rehan\Desktop\projects\website_builder\deploy_rehan_portfolio.py")
    code = deployer_path.read_text(encoding="utf-8")
    
    # Ensure new files are in files_to_pack
    new_files = [
        '"01_RQL_Conduit_Cover_1080p.png",',
        '"02_Deterministic_State_Kernel_Cover_1080p.png",',
        '"03_RQL_Aegis_Cover_1080p.png",',
        '"04_Veritas_Dossier_Cover_1080p.png",',
        '"05_Industrial_Sentinel_Cover_1080p.png",',
        '"06_ExpressBill_POS_Cover_1080p.png",',
        '"07_Sovereign_Suite_Master_Cover_1080p.png",',
        '"downloads/ExpressBill-Setup.exe",'
    ]
    
    for nf in new_files:
        if nf not in code:
            code = code.replace('"index.html",', f'{nf}\n        "index.html",')

    deployer_path.write_text(code, encoding="utf-8")
    print("✅ Updated deploy_rehan_portfolio.py manifest.")

def main():
    print("=" * 65)
    print("🌐 SYNCHRONIZING WEBSITE STOREFRONT WITH NEW GUMROAD URLS & DOWNLOADS")
    print("=" * 65)
    
    html_files = ["index.html", "projects.html", "aegis.html"]
    for f in html_files:
        fp = PORTFOLIO_DIR / f
        if fp.exists():
            update_file_links(fp)

    update_deployer_manifest()

    print("\n✨ Website files synchronized successfully!")

if __name__ == "__main__":
    main()
