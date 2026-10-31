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

ROOT_DIR = Path(r"C:\Users\rehan\Desktop\projects\raadha_rani_patna")
DIST_DIR = ROOT_DIR / "dist"
PROJECT_NAME = "raadha-rani-patna"
DOMAIN_NAME = f"{PROJECT_NAME}.pages.dev"
MIRROR_DIR = Path(rf"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\{DOMAIN_NAME}")

print("\n" + "═" * 70)
print("👑 BUILDING & DEPLOYING RAADHA RANI (REACT + VITE + RUST WASM)")
print(f"   Project: {PROJECT_NAME} | Domain: {DOMAIN_NAME}")
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

# Copy _headers to dist if exists
if (ROOT_DIR / "public" / "_headers").exists():
    shutil.copy2(ROOT_DIR / "public" / "_headers", DIST_DIR / "_headers")
    print("✅ Copied public/_headers to dist/_headers")

# 2. Mirror dist to Deployed_Websites
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
res = deploy_to_cloudflare_pages(zip_bytes, project_name=PROJECT_NAME)
print("Deployment response:", res)

# 5. Live Edge Verification
target_url = res.get("url") or f"https://{DOMAIN_NAME}"
print(f"\n🌐 Performing Live Edge Health Check on {target_url} ...")
try:
    r = requests.get(target_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=12)
    print(f"   Status Code: {r.status_code}")
    print(f"   Has React Root: {'<div id=\"root\"></div>' in r.text}")
    print(f"   Has Compiled Asset: {'assets/index-' in r.text}")
    if r.status_code == 200:
        print(f"🎉 Raadha Rani is 100% LIVE and healthy on Cloudflare Pages: {target_url}!")
except Exception as e:
    print("   Edge check notice:", e)
