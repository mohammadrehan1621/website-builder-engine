// ============================================================================
// REHAN QUANT LAB™ — NODE 5: CLOUDFLARE EDGE DEPLOY ENGINE & LIVE PROBER
// "The Physical Hands — Sub-Second Edge Dispatcher & Reverse Live Prober"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

use std::collections::HashMap;
use std::fs;
use std::path::{Path, PathBuf};
use std::process::Command;
use std::time::Instant;
use chrono::Utc;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CloudflareCredentials {
    pub account_id: String,
    pub api_token: String,
    pub is_valid: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LiveProbeResult {
    pub url: String,
    pub status_code: u16,
    pub response_bytes: usize,
    pub latency_ms: u64,
    pub has_phoenix_sentinel: bool,
    pub has_infrastructure_bar: bool,
    pub is_healthy: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SiteRegistryEntry {
    pub project_name: String,
    pub domain: String,
    pub live_url: String,
    #[serde(default)]
    pub fallback_url: Option<String>,
    pub last_deployed: String,
    pub pages: Vec<String>,
    pub local_path: String,
    #[serde(default)]
    pub status: Option<String>,
}

pub struct DeployEngine;

impl DeployEngine {
    /// Resolves Cloudflare credentials from .env or OS environment
    pub fn resolve_credentials() -> CloudflareCredentials {
        let env_paths = [
            PathBuf::from(".env"),
            PathBuf::from("C:/Users/rehan/Desktop/projects/website_builder/.env"),
            PathBuf::from("C:/Users/rehan/Desktop/website_builder/.env"),
        ];

        let mut acc_id = std::env::var("CLOUDFLARE_ACCOUNT_ID").unwrap_or_default();
        let mut token = std::env::var("CLOUDFLARE_API_TOKEN").unwrap_or_default();

        for p in &env_paths {
            if p.exists() {
                if let Ok(content) = fs::read_to_string(p) {
                    for line in content.lines() {
                        let line = line.strip_prefix('#').unwrap_or(line).trim();
                        if line.starts_with("CLOUDFLARE_ACCOUNT_ID=") {
                            let val = line.trim_start_matches("CLOUDFLARE_ACCOUNT_ID=").trim().trim_matches('"').trim_matches('\'');
                            if !val.is_empty() && acc_id.is_empty() {
                                acc_id = val.to_string();
                            }
                        } else if line.starts_with("CLOUDFLARE_API_TOKEN=") {
                            let val = line.trim_start_matches("CLOUDFLARE_API_TOKEN=").trim().trim_matches('"').trim_matches('\'');
                            if !val.is_empty() && token.is_empty() {
                                token = val.to_string();
                            }
                        }
                    }
                }
            }
        }

        let is_valid = !acc_id.is_empty() && !token.is_empty() && acc_id.len() >= 16 && token.len() >= 20;
        CloudflareCredentials {
            account_id: acc_id,
            api_token: token,
            is_valid,
        }
    }

    /// 🔄 CW: Edge Deployment via Wrangler
    pub fn deploy_site(
        project_name: &str,
        source_dir: &Path,
        custom_domain: Option<&str>,
    ) -> std::io::Result<(bool, String)> {
        let creds = Self::resolve_credentials();
        if !creds.is_valid {
            return Ok((false, "Cloudflare credentials not found or invalid in .env".to_string()));
        }

        let npx = if cfg!(windows) { "npx.cmd" } else { "npx" };
        let mut cmd = Command::new(npx);
        cmd.args([
            "wrangler",
            "pages",
            "deploy",
            &source_dir.to_string_lossy(),
            &format!("--project-name={}", project_name),
            "--branch=main",
            "--commit-dirty=true",
        ]);

        cmd.env("CLOUDFLARE_ACCOUNT_ID", &creds.account_id);
        cmd.env("CLOUDFLARE_API_TOKEN", &creds.api_token);

        println!("   \x1b[1;36m⚡ Dispatching to Cloudflare Pages edge: {}\x1b[0m", project_name);
        let mut output = cmd.output()?;

        let mut stdout = String::from_utf8_lossy(&output.stdout).to_string();
        let mut stderr = String::from_utf8_lossy(&output.stderr).to_string();
        let mut success = output.status.success() || stdout.contains("Success") || stdout.contains("Deployment complete");

        // Auto-provision Pages project if it does not exist yet
        if !success && (stdout.contains("does not exist") || stderr.contains("does not exist")) {
            println!("   \x1b[1;33m⚠️ Pages project '{}' does not exist yet. Auto-provisioning on Cloudflare Edge...\x1b[0m", project_name);
            let mut create_cmd = Command::new(npx);
            create_cmd.args([
                "wrangler",
                "pages",
                "project",
                "create",
                project_name,
                "--production-branch=main",
            ]);
            create_cmd.env("CLOUDFLARE_ACCOUNT_ID", &creds.account_id);
            create_cmd.env("CLOUDFLARE_API_TOKEN", &creds.api_token);
            let create_res = create_cmd.output();
            if let Ok(c_out) = create_res {
                let c_stdout = String::from_utf8_lossy(&c_out.stdout);
                if c_stdout.contains("Successfully created") || c_out.status.success() {
                    println!("   \x1b[1;32m✓ Pages project '{}' auto-provisioned! Retrying deployment...\x1b[0m", project_name);
                    let mut retry_cmd = Command::new(npx);
                    retry_cmd.args([
                        "wrangler",
                        "pages",
                        "deploy",
                        &source_dir.to_string_lossy(),
                        &format!("--project-name={}", project_name),
                        "--branch=main",
                        "--commit-dirty=true",
                    ]);
                    retry_cmd.env("CLOUDFLARE_ACCOUNT_ID", &creds.account_id);
                    retry_cmd.env("CLOUDFLARE_API_TOKEN", &creds.api_token);
                    if let Ok(r_out) = retry_cmd.output() {
                        output = r_out;
                        stdout = String::from_utf8_lossy(&output.stdout).to_string();
                        stderr = String::from_utf8_lossy(&output.stderr).to_string();
                        success = output.status.success() || stdout.contains("Success") || stdout.contains("Deployment complete");
                    }
                }
            }
        }

        let log = format!("{}\n{}", stdout, stderr);

        // Update Registry
        if success {
            let _ = Self::update_registry(project_name, source_dir, custom_domain);
        }

        Ok((success, log))
    }

    /// Updates deployed_sites_registry.json
    pub fn update_registry(
        project_name: &str,
        source_dir: &Path,
        custom_domain: Option<&str>,
    ) -> std::io::Result<()> {
        let registry_path = Path::new("deployed_sites_registry.json");
        let mut registry: HashMap<String, SiteRegistryEntry> = if registry_path.exists() {
            let content = fs::read_to_string(registry_path)?;
            serde_json::from_str(&content).unwrap_or_default()
        } else {
            HashMap::new()
        };

        let domain = match custom_domain {
            Some(d) => d.to_string(),
            None => {
                if project_name.ends_with(".pages.dev") {
                    project_name.to_string()
                } else {
                    format!("{}.pages.dev", project_name)
                }
            }
        };
        let live_url = format!("https://{}", domain);

        let mut pages = Vec::new();
        if let Ok(entries) = fs::read_dir(source_dir) {
            for entry in entries.flatten() {
                if let Ok(meta) = entry.metadata() {
                    if meta.is_file() {
                        pages.push(entry.file_name().to_string_lossy().to_string());
                    }
                }
            }
        }
        pages.sort();

        let entry = SiteRegistryEntry {
            project_name: project_name.to_string(),
            domain: domain.to_string(),
            live_url: live_url.clone(),
            fallback_url: Some(format!("https://{}.pages.dev", project_name.to_lowercase())),
            last_deployed: Utc::now().format("%Y-%m-%d %H:%M:%S").to_string(),
            pages,
            local_path: source_dir.to_string_lossy().to_string(),
            status: Some("LIVE_TITANIUM".to_string()),
        };

        registry.insert(domain.to_string(), entry);
        let updated_json = serde_json::to_string_pretty(&registry)?;
        fs::write(registry_path, updated_json)?;
        Ok(())
    }

    /// 🔁 ACW: Reverse Live Edge Prober
    /// Uses native curl / powershell web requests to verify live HTTP 200, Phoenix Sentinel wiring, and latency.
    pub fn probe_live_endpoint(url: &str) -> LiveProbeResult {
        let t0 = Instant::now();

        // Use curl on Windows/Linux for zero-dependency native HTTP probe
        let curl_output = Command::new("curl")
            .args(["-s", "-L", "-i", "--max-time", "8", url])
            .output();

        let latency = t0.elapsed().as_millis() as u64;

        if let Ok(out) = curl_output {
            let res_str = String::from_utf8_lossy(&out.stdout).to_string();
            let is_200 = res_str.contains("HTTP/1.1 200") || res_str.contains("HTTP/2 200") || res_str.contains("200 OK");
            let has_phoenix = res_str.contains("phoenix_sentinel") || res_str.contains("PHOENIX") || res_str.contains("rql_phoenix");
            let has_infra = res_str.contains("infrastructure") || res_str.contains("Infrastructure") || res_str.contains("INFRASTRUCTURE");

            LiveProbeResult {
                url: url.to_string(),
                status_code: if is_200 { 200 } else { 500 },
                response_bytes: res_str.len(),
                latency_ms: latency,
                has_phoenix_sentinel: has_phoenix,
                has_infrastructure_bar: has_infra,
                is_healthy: is_200,
            }
        } else {
            LiveProbeResult {
                url: url.to_string(),
                status_code: 0,
                response_bytes: 0,
                latency_ms: latency,
                has_phoenix_sentinel: false,
                has_infrastructure_bar: false,
                is_healthy: false,
            }
        }
    }

    /// 📊 Real-Time Prospective Client Speed & CMS Auditor (100% Pure Native Rust)
    pub fn audit_prospective_client(raw_url: &str, client_name: &str, company_name: &str) -> Option<ClientAuditReport> {
        let url = if !raw_url.starts_with("http://") && !raw_url.starts_with("https://") {
            format!("https://{}", raw_url)
        } else {
            raw_url.to_string()
        };

        let t0 = Instant::now();
        let curl_output = Command::new("curl")
            .args(["-s", "-L", "-i", "--max-time", "12", &url])
            .output();

        let latency = t0.elapsed().as_millis() as u64;

        if let Ok(out) = curl_output {
            let res_str = String::from_utf8_lossy(&out.stdout).to_string();
            let is_200 = res_str.contains("HTTP/1.1 200") || res_str.contains("HTTP/2 200") || res_str.contains("200 OK");
            if !is_200 {
                // Reject dead domains, unresolvable DNS, or 404/500 errors
                return None;
            }
            let status_code = 200;

            let mut platforms = Vec::new();
            let lower = res_str.to_lowercase();
            if lower.contains("wp-content") || lower.contains("wp-includes") {
                platforms.push("WordPress (PHP)");
            }
            if lower.contains("elementor") {
                platforms.push("Elementor Page Builder");
            }
            if lower.contains("woocommerce") {
                platforms.push("WooCommerce");
            }
            if lower.contains("wix.com") || lower.contains("_wix") {
                platforms.push("Wix.com");
            }
            if lower.contains("shopify") {
                platforms.push("Shopify");
            }
            if platforms.is_empty() {
                platforms.push("Custom / Legacy Server");
            }

            let platform_str = platforms.join(", ");
            let page_size_kb = (res_str.len() as f64) / 1024.0;
            let rql_baseline_ms = 208.0;
            let slowdown = (latency as f64) / rql_baseline_ms;

            let clean_domain = url.replace("https://", "").replace("http://", "").trim_matches('/').to_string();
            let pitch = format!(
"Hi {}, hope business at {} is going great.\n\n\
I was doing an engineering performance audit on local business websites today and ran a test on {}:\n\n\
• Current site load time: {:.2} seconds ({})\n\
• Modern high-speed standard: 0.20 seconds (100/100 Google Lighthouse score)\n\n\
Google recently began penalizing local business websites that take over 2.5 seconds on mobile search.\n\n\
Since we are both alumni from our BNI chapter, I can rebuild your site on our zero-cloud pure-native engine. It will load in under 250 milliseconds with 100/100 Google SEO, and eliminate your annual hosting bills completely.\n\n\
Would you be open to seeing a 60-second live speed demo on my phone this week over a cup of tea?",
                client_name, company_name, clean_domain, (latency as f64) / 1000.0, platform_str
            );

            Some(ClientAuditReport {
                url,
                status_code,
                latency_ms: latency,
                detected_platform: platform_str,
                page_size_kb,
                slowdown_factor: slowdown,
                whatsapp_pitch: pitch,
            })
        } else {
            None
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ClientAuditReport {
    pub url: String,
    pub status_code: u16,
    pub latency_ms: u64,
    pub detected_platform: String,
    pub page_size_kb: f64,
    pub slowdown_factor: f64,
    pub whatsapp_pitch: String,
}
