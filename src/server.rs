// ============================================================================
// REHAN QUANT LAB™ — BARE-METAL PURE-RUST HTTP DEV SERVER
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

pub struct DevServer;

impl DevServer {
    /// 🌐 Start multi-threaded local development server with zero runtime dependencies
    pub fn start_server(root_dir: &Path, port: u16) -> std::io::Result<()> {
        let addr = format!("127.0.0.1:{}", port);
        let listener = TcpListener::bind(&addr)?;
        let root = Arc::new(root_dir.to_path_buf());

        println!("\x1b[1;36m====================================================================\x1b[0m");
        println!("\x1b[1;32m🌐 REHAN QUANT LAB™ — PURE-RUST BARE-METAL DEV SERVER\x1b[0m");
        println!("   \x1b[1;33m• Localhost URL:   http://localhost:{}\x1b[0m", port);
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
        let mut buffer = [0u8; 4096];
        let bytes_read = stream.read(&mut buffer)?;
        if bytes_read == 0 {
            return Ok(());
        }

        let request = String::from_utf8_lossy(&buffer[..bytes_read]);
        let mut lines = request.lines();
        let request_line = lines.next().unwrap_or("");
        let mut parts = request_line.split_whitespace();

        let method = parts.next().unwrap_or("GET");
        let raw_path = parts.next().unwrap_or("/");

        if method != "GET" && method != "HEAD" {
            let res = "HTTP/1.1 405 Method Not Allowed\r\nContent-Length: 0\r\n\r\n";
            stream.write_all(res.as_bytes())?;
            return Ok(());
        }

        // Clean path, remove query params & hashes
        let clean_path = raw_path.split('?').next().unwrap_or("/").split('#').next().unwrap_or("/");
        let decoded_path = clean_path.trim_start_matches('/');

        let mut candidate = if decoded_path.is_empty() {
            root.join("index.html")
        } else {
            root.join(decoded_path)
        };

        // Try appending .html if not found
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
        if method != "HEAD" {
            stream.write_all(&body)?;
        }
        stream.flush()?;

        let elapsed = t0.elapsed();
        let status_color = if status_code == 200 { "\x1b[1;32m" } else { "\x1b[1;31m" };
        println!(
            "   [HTTP] {} {} | Status: {}{}\x1b[0m | Size: {:>7}B | {:>6.2?}",
            method, raw_path, status_color, status_code, body.len(), elapsed
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
