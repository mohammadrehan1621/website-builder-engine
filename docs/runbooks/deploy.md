# 🚀 Runbook: Production Edge Deployment & Verification
## Rehan Quant Lab (RQL) • Cloudflare Pages Global Edge Network

### 1. Scope & Objective
This runbook defines the mandatory, repeatable sequence for deploying static assets, security headers, and obfuscated routing logic from the local pure-Rust build pipeline to Cloudflare Pages edge network (`mohammadrehan.pages.dev` and `rehanquantlab.com`).

---

### 2. Pre-Deployment Verification Checklist
Before executing any deployment, the operator MUST run the local verification suite:

```powershell
cd C:\Users\rehan\Desktop\projects\website_builder

# Step 1: Run SEO Panopticon Audit (Must achieve 100/100 SSS+ Sovereign Apex)
cargo run --release --bin rql_website_builder -- seo

# Step 2: Run Pre-Launch Verifier (Zero non-ASCII mojibake, zero exposed .exe, all security headers present)
cargo run --release --bin verify_prelaunch_checklist
```

If either verification command fails or produces any warning, **HALT IMMEDIATELY**. Do not proceed to deployment.

---

### 3. Production Deployment Command
Execute deployment via `cmd.exe` to ensure proper execution of the Cloudflare Wrangler CLI wrapper:

```powershell
cd C:\Users\rehan\Desktop\projects\website_builder
cmd.exe /c "npx wrangler pages deploy Deployed_Websites/mohammadrehan.pages.dev --project-name mohammadrehan --branch main"
```

Verify that the terminal outputs:
```text
✨ Deployment complete! Take a peek over at https://<deployment-hash>.mohammadrehan.pages.dev
```

---

### 4. Post-Deployment Edge Header Verification
Perform live edge header and content audits against both edge domains:

```powershell
# 1. Inspect live security headers on primary apex domain
curl.exe -I https://rehanquantlab.com

# 2. Inspect live security headers on Cloudflare Pages edge
curl.exe -I https://mohammadrehan.pages.dev
```

Verify the presence and exact values of mandatory security headers:
- `Content-Security-Policy`: Must specify `default-src 'self' 'unsafe-inline' https:;` and prohibit external scripts.
- `Strict-Transport-Security`: Must be `max-age=31536000; includeSubDomains; preload`.
- `X-Content-Type-Options`: `nosniff`.
- `X-Frame-Options`: `DENY`.
- `Referrer-Policy`: `strict-origin-when-cross-origin`.
- `Permissions-Policy`: Camera, microphone, and geolocation all set to `()`.

---

### 5. Git Commit & Push Synchronization
Once edge verification confirms 200 OK and pristine headers:

```powershell
git status
git add .
git commit -m "feat/fix: <description of change>"
git push origin main
```
