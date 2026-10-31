// ============================================================================
// REHAN QUANT LAB™ — BARE-METAL PURE-RUST HTTP DEV SERVER & STUDIO HOST
// "Zero Node.js • Zero Python • Multi-Threaded Sub-Millisecond Silicon Server"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

use std::fs;
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::path::Path;
use std::sync::Arc;
use std::thread;
use std::time::Instant;

use crate::studio::{VisualStudioCompileRequest, VisualStudioEngine};

pub struct DevServer;

impl DevServer {
    /// 🌐 Start multi-threaded local development server & Sovereign Studio
    pub fn start_server(root_dir: &Path, port: u16) -> std::io::Result<()> {
        let addr = format!("127.0.0.1:{}", port);
        let listener = TcpListener::bind(&addr)?;
        let root = Arc::new(root_dir.to_path_buf());

        println!("\x1b[1;36m====================================================================\x1b[0m");
        println!("\x1b[1;32m🌐 REHAN QUANT LAB™ — BARE-METAL DEV SERVER & VISUAL STUDIO\x1b[0m");
        println!("   \x1b[1;33m• Localhost URL:   http://localhost:{}\x1b[0m", port);
        println!("   \x1b[1;32m• VISUAL STUDIO:   http://localhost:{}/studio\x1b[0m", port);
        println!("   \x1b[1;35m• Serving Root:    {:?}\x1b[0m", root_dir);
        println!("   \x1b[1;34m• Zero Node.js     • Zero Python    • Bare-Metal Silicon Speed\x1b[0m");
        println!("   \x1b[1;32m• Status:          LISTENING & READY (Press Ctrl+C to stop)\x1b[0m");
        println!("\x1b[1;36m====================================================================\x1b[0m\n");

        for stream in listener.incoming() {
            match stream {
                Ok(mut stream) => {
                    let root_clone = Arc::clone(&root);
                    thread::spawn(move || {
                        let _ = Self::handle_connection(&mut stream, &root_clone);
                    });
                }
                Err(e) => eprintln!("Connection error: {}", e),
            }
        }

        Ok(())
    }

    fn handle_connection(stream: &mut TcpStream, root: &Path) -> std::io::Result<()> {
        let t0 = Instant::now();
        let mut buffer = Vec::with_capacity(16384);
        let mut temp = [0u8; 8192];

        let bytes_read = stream.read(&mut temp)?;
        if bytes_read == 0 {
            return Ok(());
        }
        buffer.extend_from_slice(&temp[..bytes_read]);

        // Find header-body boundary \r\n\r\n
        let mut header_end = 0;
        let mut content_length = 0usize;

        let req_str = String::from_utf8_lossy(&buffer);
        if let Some(pos) = req_str.find("\r\n\r\n") {
            header_end = pos + 4;
            for line in req_str[..pos].lines() {
                if line.to_lowercase().starts_with("content-length:") {
                    if let Some(val) = line.split(':').nth(1) {
                        content_length = val.trim().parse::<usize>().unwrap_or(0);
                    }
                }
            }
        }

        // Read remaining body bytes if needed
        let body_already_read = buffer.len().saturating_sub(header_end);
        let mut needed = content_length.saturating_sub(body_already_read);
        while needed > 0 {
            let n = stream.read(&mut temp)?;
            if n == 0 {
                break;
            }
            buffer.extend_from_slice(&temp[..n]);
            needed = needed.saturating_sub(n);
        }

        let full_request = String::from_utf8_lossy(&buffer);
        let mut lines = full_request.lines();
        let request_line = lines.next().unwrap_or("");
        let mut parts = request_line.split_whitespace();

        let method = parts.next().unwrap_or("GET");
        let raw_path = parts.next().unwrap_or("/");
        let is_head = method == "HEAD";

        // Clean path, remove query params & hashes
        let clean_path = raw_path.split('?').next().unwrap_or("/").split('#').next().unwrap_or("/");
        let decoded_path = clean_path.trim_start_matches('/');

        // 1. ROUTE: GET /studio -> Serve Sovereign Visual Studio IDE
        if (method == "GET" || is_head) && (decoded_path == "studio" || decoded_path == "studio/") {
            let studio_html = VisualStudioEngine::get_studio_html();
            return Self::send_response(stream, 200, "OK", studio_html.as_bytes(), "text/html; charset=utf-8", is_head, t0.elapsed());
        }

        // 2. ROUTE: POST /api/studio/compile -> Compile Visual Page via Pentagon Loop
        if method == "POST" && decoded_path == "api/studio/compile" {
            let body = &full_request[header_end..];
            let res_json = match serde_json::from_str::<VisualStudioCompileRequest>(body) {
                Ok(req) => match VisualStudioEngine::compile_visual_page(root, &req) {
                    Ok(resp) => serde_json::to_string(&resp).unwrap_or_default(),
                    Err(e) => format!(r#"{{"success":false,"error":"{}"}}"#, e),
                },
                Err(e) => format!(r#"{{"success":false,"error":"Invalid JSON: {}"}}"#, e),
            };
            return Self::send_response(stream, 200, "OK", res_json.as_bytes(), "application/json", false, t0.elapsed());
        }

        // 3. ROUTE: POST /api/studio/deploy -> Deploy directly from Visual Studio
        if method == "POST" && decoded_path == "api/studio/deploy" {
            let (success, log) = VisualStudioEngine::deploy_from_studio(root, "mohammadrehan", "rehanquantlab.com")
                .unwrap_or_else(|e| (false, e));
            let res_json = format!(r#"{{"success":{},"log":"{}"}}"#, success, log.replace('"', "\\\"").replace('\n', " "));
            return Self::send_response(stream, 200, "OK", res_json.as_bytes(), "application/json", false, t0.elapsed());
        }

        // 3B. ROUTE: POST /api/leads/submit -> Offline Leads CRM Append-Only Ingestion
        if method == "POST" && (decoded_path == "api/leads/submit" || decoded_path == "api/studio/leads") {
            let body = &full_request[header_end..];
            let leads_file = root.join("leads_vault.jsonl");
            let mut line = body.trim().to_string();
            if !line.is_empty() {
                line.push('\n');
                let _ = fs::OpenOptions::new().create(true).append(true).open(&leads_file)
                    .and_then(|mut f| f.write_all(line.as_bytes()));
            }
            let res_json = r#"{"success":true,"message":"Lead securely sealed into Sovereign WAL"}"#;
            return Self::send_response(stream, 200, "OK", res_json.as_bytes(), "application/json", false, t0.elapsed());
        }

        // 3C. ROUTE: GET /api/leads/export.csv -> Download Offline Leads as CSV
        if (method == "GET" || is_head) && decoded_path == "api/leads/export.csv" {
            let leads_file = root.join("leads_vault.jsonl");
            let mut csv_data = String::from("timestamp,name,email,service,message\n");
            if let Ok(content) = fs::read_to_string(&leads_file) {
                for line in content.lines() {
                    if let Ok(val) = serde_json::from_str::<serde_json::Value>(line) {
                        let ts = val.get("timestamp").and_then(|v| v.as_str()).unwrap_or("");
                        let name = val.get("name").and_then(|v| v.as_str()).unwrap_or("").replace(',', " ");
                        let email = val.get("email").and_then(|v| v.as_str()).unwrap_or("").replace(',', " ");
                        let service = val.get("service").and_then(|v| v.as_str()).unwrap_or("").replace(',', " ");
                        let msg = val.get("message").and_then(|v| v.as_str()).unwrap_or("").replace(',', " ").replace('\n', " ");
                        csv_data.push_str(&format!("{},{},{},{},{}\n", ts, name, email, service, msg));
                    }
                }
            }
            let headers = "HTTP/1.1 200 OK\r\nContent-Type: text/csv\r\nContent-Disposition: attachment; filename=\"rql_sovereign_leads.csv\"\r\nConnection: close\r\n\r\n";
            let mut res = headers.as_bytes().to_vec();
            if !is_head {
                res.extend_from_slice(csv_data.as_bytes());
            }
            stream.write_all(&res)?;
            return Ok(());
        }

        if method != "GET" && !is_head {
            let res = "HTTP/1.1 405 Method Not Allowed\r\nContent-Length: 0\r\n\r\n";
            stream.write_all(res.as_bytes())?;
            return Ok(());
        }

        // 4. ROUTE: Static files
        let mut candidate = if decoded_path.is_empty() {
            root.join("index.html")
        } else {
            root.join(decoded_path)
        };

        if !candidate.exists() && !candidate.extension().is_some() {
            let with_html = root.join(format!("{}.html", decoded_path));
            if with_html.exists() {
                candidate = with_html;
            }
        }

        let (status_code, status_text, body, content_type) = if candidate.is_file() && candidate.exists() {
            let bytes = fs::read(&candidate).unwrap_or_default();
            let mime = Self::get_mime_type(&candidate);
            (200, "OK", bytes, mime)
        } else {
            let not_found_path = root.join("404.html");
            let bytes = if not_found_path.exists() {
                fs::read(not_found_path).unwrap_or_default()
            } else {
                b"<h1>404 Not Found - Rehan Quant Lab</h1>".to_vec()
            };
            (404, "Not Found", bytes, "text/html; charset=utf-8")
        };

        Self::send_response(stream, status_code, status_text, &body, content_type, is_head, t0.elapsed())
    }

    fn send_response(
        stream: &mut TcpStream,
        status_code: u16,
        status_text: &str,
        body: &[u8],
        content_type: &str,
        is_head: bool,
        elapsed: std::time::Duration,
    ) -> std::io::Result<()> {
        let response_headers = format!(
            "HTTP/1.1 {} {}\r\n\
             Content-Type: {}\r\n\
             Content-Length: {}\r\n\
             Connection: close\r\n\
             Server: RQL-BareMetal-Rust\r\n\
             Access-Control-Allow-Origin: *\r\n\r\n",
            status_code,
            status_text,
            content_type,
            body.len()
        );

        stream.write_all(response_headers.as_bytes())?;
        if !is_head {
            stream.write_all(body)?;
        }
        stream.flush()?;

        let status_color = if status_code == 200 { "\x1b[1;32m" } else { "\x1b[1;31m" };
        println!(
            "   [HTTP] Status: {}{}\x1b[0m | Size: {:>7}B | {:>6.2?}",
            status_color, status_code, body.len(), elapsed
        );

        Ok(())
    }

    fn get_mime_type(path: &Path) -> &'static str {
        match path.extension().and_then(|e| e.to_str()).unwrap_or("") {
            "html" | "htm" => "text/html; charset=utf-8",
            "css" => "text/css; charset=utf-8",
            "js" | "mjs" => "application/javascript; charset=utf-8",
            "wasm" => "application/wasm",
            "json" => "application/json; charset=utf-8",
            "png" => "image/png",
            "jpg" | "jpeg" => "image/jpeg",
            "webp" => "image/webp",
            "svg" => "image/svg+xml",
            "pdf" => "application/pdf",
            "xml" => "application/xml; charset=utf-8",
            "txt" => "text/plain; charset=utf-8",
            "ico" => "image/x-icon",
            "woff2" => "font/woff2",
            "woff" => "font/woff",
            "ttf" => "font/ttf",
            _ => "application/octet-stream",
        }
    }
}
