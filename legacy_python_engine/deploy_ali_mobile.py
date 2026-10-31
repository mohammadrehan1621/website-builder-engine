import os
import sys
import subprocess
from pathlib import Path

sys.path.append(r"C:\Users\rehan\Desktop\projects\website_builder")
from hosting_deployer import resolve_cloudflare_credentials

acc_id, token = resolve_cloudflare_credentials()
dist_dir = r"C:\Users\rehan\Desktop\projects\ali_mobile_patna\dist"

env = os.environ.copy()
env["CLOUDFLARE_ACCOUNT_ID"] = acc_id
env["CLOUDFLARE_API_TOKEN"] = token

cmd = [
    "npx.cmd", "wrangler", "pages", "deploy",
    dist_dir,
    "--project-name=ali-mobile-patna",
    "--branch=main",
    "--commit-dirty=true"
]

print("Running cmd:", " ".join(cmd))
res = subprocess.run(cmd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
print("Return code:", res.returncode)
safe_stdout = res.stdout.encode("ascii", "replace").decode()
safe_stderr = res.stderr.encode("ascii", "replace").decode()
print("STDOUT:\n", safe_stdout)
if safe_stderr:
    print("STDERR:\n", safe_stderr)
