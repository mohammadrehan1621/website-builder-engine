// ============================================================================
// REHAN QUANT LAB™ — UNIVERSAL SCHEMA.ORG RICH-SNIPPET ENGINE
// "Google SERP Rich Cards • SoftwareApplication • AggregateRating • Star Ratings"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

use std::fs;
use std::path::Path;

pub struct SchemaEngine;

impl SchemaEngine {
    /// 🧬 Injects Google-compliant Schema.org JSON-LD structured data into all pages
    pub fn enrich_directory_with_schemas(dir: &Path, domain: &str) -> std::io::Result<usize> {
        let domain_clean = domain.trim_end_matches('/');
        let mut enriched_count = 0usize;

        if let Ok(entries) = fs::read_dir(dir) {
            for entry in entries.flatten() {
                let path = entry.path();
                if path.is_file() && path.extension().and_then(|e| e.to_str()) == Some("html") {
                    let fname = path.file_name().unwrap_or_default().to_string_lossy().to_string();
                    if fname.starts_with("google") {
                        continue;
                    }

                    if let Ok(content) = fs::read_to_string(&path) {
                        // If page already has rich schema, check if it's full or needs augmentation
                        let has_schema = content.contains("application/ld+json");
                        if !has_schema {
                            let schema_json = Self::generate_schema_for_file(&fname, domain_clean);
                            let script_tag = format!(
                                "\n  <!-- Schema.org JSON-LD Rich Snippet Invariant -->\n  <script type=\"application/ld+json\">\n{}\n  </script>\n</head>",
                                schema_json
                            );
                            if content.contains("</head>") {
                                let new_content = content.replace("</head>", &script_tag);
                                let _ = fs::write(&path, new_content.as_bytes());
                                enriched_count += 1;
                            }
                        }
                    }
                }
            }
        }

        Ok(enriched_count)
    }

    pub fn generate_schema_for_file(file_name: &str, domain: &str) -> String {
        match file_name {
            "aegis.html" => format!(
                r#"{{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "AegisDB & RQL Aegis™ Quant Engine",
  "operatingSystem": "Linux, Windows, macOS (Bare-Metal)",
  "applicationCategory": "FinancialApplication, DeveloperApplication",
  "offers": {{
    "@type": "Offer",
    "price": "0.00",
    "priceCurrency": "USD"
  }},
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "4.95",
    "reviewCount": "84"
  }},
  "description": "Deterministic quantitative orderbook risk kernel and high-throughput memory engine."
}}"#
            ),
            "legal.html" => format!(
                r#"{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Statutory Compliance & Legal Terms — Rehan Quant Lab",
  "url": "https://{}/legal.html",
  "description": "Statutory disclosures, SEBI non-advisory operational declaration, and terms of service."
}}"#,
                domain
            ),
            "react_portal.html" => format!(
                r#"{{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Rehan Quant Lab React 3D Sovereign Portal",
  "url": "https://{}/react_portal.html",
  "applicationCategory": "InteractiveApplication",
  "operatingSystem": "Web",
  "browserRequirements": "Requires WebGL, HTML5, JavaScript"
}}"#,
                domain
            ),
            "vault.html" => format!(
                r#"{{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "RQL Founder Sovereign Studio • CW & ACW Engine",
  "url": "https://{}/vault.html",
  "applicationCategory": "SecurityApplication",
  "operatingSystem": "Web, iOS, Android (PWA)"
}}"#,
                domain
            ),
            "404.html" => format!(
                r#"{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "404 Not Found — Rehan Quant Lab",
  "url": "https://{}/404.html"
}}"#,
                domain
            ),
            _ => format!(
                r#"{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Rehan Quant Lab™ — Sovereign Systems",
  "url": "https://{}/{}",
  "publisher": {{
    "@type": "Organization",
    "name": "Rehan Quant Lab™",
    "url": "https://{}"
  }}
}}"#,
                domain, file_name, domain
            ),
        }
    }
}
