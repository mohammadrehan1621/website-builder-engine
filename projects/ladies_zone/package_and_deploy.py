import os
import sys
import zipfile
import shutil
from pathlib import Path

sys.path.append(r"C:\Users\rehan\Desktop\website_builder")
from hosting_deployer import deploy_to_cloudflare_pages, record_deployed_site

SRC_DIR = Path(r"C:\Users\rehan\Desktop\website_builder\projects\ladies_zone")
DEPLOY_LOCAL_DIR = Path(r"C:\Users\rehan\Desktop\website_builder\Deployed_Websites\ladieszone.pages.dev")
FASHION_SHOP_ZIP = Path(r"C:\Users\rehan\Downloads\Programs\fashion-shop\ladies-zone-cloudflare-pages.zip")

DEPLOY_LOCAL_DIR.mkdir(parents=True, exist_ok=True)
(DEPLOY_LOCAL_DIR / "assets").mkdir(parents=True, exist_ok=True)

# Copy files to local deployment directory
files_to_copy = ["index.html", "robots.txt", "sitemap.xml", "_headers", "_redirects"]
for fname in files_to_copy:
    src_f = SRC_DIR / fname
    if src_f.exists():
        shutil.copy2(src_f, DEPLOY_LOCAL_DIR / fname)

# Copy assets
logo_src = SRC_DIR / "assets" / "logo.png"
if logo_src.exists():
    shutil.copy2(logo_src, DEPLOY_LOCAL_DIR / "assets" / "logo.png")

# Create POSIX-compliant zip in memory and on disk
def make_posix_zip(src_dir, out_zip_path):
    with zipfile.ZipFile(out_zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for f in src_dir.rglob("*"):
            if f.is_file() and not f.name.endswith(".zip") and not f.name.endswith(".py") and "__pycache__" not in str(f):
                rel = f.relative_to(src_dir).as_posix()
                z.write(f, arcname=rel)

# 1. Write zip to fashion-shop folder
make_posix_zip(DEPLOY_LOCAL_DIR, FASHION_SHOP_ZIP)
print(f"Created {FASHION_SHOP_ZIP} (Size: {FASHION_SHOP_ZIP.stat().st_size} bytes)")

# 2. Write zip to Deployed_Websites folder
local_zip = DEPLOY_LOCAL_DIR / "website_bundle.zip"
make_posix_zip(DEPLOY_LOCAL_DIR, local_zip)

# 3. Read zip bytes for direct Cloudflare API deployment
with open(local_zip, "rb") as f:
    zip_bytes = f.read()

print("Deploying fresh build directly to Cloudflare Pages project 'ladieszone'...")
res = deploy_to_cloudflare_pages(zip_bytes, project_name="ladieszone")
print("Cloudflare Deployment Result:", res)

if res.get("success"):
    record_deployed_site("ladieszone", res.get("url", "https://ladieszone.pages.dev"), zip_bytes)
    print("Deployment recorded successfully to registry!")
