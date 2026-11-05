// ============================================================================
// REHAN QUANT LAB™ — OPEN-SEO PANOPTICON ENGINE (100% PURE NATIVE RUST)
// "Zero Python • Microsecond Byte-Slice Matrix • SERP Viewport Invariant"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

use std::collections::HashMap;
use std::fs;
use std::path::Path;
use std::time::Instant;
use chrono::Utc;
use serde::{Deserialize, Serialize};

/// High-Intent Commercial Keyword Vectors for RQL Ecosystem
pub const KEYWORD_VECTORS: &[&str] = &[
    "offline billing",
    "zero monthly fee",
    "lifetime license",
    "air-gapped",
    "pos software",
    "desktop software",
    "expressbill",
    "storeflow",
    "sovereign computing",
    "systems architect",
    "documentshield",
    "rehan quant lab",
    "quantitative",
    "deterministic",
];

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct KeywordVectorResult {
    pub keyword: String,
    pub count: usize,
    pub density_pct: f64,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MetaAuditRecord {
    pub file: String,
    pub title: String,
    pub title_length: usize,
    pub title_valid: bool,
    pub description: String,
    pub desc_length: usize,
    pub desc_valid: bool,
    pub has_canonical: bool,
    pub has_schema_engine: bool,
    pub has_og_tags: bool,
    pub findings: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BrokenLinkAudit {
    pub total_links_checked: usize,
    pub total_assets_checked: usize,
    pub broken_links: Vec<String>,
    pub broken_assets: Vec<String>,
    pub passed: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SeoPanopticonReport {
    pub timestamp: String,
    pub base_directory: String,
    pub total_html_files: usize,
    pub total_word_count: usize,
    pub broken_links_count: usize,
    pub broken_links: Vec<String>,
    pub broken_assets_count: usize,
    pub broken_assets: Vec<String>,
    pub keyword_matrix: HashMap<String, KeywordVectorResult>,
    pub meta_audits: Vec<MetaAuditRecord>,
    pub seo_panopticon_score: u32,
    pub verdict: String,
    pub sitemap_generated: bool,
    pub robots_generated: bool,
    pub execution_micros: u64,
}

pub struct SeoEngine;

impl SeoEngine {
    /// 🦀 Microsecond Keyword Vector Density Matrix Scanner
    pub fn audit_keyword_vectors(text_content: &str) -> (usize, HashMap<String, KeywordVectorResult>) {
        let lower = text_content.to_lowercase();
        let total_words = lower.split_whitespace().count().max(1);

        let mut matrix = HashMap::with_capacity(KEYWORD_VECTORS.len());
        for &kw in KEYWORD_VECTORS {
            let count = lower.matches(kw).count();
            let density_pct = ((count as f64 / total_words as f64) * 100.0 * 100.0).round() / 100.0;
            matrix.insert(
                kw.to_string(),
                KeywordVectorResult {
                    keyword: kw.to_string(),
                    count,
                    density_pct,
                },
            );
        }

        (total_words, matrix)
    }

    /// 🦀 Native SERP Viewport Validator (Zero Truncation Guarantee)
    /// Desktop Title: 30–70 chars. Mobile Description: 50–165 chars.
    pub fn audit_serp_viewport(file_name: &str, html: &str) -> MetaAuditRecord {
        let mut findings = Vec::new();

        // 1. Extract <title>
        let title = Self::extract_tag_content(html, "<title>", "</title>").unwrap_or_default();
        let title_clean = title.trim();
        let title_length = title_clean.chars().count();
        let title_valid = title_length >= 30 && title_length <= 70;

        if title_length == 0 {
            findings.push("CRITICAL: Missing <title> tag".to_string());
        } else if title_length < 30 {
            findings.push(format!("Title is too short ({} chars < 30): underutilizing SERP window", title_length));
        } else if title_length > 70 {
            findings.push(format!("Title exceeds 70 chars ({} chars): will be truncated on Google SERP", title_length));
        }

        // 2. Extract <meta name="description" content="...">
        let description = Self::extract_meta_content(html, "description").unwrap_or_default();
        let desc_clean = description.trim();
        let desc_length = desc_clean.chars().count();
        let desc_valid = desc_length >= 50 && desc_length <= 165;

        if desc_length == 0 {
            findings.push("CRITICAL: Missing meta description tag".to_string());
        } else if desc_length < 50 {
            findings.push(format!("Meta description is too short ({} chars < 50)", desc_length));
        } else if desc_length > 165 {
            findings.push(format!("Meta description exceeds 165 chars ({} chars): truncated by Google Mobile SERP", desc_length));
        }

        // 3. Extract Canonical
        let has_canonical = html.contains("rel=\"canonical\"") || html.contains("rel='canonical'");
        if !has_canonical {
            findings.push("Missing <link rel=\"canonical\"> tag".to_string());
        }

        // 4. Extract Schema / JSON-LD Microdata
        let has_schema_engine = html.contains("application/ld+json") || html.contains("schema.org");
        if !has_schema_engine {
            findings.push("Missing Schema.org JSON-LD structured data engine".to_string());
        }

        // 5. OpenGraph Tags
        let has_og_tags = (html.contains("og:title") || html.contains("property=\"og:title\""))
            && (html.contains("og:description") || html.contains("property=\"og:description\""));
        if !has_og_tags {
            findings.push("Missing OpenGraph social sharing meta tags".to_string());
        }

        MetaAuditRecord {
            file: file_name.to_string(),
            title: title_clean.to_string(),
            title_length,
            title_valid,
            description: desc_clean.to_string(),
            desc_length,
            desc_valid,
            has_canonical,
            has_schema_engine,
            has_og_tags,
            findings,
        }
    }

    /// 🦀 Native Recursive Broken Link & Asset Spider
    /// Validates every internal href and src against local disk in microseconds
    pub fn spider_broken_links_and_assets(base_dir: &Path, file_name: &str, html: &str) -> BrokenLinkAudit {
        let mut broken_links = Vec::new();
        let mut broken_assets = Vec::new();

        let hrefs = Self::extract_attribute_values(html, "href");
        let srcs = Self::extract_attribute_values(html, "src");

        let mut total_links = 0usize;
        for raw_href in hrefs {
            let target = raw_href.trim();
            if Self::is_external_or_special_link(target) {
                continue;
            }
            total_links += 1;

            // Strip anchor (#) and query params (?)
            let clean_path = target.split('#').next().unwrap_or("").split('?').next().unwrap_or("");
            if clean_path.is_empty() {
                continue;
            }

            let normalized = clean_path.trim_start_matches('/');
            let candidate_path = base_dir.join(normalized);

            if !candidate_path.exists() {
                broken_links.push(format!("In {}: broken link href='{}' (target not on disk)", file_name, target));
            }
        }

        let mut total_assets = 0usize;
        for raw_src in srcs {
            let target = raw_src.trim();
            if Self::is_external_or_special_link(target) {
                continue;
            }
            total_assets += 1;

            let clean_path = target.split('#').next().unwrap_or("").split('?').next().unwrap_or("");
            if clean_path.is_empty() {
                continue;
            }

            let normalized = clean_path.trim_start_matches('/');
            let candidate_path = base_dir.join(normalized);

            if !candidate_path.exists() {
                broken_assets.push(format!("In {}: broken asset src='{}' (file not on disk)", file_name, target));
            }
        }

        let passed = broken_links.is_empty() && broken_assets.is_empty();

        BrokenLinkAudit {
            total_links_checked: total_links,
            total_assets_checked: total_assets,
            broken_links,
            broken_assets,
            passed,
        }
    }

    /// 🦀 Dynamic sitemap.xml Generation (ISO 8601 Dates, Priority Matrix)
    pub fn generate_sitemap_xml(domain: &str, html_files: &[String], download_files: &[String]) -> String {
        let today = Utc::now().format("%Y-%m-%d").to_string();
        let domain_clean = domain.trim_end_matches('/');

        let mut xml = String::from("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n");

        for file in html_files {
            let (route, priority, changefreq) = match file.as_str() {
                "index.html" => ("", "1.00", "weekly"),
                "store.html" => ("store.html", "1.00", "daily"),
                "projects.html" => ("projects.html", "0.90", "weekly"),
                "security.html" => ("security.html", "0.90", "weekly"),
                "aegis.html" => ("aegis.html", "0.85", "monthly"),
                "experience.html" => ("experience.html", "0.80", "monthly"),
                "contact.html" => ("contact.html", "0.80", "monthly"),
                "react_portal.html" => ("react_portal.html", "0.75", "monthly"),
                "vault.html" => ("vault.html", "0.70", "monthly"),
                "legal.html" => ("legal.html", "0.50", "yearly"),
                other => (other, "0.80", "monthly"),
            };

            let loc = if route.is_empty() {
                format!("https://{}/", domain_clean)
            } else {
                format!("https://{}/{}", domain_clean, route)
            };

            xml.push_str("  <url>\n");
            xml.push_str(&format!("    <loc>{}</loc>\n", loc));
            xml.push_str(&format!("    <lastmod>{}</lastmod>\n", today));
            xml.push_str(&format!("    <changefreq>{}</changefreq>\n", changefreq));
            xml.push_str(&format!("    <priority>{}</priority>\n", priority));
            xml.push_str("  </url>\n");
        }

        // Add downloadable brochures/assets if present
        for dl in download_files {
            xml.push_str("  <url>\n");
            xml.push_str(&format!("    <loc>https://{}/{}</loc>\n", domain_clean, dl.trim_start_matches('/')));
            xml.push_str(&format!("    <lastmod>{}</lastmod>\n", today));
            xml.push_str("    <changefreq>monthly</changefreq>\n");
            xml.push_str("    <priority>0.70</priority>\n");
            xml.push_str("  </url>\n");
        }

        xml.push_str("</urlset>\n");
        xml
    }

    /// 🦀 Dynamic robots.txt Generation
    pub fn generate_robots_txt(domain: &str) -> String {
        let today = Utc::now().format("%Y-%m-%d").to_string();
        let domain_clean = domain.trim_end_matches('/');

        format!(
            "# ====================================================================\n\
             # Rehan Quant Lab (RQL) - Search Engine Optimization Directives\n\
             # Generated Deterministically by Bare-Metal Rust Engine on {}\n\
             # ====================================================================\n\n\
             User-agent: *\n\
             Allow: /\n\
             Disallow: /vault.html\n\
             Disallow: /vault\n\
             Disallow: /platform/\n\
             Disallow: /downloads/\n\n\
             # Sitemap Index Declaration\n\
             Sitemap: https://{}/sitemap.xml\n\n\
             # Friendly Bot Optimizations\n\
             User-agent: Googlebot\n\
             Allow: /\n\n\
             User-agent: Bingbot\n\
             Allow: /\n\n\
             User-agent: Applebot\n\
             Allow: /\n\n\
             User-agent: Twitterbot\n\
             Allow: /\n\n\
             User-agent: facebookexternalhit\n\
             Allow: /\n",
            today, domain_clean
        )
    }

    /// 🦀 Full Panopticon Suite Execution across an Entire Directory
    pub fn execute_panopticon_suite(base_dir: &Path, domain: &str) -> std::io::Result<SeoPanopticonReport> {
        let t0 = Instant::now();
        let mut html_files = Vec::new();
        let mut download_files = Vec::new();

        if let Ok(entries) = fs::read_dir(base_dir) {
            for entry in entries.flatten() {
                let path = entry.path();
                if path.is_file() {
                    if let Some(ext) = path.extension().and_then(|e| e.to_str()) {
                        let fname = path.file_name().unwrap_or_default().to_string_lossy().to_string();
                        if ext == "html" {
                            // Exclude google verification stubs
                            if !fname.starts_with("google") {
                                html_files.push(fname);
                            }
                        }
                    }
                }
            }
        }
        html_files.sort();

        // Check for downloads directory
        let dl_dir = base_dir.join("downloads");
        if dl_dir.exists() {
            if let Ok(entries) = fs::read_dir(&dl_dir) {
                for entry in entries.flatten() {
                    let p = entry.path();
                    if p.is_file() {
                        if p.extension().map(|e| e == "pdf").unwrap_or(false) {
                            let fname = p.file_name().unwrap_or_default().to_string_lossy().to_string();
                            download_files.push(format!("downloads/{}", fname));
                        }
                    }
                }
            }
        }
        download_files.sort();

        // 1. Audit Meta Viewports & SERP
        let mut meta_audits = Vec::with_capacity(html_files.len());
        let mut combined_text = String::new();
        let mut all_broken_links = Vec::new();
        let mut all_broken_assets = Vec::new();

        for fname in &html_files {
            let fpath = base_dir.join(fname);
            if let Ok(content) = fs::read_to_string(&fpath) {
                // SERP Audit
                let serp = Self::audit_serp_viewport(fname, &content);
                meta_audits.push(serp);

                // Spider
                let spider = Self::spider_broken_links_and_assets(base_dir, fname, &content);
                all_broken_links.extend(spider.broken_links);
                all_broken_assets.extend(spider.broken_assets);

                // Strip HTML for keyword aggregation
                let stripped = Self::strip_html_tags(&content);
                combined_text.push_str(&stripped);
                combined_text.push(' ');
            }
        }

        // 2. Keyword Vector Density Matrix
        let (total_word_count, keyword_matrix) = Self::audit_keyword_vectors(&combined_text);

        // 3. Generate sitemap.xml & robots.txt
        let sitemap_xml = Self::generate_sitemap_xml(domain, &html_files, &download_files);
        let robots_txt = Self::generate_robots_txt(domain);

        let sitemap_path = base_dir.join("sitemap.xml");
        let robots_path = base_dir.join("robots.txt");

        let sitemap_ok = fs::write(&sitemap_path, sitemap_xml.as_bytes()).is_ok();
        let robots_ok = fs::write(&robots_path, robots_txt.as_bytes()).is_ok();

        // 4. Calculate Score (Standard SERP Invariants & Broken Links)
        let total_meta = meta_audits.len();
        let passed_titles = meta_audits.iter().filter(|m| m.title_valid).count();
        let passed_descs = meta_audits.iter().filter(|m| m.desc_valid).count();
        let passed_canon = meta_audits.iter().filter(|m| m.has_canonical).count();
        let broken_total = all_broken_links.len() + all_broken_assets.len();

        let mut score = 100u32;
        if total_meta > 0 {
            let title_pen = ((total_meta - passed_titles) as u32) * 10;
            let desc_pen = ((total_meta - passed_descs) as u32) * 10;
            let canon_pen = ((total_meta - passed_canon) as u32) * 5;
            let broken_pen = (broken_total as u32) * 15;
            score = score.saturating_sub(title_pen + desc_pen + canon_pen + broken_pen);
        }

        let elapsed_micros = t0.elapsed().as_micros() as u64;

        let all_schemas = meta_audits.iter().all(|m| m.has_schema_engine);
        let all_og = meta_audits.iter().all(|m| m.has_og_tags);
        let all_canon = meta_audits.iter().all(|m| m.has_canonical);

        // Sovereign Apex Rating Ladder (D -> C -> B -> A -> A+ -> S -> S+ -> SS -> SS+ -> SSS -> SSS+)
        let verdict = if score == 100 && broken_total == 0 && sitemap_ok && robots_ok && all_schemas && all_og && all_canon {
            "SSS+ SOVEREIGN APEX (TRANSCENDENT TITANIUM)".to_string()
        } else if score == 100 && broken_total == 0 && sitemap_ok && robots_ok && all_schemas && all_og {
            "SSS (SUPREME ARCHITECT TIER)".to_string()
        } else if score == 100 && broken_total == 0 && sitemap_ok && robots_ok && all_schemas {
            "SS+ (ULTRA-FORTIFIED QUANTUM)".to_string()
        } else if score == 100 && broken_total == 0 && sitemap_ok && robots_ok {
            "SS (TITANIUM CITADEL GRADE)".to_string()
        } else if score == 100 && broken_total == 0 {
            "S+ (HIGH SOVEREIGN GRADE)".to_string()
        } else if score == 100 {
            "S (SOVEREIGN STANDARD)".to_string()
        } else if score >= 95 && broken_total == 0 {
            "A+ COMPLIANT".to_string()
        } else if score >= 90 {
            "A (HIGH INTEGRITY)".to_string()
        } else if score >= 80 {
            "B (ACCEPTABLE WITH WARNINGS)".to_string()
        } else if score >= 70 {
            "C (SUB-OPTIMAL INDEXABILITY)".to_string()
        } else {
            "D (CRITICAL REMEDIATION REQUIRED)".to_string()
        };

        let report = SeoPanopticonReport {
            timestamp: Utc::now().format("%Y-%m-%d").to_string(),
            base_directory: base_dir.to_string_lossy().to_string(),
            total_html_files: html_files.len(),
            total_word_count,
            broken_links_count: all_broken_links.len(),
            broken_links: all_broken_links,
            broken_assets_count: all_broken_assets.len(),
            broken_assets: all_broken_assets,
            keyword_matrix,
            meta_audits,
            seo_panopticon_score: score,
            verdict,
            sitemap_generated: sitemap_ok,
            robots_generated: robots_ok,
            execution_micros: elapsed_micros,
        };

        // Write SEO_PANOPTICON_REPORT.json
        let json_path = base_dir.join("SEO_PANOPTICON_REPORT.json");
        if let Ok(json_bytes) = serde_json::to_string_pretty(&report) {
            let _ = fs::write(json_path, json_bytes);
        }

        Ok(report)
    }

    // --- Helper Utilities (Zero-Allocation byte scanners & UTF-8 Safe) ---

    pub fn strip_html_tags(html: &str) -> String {
        let mut in_tag = false;
        let mut in_script = false;
        let mut in_style = false;
        let mut text = String::with_capacity(html.len() / 2);
        let mut tag_buffer = String::with_capacity(64);

        for c in html.chars() {
            if c == '<' {
                in_tag = true;
                tag_buffer.clear();
            } else if c == '>' {
                in_tag = false;
                let tag_lower = tag_buffer.to_lowercase();
                let tag_trimmed = tag_lower.trim();
                if tag_trimmed.starts_with("script") {
                    in_script = true;
                } else if tag_trimmed.starts_with("/script") {
                    in_script = false;
                } else if tag_trimmed.starts_with("style") {
                    in_style = true;
                } else if tag_trimmed.starts_with("/style") {
                    in_style = false;
                }
                tag_buffer.clear();
            } else if in_tag {
                tag_buffer.push(c);
            } else if !in_script && !in_style {
                text.push(c);
            }
        }
        text
    }

    pub fn extract_tag_content(html: &str, open_tag: &str, close_tag: &str) -> Option<String> {
        let lower = html.to_lowercase();
        let open_lower = open_tag.to_lowercase();
        let close_lower = close_tag.to_lowercase();
        if let Some(start_pos) = lower.find(&open_lower) {
            let after_open = start_pos + open_lower.len();
            if let Some(end_pos) = lower[after_open..].find(&close_lower) {
                let content = &lower[after_open..after_open + end_pos];
                return Some(content.trim().to_string());
            }
        }
        None
    }

    pub fn extract_meta_content(html: &str, meta_name: &str) -> Option<String> {
        let lower = html.to_lowercase();
        let target_name = format!("name=\"{}\"", meta_name.to_lowercase());
        let target_name_sq = format!("name='{}'", meta_name.to_lowercase());

        for tag in lower.split('<') {
            if tag.starts_with("meta") {
                let end_tag = tag.split('>').next().unwrap_or("");
                if end_tag.contains(&target_name) || end_tag.contains(&target_name_sq) {
                    if let Some(content) = Self::extract_attribute_from_tag(end_tag, "content") {
                        return Some(content);
                    }
                }
            }
        }
        None
    }

    pub fn extract_attribute_from_tag(tag: &str, attr: &str) -> Option<String> {
        let patterns = [format!("{}=\"", attr), format!("{}='", attr)];
        for p in &patterns {
            if let Some(pos) = tag.find(p) {
                let quote = tag.as_bytes()[pos + p.len() - 1];
                let val_start = pos + p.len();
                if let Some(val_len) = tag[val_start..].find(quote as char) {
                    return Some(tag[val_start..val_start + val_len].to_string());
                }
            }
        }
        None
    }

    pub fn extract_attribute_values(html: &str, attr: &str) -> Vec<String> {
        let mut results = Vec::new();
        let lower = html.to_lowercase();
        let patterns = [format!("{}=\"", attr), format!("{}='", attr)];

        for p in &patterns {
            let mut search_idx = 0;
            while let Some(pos) = lower[search_idx..].find(p) {
                let abs_pos = search_idx + pos;
                let quote = lower.as_bytes()[abs_pos + p.len() - 1];
                let val_start = abs_pos + p.len();

                if let Some(end_offset) = lower[val_start..].find(quote as char) {
                    let val = &lower[val_start..val_start + end_offset];
                    results.push(val.to_string());
                    search_idx = val_start + end_offset + 1;
                } else {
                    search_idx = val_start + 1;
                }
            }
        }
        results
    }

    fn is_external_or_special_link(link: &str) -> bool {
        let l = link.trim().to_lowercase();
        l.is_empty()
            || l.starts_with('#')
            || l.starts_with("http://")
            || l.starts_with("https://")
            || l.starts_with("//")
            || l.starts_with("mailto:")
            || l.starts_with("tel:")
            || l.starts_with("sms:")
            || l.starts_with("upi:")
            || l.starts_with("intent:")
            || l.starts_with("javascript:")
            || l.starts_with("data:")
            || l.starts_with('\'')
            || l.starts_with('"')
            || l.starts_with("blob:")
            || l.contains("data.")
            || l.contains('+')
    }
}
