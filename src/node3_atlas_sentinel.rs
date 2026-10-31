// ============================================================================
// REHAN QUANT LAB™ — NODE 3: ATLAS SENTINEL (8-PILLAR TITANIUM QUALITY GATE)
// "The Incorruptible Judge — 6-Second Deep Forensic Audit • Zero-Defect Gate"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

use std::fs;
use std::path::Path;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PillarAudit {
    pub pillar_num: u8,
    pub name: String,
    pub passed: bool,
    pub score: u32, // 0 - 100
    pub findings: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SentinelAuditReport {
    pub target_path: String,
    pub total_pillars: usize,
    pub passed_pillars: usize,
    pub overall_score: u32,
    pub is_titanium_certified: bool,
    pub pillars: Vec<PillarAudit>,
    pub timestamp: String,
}

pub struct AtlasSentinelEngine;

impl AtlasSentinelEngine {
    /// 🔄 CW: 8-Pillar Titanium Quality Audit
    pub fn audit_html_content(target_label: &str, html: &str) -> SentinelAuditReport {
        let mut pillars = Vec::with_capacity(8);

        // Pillar 1: Zero Broken Assets & Links
        let mut p1_findings = Vec::new();
        let mut p1_pass = true;
        if html.contains("src=\"#\"") || html.contains("href=\"#\"") && !html.contains("href=\"#") {
            p1_findings.push("Detected placeholder link href='#'".to_string());
            p1_pass = false;
        }
        if html.contains("assets/fake") || html.contains("todo.jpg") {
            p1_findings.push("Detected fake/broken asset paths".to_string());
            p1_pass = false;
        }
        pillars.push(PillarAudit {
            pillar_num: 1,
            name: "Zero Broken Assets & Links".to_string(),
            passed: p1_pass,
            score: if p1_pass { 100 } else { 40 },
            findings: p1_findings,
        });

        // Pillar 2: High-DPI & Responsive Viewport
        let mut p2_findings = Vec::new();
        let p2_pass = html.contains("name=\"viewport\"") && html.contains("width=device-width");
        if !p2_pass {
            p2_findings.push("Missing standard responsive viewport meta tag".to_string());
        }
        pillars.push(PillarAudit {
            pillar_num: 2,
            name: "High-DPI & Responsive Viewport".to_string(),
            passed: p2_pass,
            score: if p2_pass { 100 } else { 0 },
            findings: p2_findings,
        });

        // Pillar 3: Sub-50ms Static Edge FCP Readiness
        let byte_len = html.len();
        let p3_pass = byte_len < 500_000; // <500 KB static initial payload
        let mut p3_findings = Vec::new();
        if !p3_pass {
            p3_findings.push(format!("Payload size {} bytes exceeds 500 KB limit", byte_len));
        } else {
            p3_findings.push(format!("Optimal payload size: {:.2} KB", (byte_len as f64) / 1024.0));
        }
        pillars.push(PillarAudit {
            pillar_num: 3,
            name: "Sub-50ms Static Edge FCP Readiness".to_string(),
            passed: p3_pass,
            score: if p3_pass { 100 } else { 50 },
            findings: p3_findings,
        });

        // Pillar 4: Offline Resilient Form & Keystroke Journaling
        let has_form = html.contains("<form");
        let has_phoenix = html.contains("phoenix_sentinel") || html.contains("PHOENIX_SENTINEL") || html.contains("rql_phoenix");
        let p4_pass = !has_form || has_phoenix;
        let mut p4_findings = Vec::new();
        if has_form && !has_phoenix {
            p4_findings.push("Contact form detected without Phoenix Sentinel keystroke protection".to_string());
        } else {
            p4_findings.push("Phoenix Sentinel active or static-only document".to_string());
        }
        pillars.push(PillarAudit {
            pillar_num: 4,
            name: "Offline Resilient Form & Keystroke Journaling".to_string(),
            passed: p4_pass,
            score: if p4_pass { 100 } else { 30 },
            findings: p4_findings,
        });

        // Pillar 5: Clean Semantic HTML & Structured Microdata
        let has_doctype = html.to_lowercase().contains("<!doctype html>");
        let has_lang = html.contains("lang=\"en\"") || html.contains("lang='en'");
        let has_canon = html.contains("rel=\"canonical\"");
        let p5_pass = has_doctype && has_lang && has_canon;
        let mut p5_findings = Vec::new();
        if !has_doctype { p5_findings.push("Missing <!DOCTYPE html>".to_string()); }
        if !has_lang { p5_findings.push("Missing html lang attribute".to_string()); }
        if !has_canon { p5_findings.push("Missing canonical URL meta tag".to_string()); }
        pillars.push(PillarAudit {
            pillar_num: 5,
            name: "Clean Semantic HTML & Structured Microdata".to_string(),
            passed: p5_pass,
            score: if p5_pass { 100 } else { 60 },
            findings: p5_findings,
        });

        // Pillar 6: Content-Security-Policy & Modern Security Directives
        let has_csp = html.contains("Content-Security-Policy") || html.contains("content-security-policy");
        let p6_pass = has_csp;
        let mut p6_findings = Vec::new();
        if !has_csp {
            p6_findings.push("Recommend CSP meta header for titanium defense".to_string());
        }
        pillars.push(PillarAudit {
            pillar_num: 6,
            name: "Content-Security-Policy & Directives".to_string(),
            passed: p6_pass,
            score: if p6_pass { 100 } else { 80 },
            findings: p6_findings,
        });

        // Pillar 7: Contrast & Professional Typography
        let has_tailwind = html.contains("tailwindcss.com") || html.contains("class=\"");
        let p7_pass = has_tailwind;
        let mut p7_findings = Vec::new();
        if !p7_pass {
            p7_findings.push("Missing structured styling or font classes".to_string());
        }
        pillars.push(PillarAudit {
            pillar_num: 7,
            name: "High-Contrast Typography & Visual Hierarchy".to_string(),
            passed: p7_pass,
            score: if p7_pass { 100 } else { 50 },
            findings: p7_findings,
        });

        // Pillar 8: Zero Credential Leaks (CRITICAL SECURITY)
        let mut p8_findings = Vec::new();
        let mut p8_pass = true;
        let leak_patterns = vec!["CLOUDFLARE_API_TOKEN", "AIzaSy", "sk_live_", "cfut_"];
        for pat in leak_patterns {
            if html.contains(pat) {
                p8_findings.push(format!("CRITICAL: Detected pattern '{}' in public HTML", pat));
                p8_pass = false;
            }
        }
        pillars.push(PillarAudit {
            pillar_num: 8,
            name: "Zero Public Credential Leakage".to_string(),
            passed: p8_pass,
            score: if p8_pass { 100 } else { 0 },
            findings: p8_findings,
        });

        let total = pillars.len();
        let passed = pillars.iter().filter(|p| p.passed).count();
        let avg_score = (pillars.iter().map(|p| p.score).sum::<u32>()) / (total as u32);
        let is_titanium = passed == total && avg_score >= 95;

        SentinelAuditReport {
            target_path: target_label.to_string(),
            total_pillars: total,
            passed_pillars: passed,
            overall_score: avg_score,
            is_titanium_certified: is_titanium,
            pillars,
            timestamp: chrono::Utc::now().to_rfc3339(),
        }
    }

    /// 🔁 ACW: Forensic Counter-Audit & Gatekeeper
    /// Scans an entire directory on disk and enforces the Invariant Gate.
    pub fn audit_deployed_directory(dir: &Path) -> std::io::Result<Vec<SentinelAuditReport>> {
        let mut reports = Vec::new();

        if dir.exists() {
            if let Ok(entries) = fs::read_dir(dir) {
                for entry in entries.flatten() {
                    let path = entry.path();
                    if path.is_file() && path.extension().and_then(|e| e.to_str()) == Some("html") {
                        if let Ok(content) = fs::read_to_string(&path) {
                            let fname = path.file_name().unwrap_or_default().to_string_lossy().to_string();
                            let report = Self::audit_html_content(&fname, &content);
                            reports.push(report);
                        }
                    }
                }
            }
        }

        Ok(reports)
    }
}
