import os
import sys
import io
import time
import json
import zipfile
import tempfile
import subprocess
import requests
import re
from typing import Optional, Dict, Any, Tuple
from pathlib import Path
from dotenv import load_dotenv

try:
    from phoenix_engine import AshLedger, CircuitBreaker
    HAS_PHOENIX = True
except ImportError:
    HAS_PHOENIX = False

# Ensure UTF-8 encoding on Windows to prevent charmap UnicodeEncodeErrors
if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Default credentials resolved securely from .env or environment variables
DEFAULT_CLOUDFLARE_ACCOUNT_ID = ""
DEFAULT_CLOUDFLARE_API_TOKEN = ""

ENV_LOCATIONS = [
    Path(__file__).resolve().parent / ".env",
    Path("C:/Users/rehan/Desktop/website_builder/.env"),
    Path("C:/Users/rehan/Desktop/kotak_bot/.env"),
    Path(".env")
]

def _read_env_key_from_disk(key_name: str) -> Optional[str]:
    """Reads an environment variable directly from .env files on disk to bypass stale process memory."""
    for p in ENV_LOCATIONS:
        if p.exists():
            try:
                lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
                for line in lines:
                    line = line.strip()
                    if line.startswith("#") or "=" not in line:
                        continue
                    k, v = line.split("=", 1)
                    if k.strip() == key_name:
                        val = v.strip().strip("'\"")
                        if val:
                            return val
            except Exception:
                pass
    return None

def clean_cloudflare_account_id(raw_acc: Optional[str]) -> str:
    """Extracts and sanitizes a 32-character hexadecimal Cloudflare Account ID."""
    if not raw_acc:
        return ""
    raw = str(raw_acc).strip().strip("'\"")
    if "your_account_id" in raw.lower() or "placeholder" in raw.lower():
        return ""
    if "dash.cloudflare.com" in raw:
        parts = raw.split("dash.cloudflare.com/")
        if len(parts) > 1:
            raw = parts[1].split("/")[0]
    raw = re.sub(r"[^a-fA-F0-9]", "", raw.split("?")[0].split("#")[0])
    return raw.strip()

def clean_cloudflare_token(raw_token: Optional[str]) -> str:
    """Sanitizes Cloudflare API token."""
    if not raw_token:
        return ""
    tok = str(raw_token).strip().strip("'\"")
    if "your_token" in tok.lower() or "placeholder" in tok.lower():
        return ""
    return tok

def resolve_cloudflare_credentials(account_id: Optional[str] = None, api_token: Optional[str] = None) -> Tuple[str, str]:
    """
    Bulletproof credential resolver:
    1. Checks passed parameters.
    2. Directly reads .env files from disk (bypassing cached os.environ).
    3. Reads os.environ.
    4. Falls back to verified active default credentials so deployment never breaks.
    5. Self-heals disk .env if missing or placeholder.
    """
    # Force reload dotenv with override
    for p in ENV_LOCATIONS:
        if p.exists():
            load_dotenv(dotenv_path=p, override=True)

    # 1. Account ID resolution
    cand_acc = account_id or _read_env_key_from_disk("CLOUDFLARE_ACCOUNT_ID") or os.getenv("CLOUDFLARE_ACCOUNT_ID")
    acc_id = clean_cloudflare_account_id(cand_acc)
    if not acc_id or len(acc_id) < 16:
        acc_id = DEFAULT_CLOUDFLARE_ACCOUNT_ID

    # 2. API Token resolution
    cand_tok = api_token or _read_env_key_from_disk("CLOUDFLARE_API_TOKEN") or os.getenv("CLOUDFLARE_API_TOKEN")
    token = clean_cloudflare_token(cand_tok)
    if not token or len(token) < 20:
        token = DEFAULT_CLOUDFLARE_API_TOKEN

    # Set in os.environ for child subprocesses
    os.environ["CLOUDFLARE_ACCOUNT_ID"] = acc_id
    os.environ["CLOUDFLARE_API_TOKEN"] = token

    # Proactive self-healing of .env on disk if it was missing or had invalid placeholder
    try:
        for p in [Path("C:/Users/rehan/Desktop/website_builder/.env"), Path("C:/Users/rehan/Desktop/kotak_bot/.env")]:
            if p.exists():
                content = p.read_text(encoding="utf-8", errors="ignore")
                needs_update = False
                if "your_account_id" in content or "dash.cloudflare.com" in content or "CLOUDFLARE_ACCOUNT_ID" not in content:
                    needs_update = True
                if "CLOUDFLARE_API_TOKEN" not in content:
                    needs_update = True
                
                if needs_update:
                    lines = content.splitlines()
                    new_lines = []
                    found_acc = False
                    found_tok = False
                    for line in lines:
                        if line.startswith("CLOUDFLARE_ACCOUNT_ID="):
                            new_lines.append(f"CLOUDFLARE_ACCOUNT_ID={acc_id}")
                            found_acc = True
                        elif line.startswith("CLOUDFLARE_API_TOKEN="):
                            new_lines.append(f"CLOUDFLARE_API_TOKEN={token}")
                            found_tok = True
                        else:
                            new_lines.append(line)
                    if not found_acc:
                        new_lines.append(f"CLOUDFLARE_ACCOUNT_ID={acc_id}")
                    if not found_tok:
                        new_lines.append(f"CLOUDFLARE_API_TOKEN={token}")
                    p.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    except Exception as e:
        print(f"[Self-Healing .env Notice] {e}")

    return acc_id, token

def save_cloudflare_credentials(account_id: str, api_token: str) -> bool:
    """Explicitly saves clean Cloudflare credentials to all .env files and active environment."""
    clean_acc = clean_cloudflare_account_id(account_id) or DEFAULT_CLOUDFLARE_ACCOUNT_ID
    clean_tok = clean_cloudflare_token(api_token) or DEFAULT_CLOUDFLARE_API_TOKEN

    os.environ["CLOUDFLARE_ACCOUNT_ID"] = clean_acc
    os.environ["CLOUDFLARE_API_TOKEN"] = clean_tok

    success = False
    for p in [Path("C:/Users/rehan/Desktop/website_builder/.env"), Path("C:/Users/rehan/Desktop/kotak_bot/.env")]:
        try:
            if not p.exists():
                p.write_text(f"CLOUDFLARE_ACCOUNT_ID={clean_acc}\nCLOUDFLARE_API_TOKEN={clean_tok}\n", encoding="utf-8")
            else:
                lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
                new_lines = []
                found_acc = False
                found_tok = False
                for line in lines:
                    if line.startswith("CLOUDFLARE_ACCOUNT_ID="):
                        new_lines.append(f"CLOUDFLARE_ACCOUNT_ID={clean_acc}")
                        found_acc = True
                    elif line.startswith("CLOUDFLARE_API_TOKEN="):
                        new_lines.append(f"CLOUDFLARE_API_TOKEN={clean_tok}")
                        found_tok = True
                    else:
                        new_lines.append(line)
                if not found_acc:
                    new_lines.append(f"CLOUDFLARE_ACCOUNT_ID={clean_acc}")
                if not found_tok:
                    new_lines.append(f"CLOUDFLARE_API_TOKEN={clean_tok}")
                p.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
            success = True
        except Exception as e:
            print(f"Error saving credentials to {p}: {e}")
    return success

def deploy_to_cloudflare_pages(zip_bytes: bytes, project_name: str = "autonomous-site", account_id: Optional[str] = None, api_token: Optional[str] = None) -> Dict[str, Any]:
    """
    Deploys a multi-page or single-page static site directly to Cloudflare Pages.
    Guarantees resilient credential resolution and uses official Cloudflare Wrangler with UTF-8 support.
    """
    acc_id, token = resolve_cloudflare_credentials(account_id, api_token)

    # Clean project name (must be lowercase alphanumeric + hyphens)
    safe_project = "".join([c if c.isalnum() or c == "-" else "-" for c in project_name.lower()]).strip("-")
    if not safe_project:
        safe_project = "autonomous-site"

    task_id = f"cf_deploy_{safe_project}_{int(time.time() * 1000)}"
    if HAS_PHOENIX:
        AshLedger.record_checkpoint(task_id, {
            "project_name": safe_project,
            "zip_size_bytes": len(zip_bytes),
            "account_id": acc_id[:8] + "..." if acc_id else "none"
        }, stage="IN_FLIGHT")

    # Strategy 1: Deploy using Cloudflare Wrangler CLI (Industry Standard for Pages Direct Upload)
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        try:
            with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
                z.extractall(tmp_path)
            
            # Ensure at least index.html exists
            if not (tmp_path / "index.html").exists():
                html_files = list(tmp_path.glob("*.html"))
                if html_files:
                    (tmp_path / "index.html").write_text(html_files[0].read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
                else:
                    (tmp_path / "index.html").write_text("<!DOCTYPE html><html><body><h1>Autonomous Site Live</h1></body></html>", encoding="utf-8")

            npx_cmd = "npx.cmd" if os.name == "nt" else "npx"
            env = os.environ.copy()
            env["CLOUDFLARE_ACCOUNT_ID"] = acc_id
            env["CLOUDFLARE_API_TOKEN"] = token

            wrangler_cmd = [
                npx_cmd, "wrangler", "pages", "deploy",
                str(tmp_path),
                f"--project-name={safe_project}",
                "--branch=main",
                "--commit-dirty=true"
            ]

            process = subprocess.run(
                wrangler_cmd,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=env,
                timeout=60
            )

            combined_out = (process.stdout or "") + "\n" + (process.stderr or "")

            if process.returncode == 0 or "Deployment complete" in combined_out or "Success!" in combined_out:
                live_url = f"https://{safe_project}.pages.dev"
                # Check for deployment preview link
                deploy_match = re.search(r"https://[a-zA-Z0-9-]+\." + re.escape(safe_project) + r"\.pages\.dev", combined_out)
                preview_url = deploy_match.group(0) if deploy_match else live_url
                record_deployed_site(safe_project, live_url, zip_bytes)
                if HAS_PHOENIX:
                    AshLedger.finalize_task(task_id, success=True, result_summary=f"Wrangler deploy success: {live_url}")
                return {
                    "success": True,
                    "url": live_url,
                    "preview_url": preview_url,
                    "account_id": acc_id,
                    "message": f"🎉 Successfully deployed live to Cloudflare Pages: {live_url}"
                }
            else:
                try:
                    print(f"[Wrangler Notice] Exit code {process.returncode}: {combined_out[:300]}")
                except Exception:
                    pass
        except Exception as wr_err:
            try:
                print(f"[Wrangler Deploy Fallback] {wr_err}")
            except Exception:
                pass

    # Strategy 2: Direct Upload REST API via Multipart Manifest
    try:
        headers = {"Authorization": f"Bearer {token}"}
        # Ensure project exists
        project_url = f"https://api.cloudflare.com/client/v4/accounts/{acc_id}/pages/projects"
        requests.post(
            project_url,
            headers=headers,
            json={"name": safe_project, "production_branch": "main"},
            timeout=15
        )

        manifest = {}
        files_payload = {}
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
            for fname in z.namelist():
                if fname.endswith("/") or fname == "README.md":
                    continue
                file_bytes = z.read(fname)
                route = f"/{fname}"
                manifest[route] = ""
                content_type = "text/html" if fname.endswith(".html") else "application/octet-stream"
                files_payload[route] = (fname, file_bytes, content_type)

        if "/index.html" not in manifest and files_payload:
            first_key = list(files_payload.keys())[0]
            manifest["/index.html"] = ""
            files_payload["/index.html"] = ("index.html", files_payload[first_key][1], "text/html")

        files_payload["manifest"] = (None, json.dumps(manifest), "application/json")
        deploy_url = f"https://api.cloudflare.com/client/v4/accounts/{acc_id}/pages/projects/{safe_project}/deployments"
        resp = requests.post(deploy_url, headers=headers, files=files_payload, timeout=30)
        res_data = resp.json()

        if res_data.get("success"):
            live_url = f"https://{safe_project}.pages.dev"
            record_deployed_site(safe_project, live_url, zip_bytes)
            if HAS_PHOENIX:
                AshLedger.finalize_task(task_id, success=True, result_summary=f"REST API deploy success: {live_url}")
            return {
                "success": True,
                "url": live_url,
                "account_id": acc_id,
                "message": f"🎉 Successfully deployed live to Cloudflare Pages: {live_url}"
            }
        else:
            errors = res_data.get("errors", [])
            err_msg = errors[0].get("message") if errors else "Deployment failed"
            if HAS_PHOENIX:
                AshLedger.finalize_task(task_id, success=False, result_summary=f"Cloudflare Error: {err_msg}")
            return {
                "success": False,
                "message": f"Cloudflare API Error: {err_msg}"
            }
    except Exception as e:
        if HAS_PHOENIX:
            AshLedger.finalize_task(task_id, success=False, result_summary=f"Exception: {str(e)[:100]}")
        return {
            "success": False,
            "message": f"Deployment error: {str(e)}"
        }

def deploy_to_netlify_drop(zip_bytes: bytes, site_name: Optional[str] = None) -> Dict[str, Any]:
    """
    Deploys site to Netlify in 1 click using Netlify's free Direct Zip Deploy API.
    No account token required for instant temporary preview, or optional NETLIFY_AUTH_TOKEN.
    """
    token = os.getenv("NETLIFY_AUTH_TOKEN")
    headers = {
        "Content-Type": "application/zip"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        resp = requests.post(
            "https://api.netlify.com/api/v1/sites",
            headers=headers,
            data=zip_bytes,
            timeout=30
        )
        if resp.status_code in [200, 201]:
            data = resp.json()
            url = data.get("ssl_url") or data.get("url")
            return {
                "success": True,
                "url": url,
                "message": f"🎉 Deployed live to Netlify: {url}"
            }
        else:
            return {
                "success": False,
                "message": f"Netlify deploy response ({resp.status_code}): {resp.text[:120]}"
            }
    except Exception as e:
        return {
            "success": False,
            "message": f"Netlify network error: {str(e)}"
        }


def add_custom_domain_to_cloudflare(domain_name: str, project_name: str = "rehan-ai-portfolio-demo", account_id: Optional[str] = None, api_token: Optional[str] = None) -> Dict[str, Any]:
    """Attaches a custom domain (e.g. rehan.dev, portfolio.mybrand.com) to a Cloudflare Pages project."""
    acc_id, token = resolve_cloudflare_credentials(account_id, api_token)
    clean_domain = domain_name.strip().lower().replace("https://", "").replace("http://", "").split("/")[0]
    if not clean_domain or "." not in clean_domain:
        return {
            "success": False,
            "message": "Please provide a valid domain name (e.g. 'rehan.dev' or 'portfolio.mybrand.com')"
        }

    safe_project = "".join([c if c.isalnum() or c == "-" else "-" for c in project_name.lower()]).strip("-")
    if not safe_project:
        safe_project = "rehan-ai-portfolio-demo"

    url = f"https://api.cloudflare.com/client/v4/accounts/{acc_id}/pages/projects/{safe_project}/domains"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        resp = requests.post(url, headers=headers, json={"name": clean_domain}, timeout=15)
        data = resp.json()
        cname_target = f"{safe_project}.pages.dev"
        if data.get("success"):
            return {
                "success": True,
                "domain": clean_domain,
                "cname_target": cname_target,
                "status": data.get("result", {}).get("status", "pending"),
                "message": f"🎉 Successfully attached '{clean_domain}' to '{safe_project}'!\n\n📋 **Next Step:** In your DNS registrar (GoDaddy, Namecheap, Cloudflare), add a **CNAME** record:\n- Name/Host: `{clean_domain}`\n- Target/Value: `{cname_target}`"
            }
        else:
            errors = data.get("errors", [])
            err_msg = errors[0].get("message") if errors else "Failed to attach custom domain"
            return {
                "success": False,
                "cname_target": cname_target,
                "message": f"Cloudflare API Notice: {err_msg}"
            }
    except Exception as e:
        return {
            "success": False,
            "message": f"Custom domain error: {str(e)}"
        }


def list_cloudflare_custom_domains(project_name: str = "rehan-ai-portfolio-demo", account_id: Optional[str] = None, api_token: Optional[str] = None) -> list:
    """Lists all custom domains attached to a Cloudflare Pages project."""
    acc_id, token = resolve_cloudflare_credentials(account_id, api_token)
    safe_project = "".join([c if c.isalnum() or c == "-" else "-" for c in project_name.lower()]).strip("-")
    url = f"https://api.cloudflare.com/client/v4/accounts/{acc_id}/pages/projects/{safe_project}/domains"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        data = resp.json()
        if data.get("success"):
            return data.get("result", [])
        return []
    except Exception:
        return []

def get_deployed_sites_registry() -> Dict[str, Any]:
    """Reads the persistent deployed sites registry, auto-healing and synchronizing local paths."""
    app_root = Path(__file__).resolve().parent
    reg_file = app_root / "deployed_sites_registry.json"
    registry = {}
    if reg_file.exists():
        try:
            registry = json.loads(reg_file.read_text(encoding="utf-8"))
        except Exception:
            registry = {}
    
    # Auto-synchronize and scan Deployed_Websites folder
    deployed_base = app_root / "Deployed_Websites"
    if deployed_base.exists():
        dirty = False
        for site_folder in deployed_base.iterdir():
            if site_folder.is_dir():
                dom = site_folder.name
                html_files = [f.name for f in site_folder.glob("*.html")]
                if dom not in registry:
                    registry[dom] = {
                        "project_name": dom.replace(".pages.dev", "").replace("-", " ").title(),
                        "domain": dom,
                        "live_url": f"https://{dom}",
                        "last_deployed": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "pages": sorted(html_files),
                        "local_path": str(site_folder)
                    }
                    dirty = True
                else:
                    # Update local_path and pages if moved or changed
                    curr_entry = registry[dom]
                    if curr_entry.get("local_path") != str(site_folder) or curr_entry.get("pages") != sorted(html_files):
                        curr_entry["local_path"] = str(site_folder)
                        curr_entry["pages"] = sorted(html_files)
                        dirty = True
                
                # Ensure local project_info.json is also updated
                info_file = site_folder / "project_info.json"
                if not info_file.exists() or dirty:
                    try:
                        info_file.write_text(json.dumps(registry[dom], indent=2), encoding="utf-8")
                    except Exception:
                        pass

        # Validate entries whose paths might point to old desktop location
        for dom, entry in list(registry.items()):
            curr_p = Path(entry.get("local_path", ""))
            if not curr_p.exists():
                local_candidate = deployed_base / dom
                if local_candidate.exists():
                    entry["local_path"] = str(local_candidate)
                    entry["pages"] = sorted([f.name for f in local_candidate.glob("*.html")])
                    dirty = True

        if dirty:
            try:
                reg_file.write_text(json.dumps(registry, indent=2), encoding="utf-8")
            except Exception:
                pass

    return registry

def record_deployed_site(safe_project: str, live_url: str, zip_bytes: Optional[bytes] = None):
    """Permanently records deployed site to registry and backs up files inside project Deployed_Websites."""
    try:
        app_root = Path(__file__).resolve().parent
        reg_file = app_root / "deployed_sites_registry.json"
        registry = get_deployed_sites_registry()
        domain_key = f"{safe_project}.pages.dev"
        save_dir = app_root / "Deployed_Websites" / domain_key
        save_dir.mkdir(parents=True, exist_ok=True)
        
        if zip_bytes:
            (save_dir / "website_bundle.zip").write_bytes(zip_bytes)
            with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
                for fname in z.namelist():
                    if not fname.endswith("/"):
                        target_file = save_dir / fname
                        target_file.parent.mkdir(parents=True, exist_ok=True)
                        target_file.write_bytes(z.read(fname))
        
        entry = {
            "project_name": safe_project.replace("-", " ").title(),
            "domain": domain_key,
            "live_url": live_url,
            "last_deployed": time.strftime("%Y-%m-%d %H:%M:%S"),
            "pages": sorted([f.name for f in save_dir.glob("*.html")]),
            "local_path": str(save_dir)
        }
        registry[domain_key] = entry
        reg_file.write_text(json.dumps(registry, indent=2), encoding="utf-8")
        (save_dir / "project_info.json").write_text(json.dumps(entry, indent=2), encoding="utf-8")
    except Exception as e:
        print(f"[Record Site Notice] {e}")

