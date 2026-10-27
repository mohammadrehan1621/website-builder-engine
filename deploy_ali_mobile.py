import os
import sys
import io
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

sys.path.append(r"C:\Users\rehan\Desktop\projects\website_builder")
from hosting_deployer import deploy_to_cloudflare_pages

ROOT_DIR = Path(r"C:\Users\rehan\Desktop\projects\ali_mobile_patna")
DIST_DIR = ROOT_DIR / "dist"
MIRROR_DIR = Path(r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\ali-mobile-patna.pages.dev")

print("\n" + "═" * 70)
print("🚀 BUILDING & DEPLOYING ALI MOBILE (REACT + VITE + RUST WASM)")
print("   Project: ali-mobile-patna | Domain: ali-mobile-patna.pages.dev")
print("═" * 70)

# 1. Run Vite build
print("⚡ Running Vite build...")
build_cmd = ["npm.cmd", "run", "build"]
proc = subprocess.run(build_cmd, cwd=ROOT_DIR, capture_output=True, text=True)
if proc.returncode != 0:
    print("❌ Build failed!")
    print(proc.stderr)
    sys.exit(1)
print(proc.stdout)

if not (DIST_DIR / "index.html").exists():
    print(f"Error: {DIST_DIR / 'index.html'} not found.")
    sys.exit(1)

# 2. Mirror dist to Deployed_Websites/ali-mobile-patna.pages.dev
MIRROR_DIR.mkdir(parents=True, exist_ok=True)
for item in DIST_DIR.iterdir():
    dest = MIRROR_DIR / item.name
    if item.is_dir():
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(item, dest)
    else:
        shutil.copy2(item, dest)
print(f"✅ Mirrored dist/ to {MIRROR_DIR}")

# 3. Package dist into zip bundle
buf = io.BytesIO()
with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, _, files in os.walk(DIST_DIR):
        for file in files:
            file_path = Path(root) / file
            arcname = file_path.relative_to(DIST_DIR).as_posix()
            zf.write(file_path, arcname=arcname)
            print(f"  • Packed: {arcname:35} ({file_path.stat().st_size:,} bytes)")

zip_bytes = buf.getvalue()
print(f"\n📦 Bundle created: {len(zip_bytes):,} bytes")

# 4. Deploy to Cloudflare Pages
print("⚡ Triggering Cloudflare Pages Deploy Engine...")
res = deploy_to_cloudflare_pages(zip_bytes, project_name="ali-mobile-patna")
print("Deployment response:", res)

# 5. Live Edge Verification
print("\n🌐 Performing Live Edge Health Check on https://ali-mobile-patna.pages.dev ...")
try:
    r = requests.get("https://ali-mobile-patna.pages.dev", headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    print(f"   Status Code: {r.status_code}")
    print(f"   Has React Root: {'<div id=\"root\"></div>' in r.text}")
    print(f"   Has Compiled Asset: {'assets/index-' in r.text}")
    if r.status_code == 200:
        print("🎉 Ali Mobile is 100% LIVE and healthy on Cloudflare Pages!")
except Exception as e:
    print("   Edge check error:", e)
