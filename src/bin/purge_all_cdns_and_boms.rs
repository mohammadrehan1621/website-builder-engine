// ============================================================================
// 🏛️ REHAN QUANT LAB™ — UNIVERSAL CDN PURGE & 7-BIT ASCII IMMUNITY ENGINE
// ============================================================================
// Strips BOMs, self-hosts Lucide/Confetti/QRCode, secures Aegis downloads,
// and enforces 100% 7-bit ASCII mojibake immunity across all HTML files.
// ============================================================================

use std::fs;
use std::path::Path;

fn main() {
    println!("[*] Launching Sovereign CDN Purge & 7-Bit ASCII Immunity Engine...");
    let web_dir = Path::new("Deployed_Websites/mohammadrehan.pages.dev");

    // 1. Process all HTML files
    for entry in fs::read_dir(web_dir).unwrap() {
        let entry = entry.unwrap();
        let path = entry.path();
        if path.extension().map(|e| e == "html").unwrap_or(false) {
            let filename = path.file_name().unwrap().to_string_lossy().to_string();
            if filename == "googlecb5b21d2c61033d5.html" {
                // Just strip BOM if present
                let bytes = fs::read(&path).unwrap();
                if bytes.starts_with(&[0xEF, 0xBB, 0xBF]) {
                    fs::write(&path, &bytes[3..]).unwrap();
                    println!("    [+] Stripped BOM from {}", filename);
                }
                continue;
            }

            let mut content = fs::read_to_string(&path).unwrap();
            
            // Strip BOM character if read_to_string preserved it
            if content.starts_with('\u{feff}') {
                content = content.trim_start_matches('\u{feff}').to_string();
                println!("    [+] Removed BOM character from {}", filename);
            }

            // Replace unpkg Lucide scripts with local self-hosted asset
            content = content.replace("https://unpkg.com/lucide@latest", "assets/lucide.min.js");

            // Purge unpkg preconnects and dns-prefetch
            content = content.replace("<link rel=\"preconnect\" href=\"https://unpkg.com\" crossorigin>\r\n", "");
            content = content.replace("<link rel=\"preconnect\" href=\"https://unpkg.com\" crossorigin>\n", "");
            content = content.replace("<link rel=\"preconnect\" href=\"https://unpkg.com\" crossorigin=\"\">\r\n", "");
            content = content.replace("<link rel=\"preconnect\" href=\"https://unpkg.com\" crossorigin=\"\">\n", "");
            content = content.replace("<link rel=\"preconnect\" href=\"https://unpkg.com\">\r\n", "");
            content = content.replace("<link rel=\"preconnect\" href=\"https://unpkg.com\">\n", "");
            content = content.replace("<link crossorigin href=\"https://unpkg.com\" rel=\"preconnect\"/>", "");
            content = content.replace("<link rel=\"dns-prefetch\" href=\"https://unpkg.com\">\r\n", "");
            content = content.replace("<link rel=\"dns-prefetch\" href=\"https://unpkg.com\">\n", "");

            // Replace jsdelivr confetti with local self-hosted asset
            content = content.replace("https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.4/dist/confetti.browser.min.js", "assets/confetti.browser.min.js");

            // Replace cdnjs qrcode with local self-hosted asset
            content = content.replace("https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js", "assets/qrcode.min.js");

            // Ensure rql-shield.js is injected before </head>
            if !content.contains("rql-shield.js") && filename != "googlecb5b21d2c61033d5.html" {
                if content.contains("</head>") {
                    content = content.replace("</head>", "    <script src=\"assets/rql-shield.js\"></script>\r\n</head>");
                    println!("    [+] Injected rql-shield.js into {}", filename);
                }
            }

            // Specific page customizations
            if filename == "aegis.html" {
                // Obfuscate download link: downloads/RQL-Aegis-v1.0-Release.zip -> base64: ZG93bmxvYWRzL1JRTC1BZWdpcy12MS4wLVJlbGVhc2Uuemlw
                content = content.replace(
                    "href=\"RQL-Aegis-v1.0-Release.zip\" download",
                    "data-obf=\"ZG93bmxvYWRzL1JRTC1BZWdpcy12MS4wLVJlbGVhc2Uuemlw\" role=\"button\""
                );
                content = content.replace(
                    "href=\"RQL-Aegis-v1.0-Release.zip\"",
                    "data-obf=\"ZG93bmxvYWRzL1JRTC1BZWdpcy12MS4wLVJlbGVhc2Uuemlw\" role=\"button\""
                );
            }

            if filename == "legal.html" {
                // Ensure Section 15 title is explicitly labeled
                content = content.replace(
                    "<h2 class=\"text-lg font-bold text-slate-900\">Business Details, Operator Coordinates",
                    "<h2 class=\"text-lg font-bold text-slate-900\">Section 15: Business Details, Operator Coordinates"
                );
            }

            if filename == "react_portal.html" {
                // Purge box characters and non-ASCII glyphs
                content = content.replace('\u{2500}', "-");
                content = content.replace('\u{00B5}', "&micro;");
                content = content.replace('\u{2694}', "&bull;");
                content = content.replace('\u{2705}', "&radic;");
                content = content.replace('\u{2B07}', "&darr;");
            }

            // Write back strictly as raw 7-bit ASCII bytes without BOM
            let mut final_bytes = Vec::new();
            for b in content.bytes() {
                if b > 127 {
                    // Safety fallback: replace any remaining non-ASCII with space
                    final_bytes.push(b' ');
                } else {
                    final_bytes.push(b);
                }
            }
            fs::write(&path, final_bytes).unwrap();
            println!("    [✔] Successfully processed & hardened: {}", filename);
        }
    }

    println!("[*] Purge & Hardening cycle complete.");
}
