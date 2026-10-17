import sys
import zipfile
from pathlib import Path

sys.path.append(r"c:\Users\rehan\Desktop\website_builder")
from hosting_deployer import deploy_to_cloudflare_pages, record_deployed_site

portfolio_dir = Path(r"c:\Users\rehan\Desktop\website_builder\Deployed_Websites\mohammadrehan.pages.dev")
zip_path = portfolio_dir / "website_bundle.zip"

with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for f in portfolio_dir.rglob("*"):
        if f.is_file() and not f.name.endswith(".zip"):
            rel = f.relative_to(portfolio_dir).as_posix()
            z.write(f, arcname=rel)

with open(zip_path, "rb") as f:
    zip_bytes = f.read()

print("Deploying portfolio with Mathematical Shield to Cloudflare Pages...")
res = deploy_to_cloudflare_pages(zip_bytes, project_name="mohammadrehan")
print("Deployment Result:", res)

if res.get("success"):
    record_deployed_site("mohammadrehan", res.get("url", "https://mohammadrehan.pages.dev"), zip_bytes)
    print("Portfolio deployment recorded successfully!")
