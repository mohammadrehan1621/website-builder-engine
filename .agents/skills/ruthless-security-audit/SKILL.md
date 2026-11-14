---
name: ruthless-security-audit
description: Autonomous defensive security sentinel, static code integrity verification (Strix), edge penetration attack simulation (PentAGI), and AST vulnerability detection (Bug Hunter). Enforces zero secret leaks, 100% 7-bit ASCII compliance, DOM XSS immunity, and RSA-4096 cryptographic manifest signing.
---

# Ruthless Security & Leak Audit (Strix, PentAGI & Bug Hunter)

## Overview
This skill implements the **sovereign defensive security doctrine** for the website builder and Rehan Quant Lab ecosystem. It operates as an uncompromising, autonomous gatekeeper that runs before any production deployment to eliminate secret leaks, supply-chain tampering, injection vectors, and infrastructure drift.

---

## 1. The 4-Phase Defensive Architecture

```
+---------------------------------------------------------------------------------------+
|                       RUTHLESS DEFENSIVE SECURITY AUDIT SUITE                         |
+---------------------------------------------------------------------------------------+
|  [PHASE 1: STRIX]         • Zero private keys or production API tokens                |
|                           • 100% 7-bit ASCII compliance (0 non-ASCII bytes)           |
|                           • Webroot contains zero .git or .env directories            |
+---------------------------------------------------------------------------------------+
|  [PHASE 2: PENTAGI]       • Edge Git exposure probe -> HTTP 404 (Blocked)             |
|                           • Environment variables probe -> HTTP 404 (Blocked)         |
|                           • CMS scanner / traversal probe -> HTTP 404 (Blocked)       |
|                           • RFC 9116 security.txt probe -> HTTP 200 (Expected)        |
+---------------------------------------------------------------------------------------+
|  [PHASE 3: BUG HUNTER]    • AST inspection of DOM sinks (innerHTML, eval, write)      |
|                           • Open redirect neutralization via strict slug whitelist    |
|                           • CSP header enforcement (upgrade-insecure-requests)        |
+---------------------------------------------------------------------------------------+
|  [PHASE 4: AEGIS ENGINE]  • SHA-256 cryptographic manifest digest verification        |
|                           • RSA-4096 mathematical signature authenticity proof        |
|                           • Chaos injection & air-gap drift immunity validation       |
+---------------------------------------------------------------------------------------+
```

---

## 2. Phase 1: Strix Code Integrity & Leak Scanner

### 2.1 Secret & Key Leak Detection
Scan all source files for high-entropy secrets and credential signatures:
- **Private Keys**: `-----BEGIN (RSA|EC|PGP|OPENSSH) PRIVATE KEY-----`
- **Cloud Tokens**: AWS (`AKIA[0-9A-Z]{16}`), GitHub (`gh[pousr]_[0-9a-zA-Z]{36}`), Stripe (`sk_live_[0-9a-zA-Z]{24}`)
- **Local Absolute Paths**: Prevents leaking local host directory hierarchies (`C:\Users\...`).

### 2.2 7-Bit Strict ASCII Enforcement
- Every byte in every HTML and client JavaScript file must have a decimal value `<= 127`.
- Zero raw UTF-8 Unicode glyphs permitted in markup; all symbols must use standard HTML entities:
  - `&trade;` for ™
  - `&#8377;` for ₹
  - `&bull;` for •
  - `&rarr;` for →
  - `&ndash;` / `&mdash;` for dashes

### 2.3 Webroot Directory Quarantine
- The deployed directory (`Deployed_Websites/mohammadrehan.pages.dev/`) must never contain:
  - `.git` or `.github` folders.
  - `.env` or configuration secrets.
  - Temporary `.swp`, `.bak`, or `flight_recorder` files.

---

## 3. Phase 2: PentAGI Live Edge Penetration Simulation

Automated penetration probes simulate real-world adversarial reconnaissance:
```powershell
# Probe 1: Git repository exposure
curl -I "https://rehanquantlab.com/.git/HEAD" -> Expect HTTP 404

# Probe 2: Environment variables exposure
curl -I "https://rehanquantlab.com/.env" -> Expect HTTP 404

# Probe 3: Administrative endpoint probe
curl -I "https://rehanquantlab.com/wp-login.php" -> Expect HTTP 404

# Probe 4: Security disclosure manifest
curl -I "https://rehanquantlab.com/.well-known/security.txt" -> Expect HTTP 200
```

---

## 4. Phase 3: Claude Bug Hunter (DOM & Router Security)

### 4.1 DOM XSS Sink Immunity
- Ban direct assignment of `location.search`, `window.location.hash`, or unescaped query parameters into `.innerHTML`.
- Force text-based assignments using `.textContent` or verified sanitization functions.

### 4.2 Anycast Edge Redirect Whitelisting (`functions/go.js`)
All redirect slugs must be resolved strictly through an immutable in-memory map:
```javascript
const slugMap = {
  'store': 'https://rehanquantlab.com/store',
  'documentshield': 'https://quantify17.gumroad.com/l/rql-documentshield',
  'archivemaster': 'https://quantify17.gumroad.com/l/rql-archivemaster'
};
// Fallback to safe canonical domain; never redirect to arbitrary user-supplied URLs
let destination = slugMap[slug] || 'https://rehanquantlab.com/store';
```

---

## 5. Phase 4: Aegis Cryptographic Signatures

### 5.1 SHA-256 Manifest Digest
Every binary release (`.exe`, `.zip`) has its exact SHA-256 hash published in `security.html` and verified against the master hash manifest.

### 5.2 RSA-4096 Verification
The master manifest is digitally signed using an RSA-4096 private key stored in an air-gapped physical vault. The public certificate independently verifies mathematically that 0% supply-chain modification occurred.

---

## 6. Execution Command
Run the automated sentinel check locally before every commit and deployment:
```powershell
powershell.exe -ExecutionPolicy Bypass -File aegis_watchdog.ps1
```
*Required Outcome*: `SENTINEL AUDIT COMPLETE: 13 PASSED | 0 FAILED`.
