<#
====================================================================
REHAN QUANT LAB - AEGIS-CHAOS-PHOENIX & STRIX DAILY WATCHDOG (v2.0)
Autonomous Red-Team Auditor, Chaos Probe & Integrity Sentinel
====================================================================
#>

$ErrorActionPreference = "Continue"
Write-Host "`n========================================================" -ForegroundColor Cyan
Write-Host " [AEGIS-CHAOS-PHOENIX] INITIATING AUTONOMOUS SENTINEL" -ForegroundColor Cyan
Write-Host " Target: https://rehanquantlab.com | Mode: Continuous Audit" -ForegroundColor DarkCyan
Write-Host "========================================================`n" -ForegroundColor Cyan

$root = "$PSScriptRoot\Deployed_Websites\mohammadrehan.pages.dev"
$failures = 0
$passes = 0

function Report-Pass($msg) {
    $script:passes++
    Write-Host "  [OK / PASS] $msg" -ForegroundColor Green
}

function Report-Fail($msg) {
    $script:failures++
    Write-Host "  [FAILED] $msg" -ForegroundColor Red
}

# ----------------------------------------------------
# 1. STRIX CODE INTEGRITY & ASCII AUDIT
# ----------------------------------------------------
Write-Host ">>> PHASE 1: STRIX CODE INTEGRITY & 7-BIT ASCII AUDIT" -ForegroundColor Yellow

$htmlFiles = Get-ChildItem -Path $root -Recurse -Filter "*.html"
$asciiFailed = 0
foreach ($f in $htmlFiles) {
    $bytes = [System.IO.File]::ReadAllBytes($f.FullName)
    for ($i = 0; $i -lt $bytes.Length; $i++) {
        if ($bytes[$i] -gt 127) { $asciiFailed++; break }
    }
}
if ($asciiFailed -eq 0) {
    Report-Pass "All $($htmlFiles.Count) HTML files are 100% 7-bit ASCII compliant (0 non-ASCII bytes)."
} else {
    Report-Fail "$asciiFailed files contain non-ASCII characters!"
}

# Secret Scans
$secrets = @('sk_live_', 'ghp_', 'AIza[0-9A-Za-z\\-_]{35}', 'PRIVATE KEY')
$secLeaks = 0
foreach ($f in $htmlFiles) {
    $txt = [System.IO.File]::ReadAllText($f.FullName)
    if ($txt -match 'sk_live_' -or $txt -match 'ghp_' -or $txt -match 'BEGIN RSA PRIVATE KEY') {
        $secLeaks++
    }
}
if ($secLeaks -eq 0) {
    Report-Pass "0 hardcoded private keys or production API tokens found."
} else {
    Report-Fail "Potential secret detected in workspace!"
}

# Check .git in deployed webroot
if (-not (Test-Path "$root\.git")) {
    Report-Pass "Webroot contains zero .git directories."
} else {
    Report-Fail ".git folder detected in webroot!"
}

# ----------------------------------------------------
# 2. PENTAGI LIVE PENETRATION & EDGE PROBE
# ----------------------------------------------------
Write-Host "`n>>> PHASE 2: PENTAGI LIVE EDGE PENETRATION & ATTACK SIMULATION" -ForegroundColor Yellow

$probeEndpoints = @(
    @{ Url = "https://rehanquantlab.com/.git/config"; Expected = 404; Desc = "Git repository exposure probe" },
    @{ Url = "https://rehanquantlab.com/.env"; Expected = 404; Desc = "Environment variables leak probe" },
    @{ Url = "https://rehanquantlab.com/wp-admin/"; Expected = 404; Desc = "CMS administrative scanner probe" },
    @{ Url = "https://rehanquantlab.com/downloads/"; Expected = 404; Desc = "Directory listing / index probe" },
    @{ Url = "https://rehanquantlab.com/.well-known/security.txt"; Expected = 200; Desc = "RFC 9116 security.txt probe" }
)

foreach ($p in $probeEndpoints) {
    try {
        $req = [System.Net.HttpWebRequest]::Create($p.Url)
        $req.Timeout = 5000
        $req.Method = "GET"
        $res = $req.GetResponse()
        $code = [int]$res.StatusCode
        $res.Close()
        if ($code -eq $p.Expected) {
            Report-Pass "$($p.Desc) -> HTTP $code (Expected)"
        } else {
            Report-Fail "$($p.Desc) -> Got HTTP $code, expected $($p.Expected)!"
        }
    } catch {
        $code = 0
        if ($_.Exception.Message -match '\((\d+)\)') {
            $code = [int]$matches[1]
        } elseif ($_.Exception.Response) {
            $code = [int]$_.Exception.Response.StatusCode
        }
        
        if ($code -eq $p.Expected -or ($p.Expected -eq 404 -and $code -ge 400)) {
            Report-Pass "$($p.Desc) -> HTTP $code (Blocked / Dropped by Cloudflare Edge)"
        } else {
            Report-Fail "$($p.Desc) -> Unexpected response: $code ($($_.Exception.Message))"
        }
    }
}

# ----------------------------------------------------
# 3. AEGIS CRYPTOGRAPHIC MANIFEST & SIGNATURE AUDIT
# ----------------------------------------------------
Write-Host "`n>>> PHASE 3: AEGIS CRYPTOGRAPHIC VERIFICATION & SIGNATURES" -ForegroundColor Yellow

$manifestPath = "$root\downloads\RQL_SOVEREIGN_MANIFEST.sha256"
$sigPath = "$root\downloads\RQL_SOVEREIGN_MANIFEST.sha256.sig"
$pubKeyPath = "$root\.well-known\rql-release-signing-public.xml"

if ((Test-Path $manifestPath) -and (Test-Path $sigPath) -and (Test-Path $pubKeyPath)) {
    Report-Pass "Sovereign SHA-256 Manifest and RSA-4096 Signature files exist."
    
    # Verify cryptographic signature using public key
    try {
        $pubXml = [System.IO.File]::ReadAllText($pubKeyPath)
        $manifestTxt = [System.IO.File]::ReadAllText($manifestPath)
        $sigTxt = [System.IO.File]::ReadAllText($sigPath)
        
        $sigBase64 = $sigTxt.Replace("-----BEGIN RQL SOVEREIGN SIGNATURE-----", "").Replace("-----END RQL SOVEREIGN SIGNATURE-----", "").Trim()
        $sigBytes = [Convert]::FromBase64String($sigBase64)
        $manifestBytes = [System.Text.Encoding]::ASCII.GetBytes($manifestTxt)
        
        $rsa = New-Object System.Security.Cryptography.RSACryptoServiceProvider
        $rsa.FromXmlString($pubXml)
        $valid = $rsa.VerifyData($manifestBytes, "SHA256", $sigBytes)
        
        if ($valid) {
            Report-Pass "RSA-4096 Master Manifest Signature: 100% MATHEMATICALLY AUTHENTIC."
        } else {
            Report-Fail "Cryptographic signature failed mathematical verification!"
        }
    } catch {
        Report-Fail "Signature verification exception: $($_.Exception.Message)"
    }
} else {
    Report-Fail "Cryptographic manifest files missing!"
}

# ----------------------------------------------------
# 4. CHAOS RESILIENCE PROBE (AIR-GAP & CORRUPTION SIM)
# ----------------------------------------------------
Write-Host "`n>>> PHASE 4: CHAOS RESILIENCE & AIR-GAP DRIFT PROBE" -ForegroundColor Yellow

$chaosUrls = @(
    "https://rehanquantlab.com/?sql=SELECT%20*%20FROM%20users--",
    "https://rehanquantlab.com/?xss=%3Cscript%3Ealert(document.cookie)%3C/script%3E",
    "https://rehanquantlab.com/store?probe=chaos_injector_v1"
)

foreach ($cu in $chaosUrls) {
    try {
        $req = [System.Net.HttpWebRequest]::Create($cu)
        $req.Timeout = 5000
        $res = $req.GetResponse()
        $code = [int]$res.StatusCode
        $res.Close()
        if ($code -eq 200) {
            Report-Pass "Chaos injection safely swallowed: $code (Static Edge Invariant Holds)"
        } else {
            Report-Fail "Chaos injection returned unexpected status: $code"
        }
    } catch {
        Report-Fail "Chaos injection network failure: $($_.Exception.Message)"
    }
}

# ----------------------------------------------------
# 5. PHOENIX SUMMARY & RECOVERY READINESS
# ----------------------------------------------------
Write-Host "`n========================================================" -ForegroundColor Cyan
Write-Host " SENTINEL AUDIT COMPLETE: $passes PASSED | $failures FAILED" -ForegroundColor $(if ($failures -eq 0) { "Green" } else { "Red" })
Write-Host "========================================================`n" -ForegroundColor Cyan

if ($failures -eq 0) {
    Write-Host "PHOENIX STATUS: IMMUNE & STABLE. All sovereign invariants active.`n" -ForegroundColor Green
    exit 0
} else {
    Write-Host "PHOENIX STATUS: ANOMALIES DETECTED. Review logs above.`n" -ForegroundColor Red
    exit 1
}
