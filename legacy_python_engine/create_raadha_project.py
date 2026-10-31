import os
import sys
import requests
from dotenv import load_dotenv

sys.path.append(r"C:\Users\rehan\Desktop\projects\website_builder")
from hosting_deployer import resolve_cloudflare_credentials

acc_id, token = resolve_cloudflare_credentials()
print(f"Account: {acc_id}, Token: {token[:6]}...")

url = f"https://api.cloudflare.com/client/v4/accounts/{acc_id}/pages/projects"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

project_name = "raadha-rani-patna"
payload = {
    "name": project_name,
    "production_branch": "main"
}

r = requests.post(url, headers=headers, json=payload)
print("Create Project Status:", r.status_code)
print(r.json())
