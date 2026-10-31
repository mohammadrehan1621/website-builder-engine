import os
import sys
import requests

sys.path.append(r"C:\Users\rehan\Desktop\projects\website_builder")
from hosting_deployer import resolve_cloudflare_credentials

acc_id, token = resolve_cloudflare_credentials()
url = f"https://api.cloudflare.com/client/v4/accounts/{acc_id}/pages/projects"
headers = {"Authorization": f"Bearer {token}"}
r = requests.get(url, headers=headers)
projects = [p["name"] for p in r.json().get("result", [])]
print("Projects in this account:", projects)
