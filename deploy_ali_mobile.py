import os
import sys
import io
import zipfile
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

SITE_DIR = Path(r"C:\Users\rehan\Desktop\projects\ali_mobile_patna")
index_html = SITE_DIR / "index.html"

if not index_html.exists():
    print(f"Error: {index_html} not found.")
    sys.exit(1)

# Package entire directory recursively into zip bytes
buf = io.BytesIO()
with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, _, files in os.walk(SITE_DIR):
        for file in files:
            file_path = Path(root) / file
            # Relative arcname inside zip
            arcname = file_path.relative_to(SITE_DIR).as_posix()
            zf.write(file_path, arcname=arcname)
            print(f"  Added to bundle: {arcname} ({file_path.stat().st_size:,} bytes)")

zip_bytes = buf.getvalue()
print(f"Created complete site zip bundle: {len(zip_bytes):,} bytes")

print("🚀 Deploying Ali Mobile to Cloudflare Pages [project: ali-mobile-patna]...")
res = deploy_to_cloudflare_pages(zip_bytes, project_name="ali-mobile-patna")
print("Deployment response:", res)
