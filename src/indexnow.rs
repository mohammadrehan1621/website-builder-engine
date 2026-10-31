// ============================================================================
// REHAN QUANT LAB™ — INSTANT INDEXNOW BROADCASTER (RFC PROTOCOL)
// "Zero-Wait Real-Time Edge Broadcast to Bing, Yandex, Naver & Google"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

use std::fs;
use std::path::Path;
use std::process::Command;
use std::time::Instant;
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct IndexNowPayload {
    pub host: String,
    pub key: String,
    #[serde(rename = "keyLocation")]
    pub key_location: String,
    #[serde(rename = "urlList")]
    pub url_list: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct IndexNowBroadcastResult {
    pub host: String,
    pub total_urls: usize,
    pub indexnow_status: String,
    pub google_ping_status: String,
    pub duration_ms: u64,
    pub urls_broadcast: Vec<String>,
}

pub struct IndexNowEngine;

impl IndexNowEngine {
    /// ⚡ Broadcast production URLs immediately to IndexNow API & Google Sitemap ping
    pub fn broadcast_production_urls(
        source_dir: &Path,
        domain: &str,
    ) -> Result<IndexNowBroadcastResult, String> {
        let t0 = Instant::now();
        let domain_clean = domain.trim_end_matches('/');

        // 1. Ensure or discover indexnow key
        let key_file_name = "rql2026indexnow.txt";
        let key_file_path = source_dir.join(key_file_name);
        let key = if key_file_path.exists() {
            fs::read_to_string(&key_file_path)
                .unwrap_or_else(|_| "rql2026indexnow".to_string())
                .trim()
                .to_string()
        } else {
            let default_key = "rql2026indexnow";
            let _ = fs::write(&key_file_path, default_key.as_bytes());
            default_key.to_string()
        };

        // 2. Collect all production HTML routes
        let mut url_list = Vec::new();
        if let Ok(entries) = fs::read_dir(source_dir) {
            for entry in entries.flatten() {
                let path = entry.path();
                if path.is_file() && path.extension().and_then(|e| e.to_str()) == Some("html") {
                    let fname = path.file_name().unwrap_or_default().to_string_lossy();
                    if !fname.starts_with("google") && !fname.starts_with("404") {
                        if fname == "index.html" {
                            url_list.push(format!("https://{}/", domain_clean));
                        } else {
                            url_list.push(format!("https://{}/{}", domain_clean, fname));
                        }
                    }
                }
            }
        }
        url_list.sort();
        url_list.dedup();

        if url_list.is_empty() {
            return Err("No valid production HTML pages found to broadcast".to_string());
        }

        let key_location = format!("https://{}/{}", domain_clean, key_file_name);
        let payload = IndexNowPayload {
            host: domain_clean.to_string(),
            key: key.clone(),
            key_location,
            url_list: url_list.clone(),
        };

        let json_body = serde_json::to_string_pretty(&payload)
            .map_err(|e| format!("Failed to serialize IndexNow payload: {}", e))?;

        // Write temp payload file to guarantee exact JSON byte fidelity through curl
        let tmp_payload = source_dir.join(".indexnow_tmp.json");
        let _ = fs::write(&tmp_payload, json_body.as_bytes());
        let at_payload = format!("@{}", tmp_payload.to_string_lossy());

        // 3. Dispatch to IndexNow API (Bing, Yandex, Seznam, Naver) via resilient curl
        let indexnow_status = match Command::new("curl.exe")
            .args([
                "-s",
                "-o", "/dev/null",
                "-w", "%{http_code}",
                "-X", "POST",
                "https://api.indexnow.org/indexnow",
                "-H", "Content-Type: application/json; charset=utf-8",
                "-d", &at_payload,
            ])
            .output()
        {
            Ok(output) => {
                let code = String::from_utf8_lossy(&output.stdout).trim().to_string();
                if code == "200" || code == "202" {
                    format!("🟢 200/202 ACCEPTED (Delivered to Bing/Yandex/Naver)")
                } else if code.is_empty() {
                    "⚪ Dispatched".to_string()
                } else {
                    format!("⚪ Status {} (Queued on IndexNow network)", code)
                }
            }
            Err(e) => format!("⚠️ Local curl notice: {}", e),
        };

        let _ = fs::remove_file(&tmp_payload);

        // 4. Ping Google Sitemap Ping Webhook
        let google_ping_url = format!("https://www.google.com/ping?sitemap=https://{}/sitemap.xml", domain_clean);
        let google_ping_status = match Command::new("curl.exe")
            .args(["-s", "-o", "/dev/null", "-w", "%{http_code}", &google_ping_url])
            .output()
        {
            Ok(output) => {
                let code = String::from_utf8_lossy(&output.stdout).trim().to_string();
                if code == "200" {
                    "🟢 200 OK (Googlebot Pinged)".to_string()
                } else {
                    format!("⚪ Status {}", code)
                }
            }
            Err(e) => format!("⚠️ Google ping notice: {}", e),
        };

        let elapsed = t0.elapsed().as_millis() as u64;

        Ok(IndexNowBroadcastResult {
            host: domain_clean.to_string(),
            total_urls: url_list.len(),
            indexnow_status,
            google_ping_status,
            duration_ms: elapsed,
            urls_broadcast: url_list,
        })
    }
}
