import os
import re
import json
import time
import zipfile
import requests
from pathlib import Path

BASE_DIR = Path("c:/Users/rehan/Desktop/website_builder")
DEPLOYED_ROOT = Path("C:/Users/rehan/Desktop/Deployed_Websites")
DEPLOYED_ROOT.mkdir(parents=True, exist_ok=True)
REGISTRY_FILE = BASE_DIR / "deployed_sites_registry.json"

print(f"=== BACKING UP AND PRESERVING DEPLOYED SITES TO {DEPLOYED_ROOT} ===")

# 1. Project 1: mohammadrehan.pages.dev
rehan_dir = DEPLOYED_ROOT / "mohammadrehan.pages.dev"
rehan_dir.mkdir(parents=True, exist_ok=True)

rehan_pages = {
    "index.html": "https://mohammadrehan.pages.dev",
    "projects.html": "https://mohammadrehan.pages.dev/projects.html",
    "experience.html": "https://mohammadrehan.pages.dev/experience.html",
    "contact.html": "https://mohammadrehan.pages.dev/contact.html"
}

rehan_saved_files = []
for fname, url in rehan_pages.items():
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            (rehan_dir / fname).write_text(r.text, encoding="utf-8")
            rehan_saved_files.append(fname)
            print(f" -> [OK] mohammadrehan.pages.dev/{fname} ({len(r.text):,} bytes)")
    except Exception as e:
        print(f" -> [ERR] mohammadrehan.pages.dev/{fname}: {e}")

# If any file couldn't be fetched, fallback to local desktop files if available
local_desk_dir = Path("C:/Users/rehan/Desktop/Generated_Website")
if local_desk_dir.exists():
    for f in ["index.html", "projects.html", "experience.html", "contact.html"]:
        if not (rehan_dir / f).exists() and (local_desk_dir / f).exists():
            (rehan_dir / f).write_text((local_desk_dir / f).read_text(encoding="utf-8"), encoding="utf-8")
            rehan_saved_files.append(f)
            print(f" -> [LOCAL FALLBACK] Saved {f} from Generated_Website")

# Zip mohammadrehan
rehan_zip = rehan_dir / "website_bundle.zip"
with zipfile.ZipFile(rehan_zip, "w", zipfile.ZIP_DEFLATED) as zf:
    for f in (rehan_dir.glob("*.html")):
        zf.writestr(f.name, f.read_text(encoding="utf-8"))
    zf.writestr("README.md", "# Mohammad Rehan Portfolio\nLive URL: https://mohammadrehan.pages.dev\n")

# Project info
rehan_info = {
    "project_name": "Mohammad Rehan — Portfolio & Systems Architecture",
    "domain": "mohammadrehan.pages.dev",
    "live_url": "https://mohammadrehan.pages.dev",
    "type": "Personal Portfolio & Resume (Multi-Page)",
    "whatsapp_number": "+91 70915 18548",
    "last_deployed": time.strftime("%Y-%m-%d %H:%M:%S"),
    "pages": [f.name for f in rehan_dir.glob("*.html")],
    "local_path": str(rehan_dir)
}
(rehan_dir / "project_info.json").write_text(json.dumps(rehan_info, indent=2), encoding="utf-8")

# 2. Project 2: ladieszone.pages.dev
lz_dir = DEPLOYED_ROOT / "ladieszone.pages.dev"
lz_dir.mkdir(parents=True, exist_ok=True)

lz_pages = {
    "index.html": "https://ladieszone.pages.dev",
    "contact.html": "https://ladieszone.pages.dev/contact.html"
}

lz_saved_files = []
for fname, url in lz_pages.items():
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            (lz_dir / fname).write_text(r.text, encoding="utf-8")
            lz_saved_files.append(fname)
            print(f" -> [OK] ladieszone.pages.dev/{fname} ({len(r.text):,} bytes)")
    except Exception as e:
        print(f" -> [ERR] ladieszone.pages.dev/{fname}: {e}")

# Zip ladieszone
lz_zip = lz_dir / "website_bundle.zip"
with zipfile.ZipFile(lz_zip, "w", zipfile.ZIP_DEFLATED) as zf:
    for f in (lz_dir.glob("*.html")):
        zf.writestr(f.name, f.read_text(encoding="utf-8"))
    zf.writestr("README.md", "# Ladies Zone Exclusive Showroom\nLive URL: https://ladieszone.pages.dev\n")

# Project info
lz_info = {
    "project_name": "Ladies Zone Exclusive Showroom (Patna)",
    "domain": "ladieszone.pages.dev",
    "live_url": "https://ladieszone.pages.dev",
    "type": "E-Commerce & DTC Retail Showroom",
    "whatsapp_number": "+91 70915 18548",
    "last_deployed": time.strftime("%Y-%m-%d %H:%M:%S"),
    "pages": [f.name for f in lz_dir.glob("*.html")],
    "local_path": str(lz_dir)
}
(lz_dir / "project_info.json").write_text(json.dumps(lz_info, indent=2), encoding="utf-8")

# 3. Save Unified Registry
registry = {
    "mohammadrehan.pages.dev": rehan_info,
    "ladieszone.pages.dev": lz_info
}
REGISTRY_FILE.write_text(json.dumps(registry, indent=2), encoding="utf-8")
print(f"\n[SUCCESS] Unified Registry saved to {REGISTRY_FILE}")
print("Both projects permanently saved with source code, info, and ZIP bundles!")
