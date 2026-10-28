import os
import sys
import io
import time
import json
import shutil
import zipfile
import subprocess
import requests
from pathlib import Path

# Configure Windows UTF-8 stdout
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from hosting_deployer import deploy_to_cloudflare_pages, resolve_cloudflare_credentials

BASE_DIR = Path(__file__).resolve().parent
SRC_REPO_DIR = Path(r"C:\Users\rehan\Desktop\Rehan_Quant_Lab\Website_RehanQuantLab")
PORTFOLIO_DIR = BASE_DIR / "Deployed_Websites" / "mohammadrehan.pages.dev"
REGISTRY_FILE = BASE_DIR / "deployed_sites_registry.json"


def sync_from_source_repo():
    """Syncs modified files from primary git repo to deployment staging directory."""
    if not SRC_REPO_DIR.exists():
        return
    print(f"🔄 Syncing latest assets and code from {SRC_REPO_DIR.name}...")
    for item in SRC_REPO_DIR.iterdir():
        if item.name.startswith(".git"):
            continue
        dest = PORTFOLIO_DIR / item.name
        if item.is_file():
            shutil.copy2(item, dest)
        elif item.is_dir():
            shutil.copytree(item, dest, dirs_exist_ok=True)
    print("✅ Staging directory synchronized with source repository.")

def deploy_portfolio():
    print("\n" + "═" * 70)
    print("🚀 DEPLOYING UPGRADED PORTFOLIO TO CLOUDFLARE PAGES")
    print("   Project: Mohammadrehan | Domain: rehanquantlab.com (mohammadrehan.pages.dev)")
    print("═" * 70)

    if not PORTFOLIO_DIR.exists():
        print(f"Error: {PORTFOLIO_DIR} not found.")
        return False

    # 1. Sync source repository files
    sync_from_source_repo()

    # 2. Run Autonomous SEO Compiler (dynamic sitemap, robots.txt, schema injection)
    seo_compiler_path = BASE_DIR / "auto_seo_compiler.py"
    if seo_compiler_path.exists():
        try:
            print("\n🤖 Running Inbuilt Autonomous SEO Compiler...")
            subprocess.run([sys.executable, str(seo_compiler_path)], check=True)
            print("✅ SEO compilation finished successfully.")
        except Exception as e:
            print(f"⚠️ SEO compilation notice: {e}")

    # Package files into zip bytes
    buf = io.BytesIO()
    files_to_pack = [
        "01_RQL_Conduit_Cover_1080p.png",
        "02_Deterministic_State_Kernel_Cover_1080p.png",
        "03_RQL_Aegis_Cover_1080p.png",
        "04_Veritas_Dossier_Cover_1080p.png",
        "05_Industrial_Sentinel_Cover_1080p.png",
        "06_ExpressBill_POS_Cover_1080p.png",
        "07_Sovereign_Suite_Master_Cover_1080p.png",
        "08_RQL_TagMaster_Cover_1080p.png",
        "09_RQL_DeskBroadcast_Cover_1080p.png",
        "10_RQL_TaxMatrix_Cover_1080p.png",
        "11_RQL_LocalMesh_Cover_1080p.png",
        "12_RQL_StoreFlow_Cover_1080p.png",
        "14_RQL_LedgerGuard_Cover_1080p.png",
        "15_RQL_StockAudit_Cover_1080p.png",
        "16_RQL_OmniDispatch_Cover_1080p.png",
        "17_RQL_Nexus_Cover_1080p.png",
        "18_RQL_DocumentShield_Cover_1080p.png",
        "18_RQL_DocumentShield_Square_Thumbnail.png",
        "Bundle_01_RQL_Retail_Master_Cover_1080p.png",
        "Bundle_02_RQL_CA_Tax_Master_Cover_1080p.png",
        "Bundle_03_RQL_Quant_Core_Master_Cover_1080p.png",
        "favicon.svg",
        "icons.svg",
        "downloads/ExpressBill-Setup.exe",
        "downloads/RQL_StoreFlow_Workstation_Brochure.pdf",
        "downloads/RQL_LedgerGuard_CA_Reconciler_Brochure.pdf",
        "downloads/StoreFlow_Workstation_Brochure.pdf",
        "downloads/LedgerGuard_CA_Reconciler_Brochure.pdf",
        "index.html",
        "store.html",
        "aegis.html",
        "projects.html",
        "experience.html",
        "contact.html",
        "legal.html",
        "Mohammad_Rehan_Resume.pdf",
        "RQL-Aegis-v1.0-Release.zip",
        "emblem.jpg",
        "logo.jpg",
        "emblem.webp",
        "logo.webp",
        "05_rql_conduit_bonding_engine_1080p.png",
        "05_rql_conduit_bonding_engine_1080p.webp",
        "ExpressBill_POS_Commercial_Hero.jpg",
        "ExpressBill_POS_Commercial_Hero.webp",
        "linkedin_banner.png",
        "og_preview.png",
        "phoenix_sentinel.js",
        "rql_seo_engine.js",
        "lively_motion.js",
        "react_live_engine.js",
        "_headers",
        "public/_headers",
        "react_portal.html",
        "rql_wasm.js",
        "rql_wasm_engine.wasm",
        "robots.txt",
        "sitemap.xml",
        "googlecb5b21d2c61033d5.html",
        "expressbill/index.html",
        "expressbill/manifest.json",
        "expressbill/sw.js"
    ]

    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for fname in files_to_pack:
            fpath = PORTFOLIO_DIR / fname
            if fpath.exists():
                zf.write(fpath, arcname=fname)
                print(f"  • Packed: {fname:25} ({fpath.stat().st_size:,} bytes)")
            else:
                print(f"  ⚠️ Warning: {fname} missing.")
        assets_dir = PORTFOLIO_DIR / "assets"
        if assets_dir.exists():
            for afile in assets_dir.rglob("*"):
                if afile.is_file():
                    arc = afile.relative_to(PORTFOLIO_DIR).as_posix()
                    zf.write(afile, arcname=arc)
                    print(f"  • Packed Asset: {arc:25} ({afile.stat().st_size:,} bytes)")

        media_dir = PORTFOLIO_DIR / "media"
        if media_dir.exists():
            for mfile in media_dir.rglob("*"):
                if mfile.is_file():
                    arc = mfile.relative_to(PORTFOLIO_DIR).as_posix()
                    zf.write(mfile, arcname=arc)
                    print(f"  • Packed Media: {arc:25} ({mfile.stat().st_size:,} bytes)")

    zip_bytes = buf.getvalue()
    zip_path = PORTFOLIO_DIR / "website_bundle.zip"
    zip_path.write_bytes(zip_bytes)
    print(f"\n📦 Bundle created: {zip_path.name} ({len(zip_bytes):,} bytes)")

    # Execute Cloudflare Deploy
    print("\n⚡ Triggering Cloudflare Pages Deploy Engine (Wrangler)...")
    res = deploy_to_cloudflare_pages(
        zip_bytes=zip_bytes,
        project_name="Mohammadrehan"
    )

    print(f"\nDeployment Result: Success = {res.get('success')}")
    print(f"Live URL: {res.get('url')}")
    if res.get("error"):
        print(f"Details / Log: {res.get('error')[:300]}")

    # Update Registry
    try:
        registry = {}
        if REGISTRY_FILE.exists():
            registry = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
        
        registry["rehanquantlab.com"] = {
            "project_name": "Mohammadrehan",
            "domain": "rehanquantlab.com",
            "live_url": "https://rehanquantlab.com",
            "fallback_url": "https://mohammadrehan.pages.dev",
            "last_deployed": time.strftime("%Y-%m-%d %H:%M:%S"),
            "pages": files_to_pack,
            "local_path": str(PORTFOLIO_DIR),
            "status": "LIVE_TITANIUM"
        }
        REGISTRY_FILE.write_text(json.dumps(registry, indent=2), encoding="utf-8")
        print("✅ Registry updated with live deployment metadata.")
    except Exception as e:
        print(f"Registry notice: {e}")

    # Verify live HTTP response on custom domain and pages.dev
    time.sleep(2)
    for target_url in ["https://rehanquantlab.com", "https://rehanquantlab.com/store.html", "https://rehanquantlab.com/sitemap.xml", "https://mohammadrehan.pages.dev"]:
        try:
            r = requests.get(target_url, timeout=10)
            has_phoenix = "phoenix_sentinel.js" in r.text
            has_infra_bar = "live-ticker-container" in r.text.lower() or "production infrastructure" in r.text.lower()
            print("\n" + "─" * 70)
            print(f"🌐 Live Edge Health Check [{target_url}]: Status {r.status_code} ({len(r.text):,} bytes)")
            print(f"   • Phoenix Sentinel Script Wired: {'🟢 YES' if has_phoenix else '🔴 NO'}")
            print(f"   • Infrastructure Status Bar Live: {'🟢 YES' if has_infra_bar else '🔴 NO'}")
            print("─" * 70)
        except Exception as e:
            print(f"Edge check warning [{target_url}]: {e}")

    return res.get("success", False)

if __name__ == "__main__":
    deploy_portfolio()