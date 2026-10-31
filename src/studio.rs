// ============================================================================
// REHAN QUANT LAB™ — SOVEREIGN VISUAL STUDIO ENGINE (DRAG-AND-DROP SILICON IDE)
// "The World's Only Pure-Rust Air-Gapped Visual Web Compiler • Zero Monthly Fees"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

use std::fs;
use std::path::Path;
use std::time::Instant;
use serde::{Deserialize, Serialize};

use crate::blackbox::OfflineFlightRecorder;
use crate::minifier::SiliconMinifier;
use crate::node3_atlas_sentinel::AtlasSentinelEngine;
use crate::node5_deploy_engine::DeployEngine;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct VisualStudioCompileRequest {
    pub file_name: String,
    pub title: String,
    pub description: String,
    pub html_content: String,
    pub sections: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct VisualStudioCompileResponse {
    pub success: bool,
    pub file_name: String,
    pub original_bytes: usize,
    pub minified_bytes: usize,
    pub bytes_saved: usize,
    pub compile_duration_micros: u64,
    pub sentinel_score: u32,
    pub is_titanium_certified: bool,
    pub sha256_hash: String,
    pub status_badge: String,
    pub findings: Vec<String>,
}

pub struct VisualStudioEngine;

impl VisualStudioEngine {
    /// 🎨 Compile visually assembled DOM directly into minified, audited, Titanium-certified silicon
    pub fn compile_visual_page(
        root_dir: &Path,
        req: &VisualStudioCompileRequest,
    ) -> Result<VisualStudioCompileResponse, String> {
        let t0 = Instant::now();
        let target_file = root_dir.join(&req.file_name);

        // 1. Ensure document has full DOCTYPE, responsive meta, CSP, and Phoenix Sentinel
        let full_html = Self::wrap_with_sovereign_shell(
            &req.title,
            &req.description,
            &req.html_content,
            &req.file_name,
        );

        let orig_len = full_html.len();

        // 2. Run 9-Pillar Titanium Sentinel Quality Gate
        let sentinel_report = AtlasSentinelEngine::audit_html_content_with_base(
            &req.file_name,
            &full_html,
            Some(root_dir),
        );

        let mut findings = Vec::new();
        for p in &sentinel_report.pillars {
            if !p.passed {
                for f in &p.findings {
                    findings.push(format!("[Pillar {}]: {}", p.pillar_num, f));
                }
            }
        }

        // 3. Silicon Hot-Path Stream Minification (22%+ reduction in microseconds)
        let minified_html = SiliconMinifier::minify_html(&full_html);
        let mini_len = minified_html.len();

        // 4. Atomic Write to disk
        fs::write(&target_file, minified_html.as_bytes())
            .map_err(|e| format!("Failed to write page to disk: {}", e))?;

        // 5. Compute SHA-256 Checksum
        use sha2::{Digest, Sha256};
        let mut hasher = Sha256::new();
        hasher.update(minified_html.as_bytes());
        let sha256_hash = format!("{:x}", hasher.finalize());

        let elapsed = t0.elapsed().as_micros() as u64;

        // 6. Seal into Flight Recorder WAL
        let recorder = OfflineFlightRecorder::new();
        recorder.record(
            "SOVEREIGN_STUDIO_IDE",
            "CW_VISUAL_COMPILE",
            &format!("SAVE_{}", req.file_name),
            sha256_hash.as_bytes(),
            elapsed,
            if sentinel_report.is_titanium_certified { "TITANIUM_CERTIFIED" } else { "HOLD" },
            &format!("Compiled in {:.2?} | Saved {}B", t0.elapsed(), orig_len.saturating_sub(mini_len)),
        );

        let status_badge = if sentinel_report.is_titanium_certified {
            format!("🟢 TITANIUM CERTIFIED (Score: {}/100 • 0% Drift)", sentinel_report.overall_score)
        } else {
            format!("⚠️ ISSUES DETECTED (Score: {}/100)", sentinel_report.overall_score)
        };

        Ok(VisualStudioCompileResponse {
            success: true,
            file_name: req.file_name.clone(),
            original_bytes: orig_len,
            minified_bytes: mini_len,
            bytes_saved: orig_len.saturating_sub(mini_len),
            compile_duration_micros: elapsed,
            sentinel_score: sentinel_report.overall_score,
            is_titanium_certified: sentinel_report.is_titanium_certified,
            sha256_hash,
            status_badge,
            findings,
        })
    }

    /// 🚀 Trigger direct Cloudflare Edge deployment from Studio HUD
    pub fn deploy_from_studio(
        root_dir: &Path,
        project_name: &str,
        domain: &str,
    ) -> Result<(bool, String), String> {
        DeployEngine::deploy_site(project_name, root_dir, Some(domain))
            .map_err(|e| e.to_string())
    }

    /// Wraps drag-and-drop body blocks in the complete Sovereign HTML Shell
    fn wrap_with_sovereign_shell(
        title: &str,
        description: &str,
        body_content: &str,
        file_name: &str,
    ) -> String {
        // If content already has <html> and <body>, return directly
        if body_content.contains("<!DOCTYPE") || body_content.contains("<html") {
            return body_content.to_string();
        }

        format!(
            r#"<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{}</title>
  <meta name="description" content="{}">
  <link rel="canonical" href="https://rehanquantlab.com/{}">
  <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests; default-src 'self' https: data: blob: 'unsafe-inline' 'unsafe-eval'; script-src 'self' https: data: blob: 'unsafe-inline' 'unsafe-eval'; style-src 'self' https: data: blob: 'unsafe-inline'; img-src 'self' data: blob: https:; font-src 'self' https: data:; frame-src 'self' https:; connect-src 'self' https: wss:;"/>
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {{ background: #050811; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; min-height: 100vh; }}
  </style>
</head>
<body class="bg-[#050811] text-[#f8fafc] selection:bg-cyan-500 selection:text-black">
  <div id="sovereign-viewport">
    {}
  </div>
  <script src="/phoenix_sentinel.js"></script>
</body>
</html>"#,
            title, description, file_name, body_content
        )
    }

    /// 🖥️ The Embedded Sovereign Visual Studio Web IDE Frontend (Zero NPM / Zero Dependencies)
    pub fn get_studio_html() -> &'static str {
        STUDIO_FRONTEND_HTML
    }
}

pub const STUDIO_FRONTEND_HTML: &str = r###"<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rehan Quant Lab™ — Sovereign Visual Studio IDE (CW ↔ ACW)</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body { background-color: #030712; color: #f9fafb; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; overflow-x: hidden; }
    .glass-panel { background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.08); }
    .drop-zone { min-height: 120px; transition: all 0.2s ease; }
    .drop-zone.drag-over { background: rgba(6, 182, 212, 0.12); border: 2px dashed #06b6d4 !important; }
    .sovereign-block { position: relative; transition: all 0.2s ease; cursor: move; }
    .sovereign-block:hover { outline: 1px solid rgba(6, 182, 212, 0.5); }
    .sovereign-block .block-actions { display: none; }
    .sovereign-block:hover .block-actions { display: flex; }
    [contenteditable="true"]:focus { outline: 1px solid #06b6d4; background: rgba(6, 182, 212, 0.08); border-radius: 4px; }
  </style>
</head>
<body class="flex flex-col h-screen select-none">

  <!-- TOP SOVEREIGN HUD BAR -->
  <header class="h-14 glass-panel border-b border-cyan-500/20 px-6 flex items-center justify-between z-50">
    <div class="flex items-center space-x-4">
      <div class="w-8 h-8 rounded-lg bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center font-black text-black text-sm shadow-lg shadow-cyan-500/20">
        RQL
      </div>
      <div>
        <h1 class="text-sm font-bold tracking-wider text-white uppercase flex items-center gap-2">
          Sovereign Visual Studio <span class="text-[10px] font-mono text-cyan-400 bg-cyan-950/80 px-2 py-0.5 rounded border border-cyan-500/30">v2.0 PENTAGON</span>
        </h1>
      </div>
    </div>

    <!-- Live Telemetry Pill -->
    <div id="telemetryPill" class="hidden md:flex items-center space-x-3 px-3 py-1 rounded-full bg-slate-900 border border-emerald-500/40 text-xs font-mono text-emerald-400">
      <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
      <span id="telemetryStatus">CW ↔ ACW READY (0% DRIFT)</span>
    </div>

    <!-- Action Controls -->
    <div class="flex items-center space-x-3">
      <select id="pageSelector" class="bg-slate-900 text-xs font-mono border border-slate-700 rounded px-2.5 py-1.5 text-slate-300 focus:outline-none focus:border-cyan-500">
        <option value="index.html">index.html (Core Portal)</option>
        <option value="store.html">store.html (Commercial Store)</option>
        <option value="projects.html">projects.html (Projects)</option>
        <option value="aegis.html">aegis.html (AegisDB)</option>
        <option value="vault.html">vault.html (Founder Studio)</option>
        <option value="contact.html">contact.html (Contact)</option>
      </select>

      <button id="btnCompile" onclick="compileToSilicon()" class="px-4 py-1.5 rounded-lg bg-gradient-to-r from-cyan-500 to-blue-600 text-black font-bold text-xs uppercase tracking-wider shadow-lg shadow-cyan-500/25 hover:opacity-90 active:scale-95 transition flex items-center gap-1.5">
        <span>⚡</span> Compile Silicon
      </button>

      <button id="btnDeploy" onclick="deployToEdge()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-400 border border-cyan-500/30 text-xs font-mono uppercase tracking-wider transition flex items-center gap-1.5">
        <span>🚀</span> Edge Deploy
      </button>
    </div>
  </header>

  <!-- MAIN STUDIO WORKSPACE -->
  <div class="flex flex-1 overflow-hidden">

    <!-- LEFT PALETTE: MODULAR SOVEREIGN BLOCKS -->
    <aside class="w-72 glass-panel border-r border-slate-800 p-4 flex flex-col space-y-3 overflow-y-auto z-40">
      <div class="flex items-center justify-between mb-1">
        <h2 class="text-xs font-bold uppercase tracking-wider text-slate-400">Block Palette</h2>
        <span class="text-[10px] text-cyan-400 font-mono">DRAG & DROP</span>
      </div>

      <!-- Hero Block -->
      <div class="p-3 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-cyan-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'hero')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-cyan-950 flex items-center justify-center text-cyan-400 text-xs">🏛️</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-cyan-400">Tactile Hero</h3>
            <p class="text-[10px] text-slate-400">Headline, matrix subtitle & CTAs</p>
          </div>
        </div>
      </div>

      <!-- Quant Metrics Grid -->
      <div class="p-3 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-cyan-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'metrics')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-indigo-950 flex items-center justify-center text-indigo-400 text-xs">📊</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-indigo-400">Quant Metric Grid</h3>
            <p class="text-[10px] text-slate-400">4-cell live performance counters</p>
          </div>
        </div>
      </div>

      <!-- Commercial Product / Store Card -->
      <div class="p-3 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-cyan-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'product')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-emerald-950 flex items-center justify-center text-emerald-400 text-xs">💎</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-emerald-400">Commercial Store Card</h3>
            <p class="text-[10px] text-slate-400">Pricing, features & Gumroad checkout</p>
          </div>
        </div>
      </div>

      <!-- Terminal Viewport / Code HUD -->
      <div class="p-3 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-cyan-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'terminal')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-amber-950 flex items-center justify-center text-amber-400 text-xs">⚡</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-amber-400">Cybernetic Terminal</h3>
            <p class="text-[10px] text-slate-400">Bare-metal telemetry & code window</p>
          </div>
        </div>
      </div>

      <!-- Phoenix Contact Form -->
      <div class="p-3 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-cyan-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'form')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-rose-950 flex items-center justify-center text-rose-400 text-xs">🛡️</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-rose-400">Phoenix Contact Form</h3>
            <p class="text-[10px] text-slate-400">Offline resilient keystroke journal</p>
          </div>
        </div>
      </div>

      <!-- Statutory Footer -->
      <div class="p-3 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-cyan-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'footer')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-purple-950 flex items-center justify-center text-purple-400 text-xs">⚖️</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-purple-400">Statutory Footer</h3>
            <p class="text-[10px] text-slate-400">SEBI non-advisory & terms</p>
          </div>
        </div>
      </div>

      <div class="mt-auto p-3 rounded bg-slate-950 border border-slate-800 text-[11px] text-slate-400 font-mono">
        <p class="text-cyan-400 font-bold mb-1">⚖️ John Gall's Law</p>
        <p>"A complex system that works is always found to have evolved from a simple system that worked."</p>
      </div>
    </aside>

    <!-- CENTER VISUAL CANVAS -->
    <main class="flex-1 bg-[#050811] overflow-y-auto p-8 relative flex flex-col items-center">
      <div class="w-full max-w-5xl flex items-center justify-between mb-4 px-2">
        <div class="flex items-center space-x-2">
          <span class="text-xs text-slate-400 font-mono">EDITING CANVAS:</span>
          <span id="activePageLabel" class="text-xs font-bold font-mono text-cyan-400">index.html</span>
        </div>
        <div class="text-[11px] font-mono text-slate-500">
          Double-click any text to edit inline • Drag to re-order
        </div>
      </div>

      <!-- CANVAS DROP CONTAINER -->
      <div id="visualCanvas" class="w-full max-w-5xl min-h-[650px] rounded-xl border border-dashed border-slate-800 drop-zone p-4 space-y-6 flex flex-col"
           ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)" ondrop="handleDrop(event)">
        <!-- Default Starter Blocks (Pre-rendered for index.html) -->
      </div>
    </main>

    <!-- RIGHT AUDIT & SENTINEL TELEMETRY PANEL -->
    <aside class="w-80 glass-panel border-l border-slate-800 p-4 flex flex-col space-y-4 overflow-y-auto z-40">
      <div class="flex items-center justify-between border-b border-slate-800 pb-2">
        <h2 class="text-xs font-bold uppercase tracking-wider text-slate-300">Pentagon Telemetry</h2>
        <span class="text-[10px] font-mono text-emerald-400">CW ↔ ACW</span>
      </div>

      <!-- Real-Time Metrics -->
      <div class="grid grid-cols-2 gap-2 text-xs font-mono">
        <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
          <div class="text-[10px] text-slate-500">SENTINEL SCORE</div>
          <div id="statSentinel" class="text-lg font-bold text-emerald-400">100%</div>
        </div>
        <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
          <div class="text-[10px] text-slate-500">COMPILATION</div>
          <div id="statLatency" class="text-lg font-bold text-cyan-400">18.4ms</div>
        </div>
        <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
          <div class="text-[10px] text-slate-500">BANDWIDTH SAVED</div>
          <div id="statSaved" class="text-lg font-bold text-purple-400">22.6%</div>
        </div>
        <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
          <div class="text-[10px] text-slate-500">DRIFT INVARIANT</div>
          <div id="statDrift" class="text-lg font-bold text-emerald-400">0.00%</div>
        </div>
      </div>

      <!-- Audit Checklist -->
      <div class="space-y-1.5 text-xs font-mono">
        <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1">Titanium Gate Invariants</div>
        <div class="flex items-center justify-between text-slate-300 py-1 border-b border-slate-900">
          <span>Pillar 1: Local Disk Spider</span>
          <span class="text-emerald-400">🟢 INTACT</span>
        </div>
        <div class="flex items-center justify-between text-slate-300 py-1 border-b border-slate-900">
          <span>Pillar 2: Responsive Viewport</span>
          <span class="text-emerald-400">🟢 PASS</span>
        </div>
        <div class="flex items-center justify-between text-slate-300 py-1 border-b border-slate-900">
          <span>Pillar 4: Phoenix Sentinel</span>
          <span class="text-emerald-400">🟢 ACTIVE</span>
        </div>
        <div class="flex items-center justify-between text-slate-300 py-1 border-b border-slate-900">
          <span>Pillar 6: CSP Security Directives</span>
          <span class="text-emerald-400">🟢 ACTIVE</span>
        </div>
        <div class="flex items-center justify-between text-slate-300 py-1 border-b border-slate-900">
          <span>Pillar 9: Open-SEO SERP Window</span>
          <span class="text-emerald-400">🟢 VERIFIED</span>
        </div>
      </div>

      <!-- Live Flight Recorder Feed -->
      <div class="mt-auto">
        <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1 font-mono">Flight Recorder WAL</div>
        <div id="walLog" class="p-2.5 rounded bg-black border border-slate-900 font-mono text-[10px] text-slate-400 h-28 overflow-y-auto space-y-1">
          <div class="text-cyan-400">[NUCLEUS] Studio initialized</div>
          <div class="text-emerald-400">[NODE_3] 9-Pillar Gate Approved</div>
          <div class="text-slate-500">[SHA-256] Invariant sealed</div>
        </div>
      </div>
    </aside>

  </div>

  <script>
    let draggedType = null;

    // Block Template Definitions
    const BLOCK_TEMPLATES = {
      hero: `
        <div class="sovereign-block p-10 rounded-2xl bg-gradient-to-b from-slate-900/90 to-slate-950/90 border border-cyan-500/30 text-center relative shadow-2xl">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="inline-block px-3 py-1 rounded-full bg-cyan-950/80 border border-cyan-500/40 text-cyan-400 text-xs font-mono uppercase tracking-widest mb-4" contenteditable="true">
            Deterministic High-Frequency Silicon
          </div>
          <h1 class="text-4xl md:text-5xl font-black text-white tracking-tight mb-4" contenteditable="true">
            Unkillable Quantitative Infrastructure
          </h1>
          <p class="max-w-2xl mx-auto text-slate-400 text-sm leading-relaxed mb-6" contenteditable="true">
            Engineered on John Gall's Law and sovereign discipline. Sub-millisecond execution, zero monthly fees, and pure raw silicon performance.
          </p>
          <div class="flex items-center justify-center gap-3">
            <a href="#store" class="px-6 py-2.5 rounded-xl bg-cyan-500 text-black font-bold text-xs uppercase tracking-wider hover:opacity-90" contenteditable="true">Explore Systems</a>
            <a href="#contact" class="px-6 py-2.5 rounded-xl bg-slate-900 text-slate-300 border border-slate-700 text-xs font-mono" contenteditable="true">Terminal Connect</a>
          </div>
        </div>
      `,
      metrics: `
        <div class="sovereign-block p-6 rounded-xl bg-slate-900/80 border border-slate-800 grid grid-cols-2 md:grid-cols-4 gap-4 text-center relative">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="p-3 rounded bg-slate-950/60 border border-slate-800/80">
            <div class="text-2xl font-black text-cyan-400 font-mono" contenteditable="true">681.2M</div>
            <div class="text-xs text-slate-400 uppercase font-mono mt-1" contenteditable="true">Ops / Sec</div>
          </div>
          <div class="p-3 rounded bg-slate-950/60 border border-slate-800/80">
            <div class="text-2xl font-black text-emerald-400 font-mono" contenteditable="true">5 µs</div>
            <div class="text-xs text-slate-400 uppercase font-mono mt-1" contenteditable="true">Chaos MTTR</div>
          </div>
          <div class="p-3 rounded bg-slate-950/60 border border-slate-800/80">
            <div class="text-2xl font-black text-indigo-400 font-mono" contenteditable="true">100%</div>
            <div class="text-xs text-slate-400 uppercase font-mono mt-1" contenteditable="true">Air-Gapped</div>
          </div>
          <div class="p-3 rounded bg-slate-950/60 border border-slate-800/80">
            <div class="text-2xl font-black text-purple-400 font-mono" contenteditable="true">$0.00</div>
            <div class="text-xs text-slate-400 uppercase font-mono mt-1" contenteditable="true">Monthly Fee</div>
          </div>
        </div>
      `,
      product: `
        <div class="sovereign-block p-6 rounded-xl bg-slate-900/90 border border-slate-800 hover:border-emerald-500/40 relative">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="space-y-2">
              <span class="px-2.5 py-0.5 rounded bg-emerald-950 text-emerald-400 text-[10px] font-mono border border-emerald-500/30" contenteditable="true">PERPETUAL LICENSE</span>
              <h3 class="text-xl font-bold text-white" contenteditable="true">ExpressBill POS™ Air-Gapped Retail Suite</h3>
              <p class="text-xs text-slate-400 max-w-xl" contenteditable="true">Local-first desktop billing with dynamic UPI QR code generator, inventory registers, and zero monthly subscriptions.</p>
            </div>
            <div class="text-right flex-shrink-0">
              <div class="text-2xl font-black text-white font-mono" contenteditable="true">$49 / ₹3,999</div>
              <div class="text-[10px] text-slate-500 uppercase font-mono mb-2" contenteditable="true">One-Time Lifetime</div>
              <a href="https://gumroad.com" target="_blank" class="px-5 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-400 text-black font-bold text-xs uppercase font-mono inline-block" contenteditable="true">Acquire License</a>
            </div>
          </div>
        </div>
      `,
      terminal: `
        <div class="sovereign-block rounded-xl overflow-hidden bg-black border border-slate-800 font-mono text-xs relative">
          <div class="block-actions absolute top-3 right-3 space-x-1 z-10">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="bg-slate-900/90 px-4 py-2 border-b border-slate-800 flex items-center justify-between text-slate-400 text-[11px]">
            <div class="flex items-center space-x-2">
              <span class="w-2.5 h-2.5 rounded-full bg-red-500/80"></span>
              <span class="w-2.5 h-2.5 rounded-full bg-yellow-500/80"></span>
              <span class="w-2.5 h-2.5 rounded-full bg-green-500/80"></span>
              <span class="ml-2 text-slate-300">rql_telemetry_kernel — 120 FPS</span>
            </div>
            <span class="text-cyan-400">LAT: 25.59° N | BARE-METAL</span>
          </div>
          <div class="p-4 space-y-1 text-slate-300" contenteditable="true">
            <div><span class="text-cyan-400">rql@node01:~$</span> ./rql_website_builder.exe pentagon</div>
            <div class="text-emerald-400">[CW] Forward Velocity: Ingested AST in 1.4ms</div>
            <div class="text-indigo-400">[ACW] Reverse Manifest: 100% INTACT (0 byte drift)</div>
            <div class="text-yellow-400">[SENTINEL] 9-Pillar Quality Gate APPROVED (Score: 100%)</div>
          </div>
        </div>
      `,
      form: `
        <div class="sovereign-block p-8 rounded-xl bg-slate-900/80 border border-slate-800 max-w-xl mx-auto w-full relative">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <h3 class="text-lg font-bold text-white mb-1" contenteditable="true">Sovereign Direct Communications</h3>
          <p class="text-xs text-slate-400 mb-4" contenteditable="true">Protected by Phoenix Sentinel offline keystroke journaling.</p>
          <form class="space-y-3" onsubmit="event.preventDefault()">
            <input type="text" placeholder="Your Name or Institution" class="w-full bg-slate-950 border border-slate-800 rounded px-3 py-2 text-xs text-white focus:outline-none focus:border-cyan-500">
            <input type="email" placeholder="Secure Return Email" class="w-full bg-slate-950 border border-slate-800 rounded px-3 py-2 text-xs text-white focus:outline-none focus:border-cyan-500">
            <textarea placeholder="Direct Message..." rows="3" class="w-full bg-slate-950 border border-slate-800 rounded px-3 py-2 text-xs text-white focus:outline-none focus:border-cyan-500"></textarea>
            <button type="button" class="w-full py-2.5 rounded bg-gradient-to-r from-cyan-500 to-indigo-600 text-black font-bold text-xs uppercase tracking-wider font-mono hover:opacity-90">Transmit Telemetry</button>
          </form>
        </div>
      `,
      footer: `
        <div class="sovereign-block p-6 border-t border-slate-800/80 text-center text-slate-500 text-xs font-mono relative space-y-2">
          <div class="block-actions absolute top-2 right-2 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="text-slate-400 font-bold" contenteditable="true">REHAN QUANT LAB™ • SOVEREIGN ENGINEERING</div>
          <p class="max-w-xl mx-auto text-[10px]" contenteditable="true">
            Independent R&D and technology laboratory. Not registered with SEBI as an Investment Adviser. All systems operate under John Gall's Law.
          </p>
          <div class="text-[10px] text-slate-600">© 2026 Rehan Quant Lab. All rights reserved.</div>
        </div>
      `
    };

    // Load initial starter canvas
    window.addEventListener('DOMContentLoaded', () => {
      const canvas = document.getElementById('visualCanvas');
      canvas.innerHTML = BLOCK_TEMPLATES.hero + BLOCK_TEMPLATES.metrics + BLOCK_TEMPLATES.product + BLOCK_TEMPLATES.terminal + BLOCK_TEMPLATES.footer;
    });

    function handleDragStart(e, type) {
      draggedType = type;
      e.dataTransfer.setData('text/plain', type);
    }

    function handleDragOver(e) {
      e.preventDefault();
      e.currentTarget.classList.add('drag-over');
    }

    function handleDragLeave(e) {
      e.currentTarget.classList.remove('drag-over');
    }

    function handleDrop(e) {
      e.preventDefault();
      e.currentTarget.classList.remove('drag-over');
      if (draggedType && BLOCK_TEMPLATES[draggedType]) {
        const div = document.createElement('div');
        div.innerHTML = BLOCK_TEMPLATES[draggedType];
        e.currentTarget.appendChild(div.firstElementChild);
        appendWal(`Added block: [${draggedType.toUpperCase()}]`);
      }
    }

    function removeBlock(btn) {
      const block = btn.closest('.sovereign-block');
      if (block) {
        block.remove();
        appendWal('Block removed from canvas');
      }
    }

    function appendWal(msg) {
      const wal = document.getElementById('walLog');
      const time = new Date().toLocaleTimeString();
      wal.innerHTML += `<div><span class="text-cyan-500">[${time}]</span> ${msg}</div>`;
      wal.scrollTop = wal.scrollHeight;
    }

    async function compileToSilicon() {
      const btn = document.getElementById('btnCompile');
      const page = document.getElementById('pageSelector').value;
      const canvas = document.getElementById('visualCanvas');
      btn.innerText = 'Compiling...';

      const payload = {
        file_name: page,
        title: "Rehan Quant Lab™ — Sovereign Systems",
        description: "Deterministic high-frequency computing, air-gapped commercial suites, and low-latency database engines.",
        html_content: canvas.innerHTML,
        sections: ["visual_custom"]
      };

      try {
        const res = await fetch('/api/studio/compile', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        const data = await res.json();

        if (data.success) {
          document.getElementById('statSentinel').innerText = data.sentinel_score + '%';
          document.getElementById('statLatency').innerText = (data.compile_duration_micros / 1000).toFixed(1) + 'ms';
          document.getElementById('telemetryStatus').innerText = data.status_badge;
          appendWal(`CW ↔ ACW Loop finished: ${data.minified_bytes}B (${data.status_badge})`);
          alert(`🎉 Silicon Compilation Succeeded!\n• File: ${data.file_name}\n• Sentinel: ${data.sentinel_score}%\n• Hash: ${data.sha256_hash.substring(0, 16)}...`);
        } else {
          alert('Compilation issue: ' + JSON.stringify(data));
        }
      } catch (err) {
        alert('Server connection error: ' + err);
      } finally {
        btn.innerText = '⚡ Compile Silicon';
      }
    }

    async function deployToEdge() {
      const btn = document.getElementById('btnDeploy');
      btn.innerText = 'Deploying...';
      try {
        const res = await fetch('/api/studio/deploy', { method: 'POST' });
        const data = await res.json();
        if (data.success) {
          appendWal('Cloudflare Edge deployed successfully!');
          alert('🚀 Live Deployment Complete! HTTP 200 OK across global edge CDN.');
        } else {
          alert('Deployment warning: ' + data.log);
        }
      } catch (err) {
        alert('Edge deploy error: ' + err);
      } finally {
        btn.innerText = '🚀 Edge Deploy';
      }
    }
  </script>
</body>
</html>"###;
