import os
import sys
import io
import time
import json
import zipfile
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
PORTFOLIO_DIR = BASE_DIR / "Deployed_Websites" / "mohammadrehan.pages.dev"
REGISTRY_FILE = BASE_DIR / "deployed_sites_registry.json"

def deploy_portfolio():
    print("\n" + "═" * 70)
    print("🚀 DEPLOYING UPGRADED PORTFOLIO TO CLOUDFLARE PAGES")
    print("   Project: Mohammadrehan | Domain: rehanquantlab.com (mohammadrehan.pages.dev)")
    print("═" * 70)

    if not PORTFOLIO_DIR.exists():
        print(f"Error: {PORTFOLIO_DIR} not found.")
        return False

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
        "downloads/ExpressBill-Setup.exe",
        "index.html",
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
        "aria_neural_engine.js",
        "lively_motion.js",
        "_headers",
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
    for target_url in ["https://rehanquantlab.com", "https://mohammadrehan.pages.dev"]:
        try:
            r = requests.get(target_url, timeout=10)
            has_phoenix = "phoenix_sentinel.js" in r.text
            has_infra_bar = "production infrastructure" in r.text.lower()
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
