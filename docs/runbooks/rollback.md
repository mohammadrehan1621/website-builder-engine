# ↩️ Runbook: Instant Rollback Procedure
## Rehan Quant Lab (RQL) • Cloudflare Pages Edge Rollback

### 1. Scope & Objective
In the event of an edge anomaly, content regression, unexpected rendering defect, or header misconfiguration discovered post-deployment, this runbook outlines the zero-downtime, sub-30-second rollback procedure.

---

### 2. Instant Edge Rollback via Wrangler CLI
Cloudflare Pages retains an immutable cryptographic record of every historic deployment hash. You can roll back instantly without waiting for a re-compilation or git revert.

#### Option A: Rollback via Cloudflare Dashboard
1. Open Cloudflare Dashboard: **Workers & Pages** -> **mohammadrehan**.
2. Navigate to the **Deployments** tab.
3. Locate the last known good deployment (e.g., `e3b46976`).
4. Click the three dots `...` next to the deployment and select **Rollback to this deployment**.
5. Confirm rollback. The edge routes traffic to the target build globally in under 5 seconds.

#### Option B: Fast Re-deploy of Previous Git Commit
If CLI rollback is preferred:
```powershell
cd C:\Users\rehan\Desktop\projects\website_builder

# Checkout previous known healthy commit
git log --oneline -n 5
git checkout <previous-commit-hash> -- Deployed_Websites/mohammadrehan.pages.dev

# Deploy previous static build immediately
cmd.exe /c "npx wrangler pages deploy Deployed_Websites/mohammadrehan.pages.dev --project-name mohammadrehan --branch main"

# Restore git working tree
git checkout HEAD -- Deployed_Websites/mohammadrehan.pages.dev
```

---

### 3. Post-Rollback Verification
Verify that the apex domain and edge domain are serving the restored state:
```powershell
curl.exe -I https://rehanquantlab.com
curl.exe -s https://rehanquantlab.com | Select-String "Rehan Quant Lab"
```

Verify that all critical links, obfuscation scripts, and legal codex sections match expected baseline.
