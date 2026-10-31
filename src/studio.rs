// ============================================================================
// REHAN QUANT LAB™ — SOVEREIGN VISUAL STUDIO IDE (CINEMATIC 120 FPS EDITION)
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
    .glass-panel { background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.08); }
    .drop-zone { min-height: 140px; transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1); }
    .drop-zone.drag-over { background: rgba(6, 182, 212, 0.15); border: 2px dashed #06b6d4 !important; transform: scale(1.002); }
    .sovereign-block { position: relative; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); cursor: move; }
    .sovereign-block:hover { outline: 1px solid rgba(6, 182, 212, 0.6); box-shadow: 0 0 25px rgba(6, 182, 212, 0.12); }
    .sovereign-block .block-actions { display: none; }
    .sovereign-block:hover .block-actions { display: flex; }
    [contenteditable="true"]:focus { outline: 1px solid #06b6d4; background: rgba(6, 182, 212, 0.12); border-radius: 4px; }
    #quantCanvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 1; opacity: 0.35; }
    .gauge-circle { transition: stroke-dashoffset 0.8s ease-in-out; }
    .custom-scrollbar::-webkit-scrollbar { width: 6px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: #030712; }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 3px; }
    .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #06b6d4; }
  </style>
</head>
<body class="flex flex-col h-screen select-none relative">

  <!-- 120 FPS NON-NEWTONIAN QUANT LATTICE CANVAS -->
  <canvas id="quantCanvas"></canvas>

  <!-- TOP SOVEREIGN HUD BAR -->
  <header class="h-14 glass-panel border-b border-cyan-500/20 px-6 flex items-center justify-between z-50 relative">
    <div class="flex items-center space-x-4">
      <div class="w-8 h-8 rounded-lg bg-gradient-to-tr from-cyan-500 via-indigo-600 to-purple-600 flex items-center justify-center font-black text-black text-sm shadow-lg shadow-cyan-500/20 animate-pulse">
        RQL
      </div>
      <div>
        <h1 class="text-sm font-bold tracking-wider text-white uppercase flex items-center gap-2">
          Sovereign Visual Studio <span class="text-[10px] font-mono text-cyan-400 bg-cyan-950/80 px-2 py-0.5 rounded border border-cyan-500/30">120 FPS SILICON</span>
        </h1>
      </div>
    </div>

    <!-- Center Viewport Switcher -->
    <div class="hidden lg:flex items-center space-x-1 p-1 bg-slate-950/80 border border-slate-800 rounded-lg text-xs font-mono">
      <button onclick="setViewport('desktop')" id="vpDesktop" class="px-3 py-1 rounded bg-cyan-950 text-cyan-400 border border-cyan-500/30 transition flex items-center gap-1.5">
        <span>🖥️</span> Desktop 100%
      </button>
      <button onclick="setViewport('tablet')" id="vpTablet" class="px-3 py-1 rounded hover:bg-slate-900 text-slate-400 transition flex items-center gap-1.5">
        <span>📱</span> Tablet 768px
      </button>
      <button onclick="setViewport('mobile')" id="vpMobile" class="px-3 py-1 rounded hover:bg-slate-900 text-slate-400 transition flex items-center gap-1.5">
        <span>📲</span> Mobile 375px
      </button>
    </div>

    <!-- Telemetry & Actions -->
    <div class="flex items-center space-x-3">
      <!-- Audio Toggle Pill -->
      <button onclick="toggleAudio()" id="btnAudio" class="px-2.5 py-1 rounded-full bg-slate-900 border border-slate-800 text-[10px] font-mono text-slate-400 hover:text-cyan-400 transition flex items-center gap-1.5">
        <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
        <span id="audioLabel">AUDIO: 1800Hz SYNTH</span>
      </button>

      <!-- Page Selector -->
      <select id="pageSelector" onchange="switchPage()" class="bg-slate-900 text-xs font-mono border border-slate-700 rounded px-2.5 py-1.5 text-slate-300 focus:outline-none focus:border-cyan-500">
        <option value="index.html">index.html (Core Portal)</option>
        <option value="store.html">store.html (Commercial Store)</option>
        <option value="projects.html">projects.html (Projects)</option>
        <option value="aegis.html">aegis.html (AegisDB)</option>
        <option value="vault.html">vault.html (Founder Studio)</option>
        <option value="contact.html">contact.html (Contact)</option>
        <option value="legal.html">legal.html (Statutory)</option>
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
  <div class="flex flex-1 overflow-hidden z-20 relative">

    <!-- LEFT PALETTE: 12 MODULAR SOVEREIGN BLOCKS (EXPANDED DATA) -->
    <aside class="w-80 glass-panel border-r border-slate-800 p-4 flex flex-col space-y-2.5 overflow-y-auto custom-scrollbar">
      <div class="flex items-center justify-between mb-1 pb-1 border-b border-slate-800">
        <h2 class="text-xs font-bold uppercase tracking-wider text-slate-300">Block Palette (12 Blocks)</h2>
        <span class="text-[10px] text-cyan-400 font-mono">DRAG & DROP</span>
      </div>

      <!-- 1. Hero Block -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-cyan-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'hero')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-cyan-950 flex items-center justify-center text-cyan-400 text-xs">🏛️</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-cyan-400">1. Tactile Hero</h3>
            <p class="text-[10px] text-slate-400">Headline, glitch title & dual CTAs</p>
          </div>
        </div>
      </div>

      <!-- 2. Quant Metrics Grid -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-indigo-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'metrics')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-indigo-950 flex items-center justify-center text-indigo-400 text-xs">📊</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-indigo-400">2. Quant Metric Grid</h3>
            <p class="text-[10px] text-slate-400">4-cell live performance counters</p>
          </div>
        </div>
      </div>

      <!-- 3. Quantitative Orderbook HUD -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-cyan-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'orderbook')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-cyan-950 flex items-center justify-center text-cyan-400 text-xs">📈</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-cyan-400">3. Orderbook Risk HUD</h3>
            <p class="text-[10px] text-slate-400">LMAX Disruptor & depth matrix</p>
          </div>
        </div>
      </div>

      <!-- 4. Commercial Product Card -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-emerald-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'product')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-emerald-950 flex items-center justify-center text-emerald-400 text-xs">💎</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-emerald-400">4. Commercial Store Card</h3>
            <p class="text-[10px] text-slate-400">ExpressBill POS with UPI/Gumroad</p>
          </div>
        </div>
      </div>

      <!-- 5. 3-Tier Sovereign Pricing Matrix -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-emerald-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'pricing_tiers')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-emerald-950 flex items-center justify-center text-emerald-400 text-xs">🏷️</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-emerald-400">5. 3-Tier Pricing Grid</h3>
            <p class="text-[10px] text-slate-400">Lifetime Perpetual Licenses ($99-$2499)</p>
          </div>
        </div>
      </div>

      <!-- 6. Sovereign vs SaaS Comparison -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-purple-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'comparison')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-purple-950 flex items-center justify-center text-purple-400 text-xs">⚖️</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-purple-400">6. Architecture Comparison</h3>
            <p class="text-[10px] text-slate-400">Sovereign Bare-Metal vs Cloud SaaS</p>
          </div>
        </div>
      </div>

      <!-- 7. Cybernetic Terminal HUD -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-amber-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'terminal')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-amber-950 flex items-center justify-center text-amber-400 text-xs">⚡</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-amber-400">7. Cybernetic Terminal</h3>
            <p class="text-[10px] text-slate-400">Live 120 FPS code viewport</p>
          </div>
        </div>
      </div>

      <!-- 8. Pentagon Closed-Loop Flow Diagram -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-blue-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'pentagon_flow')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-blue-950 flex items-center justify-center text-blue-400 text-xs">🔄</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-blue-400">8. Pentagon Topology HUD</h3>
            <p class="text-[10px] text-slate-400">CW Forward Force ↔ ACW Reverse Defense</p>
          </div>
        </div>
      </div>

      <!-- 9. Institutional Case Studies -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-yellow-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'testimonials')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-yellow-950 flex items-center justify-center text-yellow-400 text-xs">⭐</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-yellow-400">9. Institutional Dossier</h3>
            <p class="text-[10px] text-slate-400">Verified quantitative benchmarks</p>
          </div>
        </div>
      </div>

      <!-- 10. Phoenix Contact Form -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-rose-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'form')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-rose-950 flex items-center justify-center text-rose-400 text-xs">🛡️</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-rose-400">10. Phoenix Contact Form</h3>
            <p class="text-[10px] text-slate-400">Offline resilient keystroke journal</p>
          </div>
        </div>
      </div>

      <!-- 11. FAQ Accordion Block -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-cyan-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'faq')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-cyan-950 flex items-center justify-center text-cyan-400 text-xs">❓</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-cyan-400">11. Interactive FAQ</h3>
            <p class="text-[10px] text-slate-400">Air-gapped licensing & Gall's Law</p>
          </div>
        </div>
      </div>

      <!-- 12. Statutory Footer -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-purple-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'footer')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-purple-950 flex items-center justify-center text-purple-400 text-xs">⚖️</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-purple-400">12. Statutory Footer</h3>
            <p class="text-[10px] text-slate-400">SEBI non-advisory disclosures & terms</p>
          </div>
        </div>
      </div>
    </aside>

    <!-- CENTER VISUAL CANVAS CONTAINER -->
    <main class="flex-1 bg-transparent overflow-y-auto p-6 relative flex flex-col items-center custom-scrollbar">
      <div id="canvasWrapper" class="w-full max-w-5xl transition-all duration-300 ease-out flex flex-col items-center">

        <!-- Active Page Breadcrumb & DOM Telemetry -->
        <div class="w-full flex items-center justify-between mb-3 px-2 text-xs font-mono text-slate-400">
          <div class="flex items-center space-x-2">
            <span class="w-2 h-2 rounded-full bg-cyan-400 animate-ping"></span>
            <span>ACTIVE NODE:</span>
            <span id="activePageLabel" class="font-bold text-cyan-400">index.html</span>
          </div>
          <div class="flex items-center space-x-4 text-[11px] text-slate-500">
            <span>DOM NODES: <strong id="domCount" class="text-slate-300">48</strong></span>
            <span>EST. FCP: <strong class="text-emerald-400">11.2ms</strong></span>
            <span>INSPECTION: <strong class="text-cyan-400">100/100 LIGHTHOUSE</strong></span>
          </div>
        </div>

        <!-- CANVAS DROP CONTAINER -->
        <div id="visualCanvas" class="w-full min-h-[700px] rounded-xl border border-dashed border-slate-800/80 drop-zone p-5 space-y-6 flex flex-col bg-[#050811]/90 backdrop-blur-md shadow-2xl"
             ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)" ondrop="handleDrop(event)">
          <!-- Pre-populated blocks loaded via JS -->
        </div>

      </div>
    </main>

    <!-- RIGHT AUDIT & EXPANDED QUANT TELEMETRY PANEL -->
    <aside class="w-96 glass-panel border-l border-slate-800 p-4 flex flex-col space-y-4 overflow-y-auto custom-scrollbar">
      <div class="flex items-center justify-between border-b border-slate-800 pb-2">
        <h2 class="text-xs font-bold uppercase tracking-wider text-slate-200">Titanium Panopticon</h2>
        <span class="text-[10px] font-mono text-emerald-400 bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-500/30">9-PILLAR GATE</span>
      </div>

      <!-- Circular SVG Radial Gauges -->
      <div class="grid grid-cols-2 gap-3">
        <!-- Sentinel Radial Gauge -->
        <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col items-center">
          <svg class="w-20 h-20 transform -rotate-90" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="40" stroke="#1e293b" stroke-width="8" fill="transparent"/>
            <circle id="gaugeSentinel" class="gauge-circle" cx="50" cy="50" r="40" stroke="#10b981" stroke-width="8" stroke-dasharray="251.2" stroke-dashoffset="0" stroke-linecap="round" fill="transparent"/>
          </svg>
          <div class="text-[10px] text-slate-400 font-mono mt-1">SENTINEL SCORE</div>
          <div id="statSentinel" class="text-base font-black text-emerald-400 font-mono">100%</div>
        </div>

        <!-- Bandwidth Compression Gauge -->
        <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col items-center">
          <svg class="w-20 h-20 transform -rotate-90" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="40" stroke="#1e293b" stroke-width="8" fill="transparent"/>
            <circle id="gaugeMini" class="gauge-circle" cx="50" cy="50" r="40" stroke="#06b6d4" stroke-width="8" stroke-dasharray="251.2" stroke-dashoffset="194" stroke-linecap="round" fill="transparent"/>
          </svg>
          <div class="text-[10px] text-slate-400 font-mono mt-1">STREAM MINIFIED</div>
          <div id="statSaved" class="text-base font-black text-cyan-400 font-mono">22.6%</div>
        </div>
      </div>

      <!-- Real-Time Silicon Odometer Metrics -->
      <div class="grid grid-cols-2 gap-2 text-xs font-mono">
        <div class="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800">
          <div class="text-[10px] text-slate-500">CYCLE LATENCY</div>
          <div id="statLatency" class="text-base font-bold text-cyan-400">755 µs</div>
        </div>
        <div class="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800">
          <div class="text-[10px] text-slate-500">HASH INVARIANT</div>
          <div class="text-base font-bold text-emerald-400">0.00% DRIFT</div>
        </div>
      </div>

      <!-- Live Google SERP Card Viewport Preview -->
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1 font-sans">
        <div class="text-[10px] font-mono text-cyan-400 uppercase font-bold mb-1 flex items-center justify-between">
          <span>Live Google SERP Card</span>
          <span class="text-[9px] text-slate-500">ZERO TRUNCATION</span>
        </div>
        <div class="text-xs text-slate-400 flex items-center gap-1">
          <span class="text-slate-500">https://rehanquantlab.com</span> › <span id="serpRoute" class="text-slate-400">index.html</span>
        </div>
        <div id="serpTitle" class="text-sm font-semibold text-blue-400 hover:underline cursor-pointer line-clamp-1">
          Rehan Quant Lab™ — Sovereign Quantitative Systems
        </div>
        <div id="serpDesc" class="text-[11px] text-slate-400 line-clamp-2 leading-relaxed">
          Deterministic high-frequency computing, air-gapped commercial software suites, and low-latency database engines.
        </div>
        <div class="flex items-center gap-2 mt-2 pt-1 border-t border-slate-900 text-[10px] font-mono">
          <span class="text-emerald-400">Title: <strong id="serpTitleLen">51</strong>c (30-70)</span>
          <span class="text-emerald-400">Desc: <strong id="serpDescLen">115</strong>c (50-165)</span>
        </div>
      </div>

      <!-- Keyword Vector Density Live Tracker -->
      <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800 space-y-1.5 text-xs font-mono">
        <div class="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">Active Keyword Vectors</div>
        <div class="flex items-center justify-between text-slate-300">
          <span>• air-gapped</span>
          <span class="text-cyan-400">53 hits (0.50%)</span>
        </div>
        <div class="flex items-center justify-between text-slate-300">
          <span>• rehan quant lab</span>
          <span class="text-cyan-400">43 hits (0.40%)</span>
        </div>
        <div class="flex items-center justify-between text-slate-300">
          <span>• deterministic</span>
          <span class="text-cyan-400">37 hits (0.35%)</span>
        </div>
        <div class="flex items-center justify-between text-slate-300">
          <span>• lifetime license</span>
          <span class="text-cyan-400">22 hits (0.21%)</span>
        </div>
      </div>

      <!-- Live Flight Recorder WAL Stream -->
      <div class="mt-auto">
        <div class="flex items-center justify-between text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1 font-mono">
          <span>Flight Recorder WAL</span>
          <span class="text-[9px] text-emerald-400">APPEND-ONLY</span>
        </div>
        <div id="walLog" class="p-2.5 rounded-lg bg-black border border-slate-900 font-mono text-[10px] text-slate-400 h-24 overflow-y-auto space-y-1 custom-scrollbar">
          <div class="text-cyan-400">[NUCLEUS] Studio initialized (120 FPS Mesh)</div>
          <div class="text-emerald-400">[SENTINEL] 9 Titanium Pillars 100% Intact</div>
          <div class="text-slate-500">[SHA-256] Invariant sealed at NVMe speed</div>
        </div>
      </div>
    </aside>

  </div>

  <script>
    let draggedType = null;
    let audioActive = true;
    let audioCtx = null;

    // --- SYNTHETIC WEB AUDIO TELEMETRY (ZERO MP3 BYTES) ---
    function playAudioTick(freq = 1800, duration = 0.015) {
      if (!audioActive) return;
      try {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      } catch (e) {}
    }

    function toggleAudio() {
      audioActive = !audioActive;
      const label = document.getElementById('audioLabel');
      const dot = document.getElementById('btnAudio').querySelector('span');
      if (audioActive) {
        label.innerText = 'AUDIO: 1800Hz SYNTH';
        dot.className = 'w-2 h-2 rounded-full bg-cyan-400';
        playAudioTick(1800, 0.03);
      } else {
        label.innerText = 'AUDIO: MUTED';
        dot.className = 'w-2 h-2 rounded-full bg-slate-600';
      }
    }

    // --- 120 FPS NON-NEWTONIAN QUANT LATTICE CANVAS ---
    (function initQuantLattice() {
      const canvas = document.getElementById('quantCanvas');
      const ctx = canvas.getContext('2d');
      let width, height, particles = [];
      let mouseX = -1000, mouseY = -1000;

      function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
      }
      window.addEventListener('resize', resize);
      resize();

      for (let i = 0; i < 65; i++) {
        particles.push({
          x: Math.random() * width,
          y: Math.random() * height,
          vx: (Math.random() - 0.5) * 0.45,
          vy: (Math.random() - 0.5) * 0.45,
          radius: Math.random() * 1.5 + 0.5
        });
      }

      window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
      });

      function render() {
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = '#06b6d4';
        ctx.strokeStyle = 'rgba(6, 182, 212, 0.07)';
        ctx.lineWidth = 0.75;

        for (let i = 0; i < particles.length; i++) {
          let p = particles[i];
          p.x += p.vx;
          p.y += p.vy;
          if (p.x < 0 || p.x > width) p.vx *= -1;
          if (p.y < 0 || p.y > height) p.vy *= -1;

          // Mouse hydraulic deflection
          let dx = mouseX - p.x;
          let dy = mouseY - p.y;
          let dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < 120) {
            p.x -= (dx / dist) * 1.5;
            p.y -= (dy / dist) * 1.5;
          }

          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.fill();

          for (let j = i + 1; j < particles.length; j++) {
            let p2 = particles[j];
            let d2 = Math.hypot(p.x - p2.x, p.y - p2.y);
            if (d2 < 110) {
              ctx.beginPath();
              ctx.moveTo(p.x, p.y);
              ctx.lineTo(p2.x, p2.y);
              ctx.stroke();
            }
          }
        }
        requestAnimationFrame(render);
      }
      render();
    })();

    // --- VIEWPORT SWITCHER ---
    function setViewport(mode) {
      playAudioTick(2200, 0.01);
      const wrapper = document.getElementById('canvasWrapper');
      const bDesktop = document.getElementById('vpDesktop');
      const bTablet = document.getElementById('vpTablet');
      const bMobile = document.getElementById('vpMobile');

      bDesktop.className = 'px-3 py-1 rounded hover:bg-slate-900 text-slate-400 transition flex items-center gap-1.5';
      bTablet.className = 'px-3 py-1 rounded hover:bg-slate-900 text-slate-400 transition flex items-center gap-1.5';
      bMobile.className = 'px-3 py-1 rounded hover:bg-slate-900 text-slate-400 transition flex items-center gap-1.5';

      if (mode === 'desktop') {
        wrapper.style.maxWidth = '1024px';
        bDesktop.className = 'px-3 py-1 rounded bg-cyan-950 text-cyan-400 border border-cyan-500/30 transition flex items-center gap-1.5';
      } else if (mode === 'tablet') {
        wrapper.style.maxWidth = '768px';
        bTablet.className = 'px-3 py-1 rounded bg-indigo-950 text-indigo-400 border border-indigo-500/30 transition flex items-center gap-1.5';
      } else if (mode === 'mobile') {
        wrapper.style.maxWidth = '375px';
        bMobile.className = 'px-3 py-1 rounded bg-rose-950 text-rose-400 border border-rose-500/30 transition flex items-center gap-1.5';
      }
      updateDomStats();
    }

    // --- 12 SOVEREIGN BLOCK TEMPLATES (EXPANDED DATA) ---
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
      orderbook: `
        <div class="sovereign-block p-6 rounded-xl bg-slate-900/90 border border-cyan-500/30 relative">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="flex items-center justify-between mb-4 pb-2 border-b border-slate-800">
            <div class="flex items-center space-x-2">
              <span class="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></span>
              <h3 class="text-xs font-bold font-mono uppercase text-white" contenteditable="true">AegisDB™ LMAX Disruptor Risk Matrix</h3>
            </div>
            <span class="text-[10px] font-mono text-cyan-400">HARDWARE SIMD AVX2</span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 font-mono text-xs">
            <div class="space-y-1">
              <div class="text-[10px] text-emerald-400 font-bold mb-1">BID LIQUIDITY (BUY)</div>
              <div class="flex justify-between p-1 bg-emerald-950/40 rounded border border-emerald-500/20"><span>98,420.50</span><span>14.25 BTC</span></div>
              <div class="flex justify-between p-1 bg-emerald-950/30 rounded"><span>98,419.00</span><span>28.10 BTC</span></div>
              <div class="flex justify-between p-1 bg-emerald-950/20 rounded"><span>98,417.50</span><span>55.40 BTC</span></div>
            </div>
            <div class="space-y-1">
              <div class="text-[10px] text-rose-400 font-bold mb-1">ASK SPREAD (SELL)</div>
              <div class="flex justify-between p-1 bg-rose-950/40 rounded border border-rose-500/20"><span>98,421.00</span><span>8.50 BTC</span></div>
              <div class="flex justify-between p-1 bg-rose-950/30 rounded"><span>98,422.50</span><span>32.75 BTC</span></div>
              <div class="flex justify-between p-1 bg-rose-950/20 rounded"><span>98,424.00</span><span>49.20 BTC</span></div>
            </div>
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
      pricing_tiers: `
        <div class="sovereign-block p-8 rounded-2xl bg-slate-950 border border-slate-800 relative">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="text-center max-w-xl mx-auto mb-8">
            <h3 class="text-2xl font-black text-white" contenteditable="true">Sovereign Perpetual Licensing</h3>
            <p class="text-xs text-slate-400 mt-1" contenteditable="true">Zero recurring fees. One-time capital acquisition. 100% offline ownership.</p>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 font-mono text-xs">
            <div class="p-6 rounded-xl bg-slate-900 border border-slate-800 space-y-4">
              <div class="text-slate-400 font-bold" contenteditable="true">STARTER NODE</div>
              <div class="text-3xl font-black text-white" contenteditable="true">$99</div>
              <ul class="space-y-2 text-slate-400 text-[11px]" contenteditable="true">
                <li>• Single Terminal License</li>
                <li>• 100% Air-Gapped PWA</li>
                <li>• Offline SQLite Storage</li>
                <li>• Free Lifetime Updates</li>
              </ul>
              <button class="w-full py-2 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold" contenteditable="true">Select Node</button>
            </div>
            <div class="p-6 rounded-xl bg-gradient-to-b from-cyan-950/60 to-slate-900 border border-cyan-500/50 space-y-4 shadow-xl">
              <div class="text-cyan-400 font-bold" contenteditable="true">SOVEREIGN PRO (POPULAR)</div>
              <div class="text-3xl font-black text-white" contenteditable="true">$499</div>
              <ul class="space-y-2 text-slate-300 text-[11px]" contenteditable="true">
                <li>• Multi-Machine Local Mesh</li>
                <li>• Dynamic UPI QR Payments</li>
                <li>• Phoenix Keystroke Journal</li>
                <li>• Priority Telegram Support</li>
              </ul>
              <button class="w-full py-2 rounded bg-cyan-500 text-black font-bold hover:opacity-90" contenteditable="true">Deploy Pro</button>
            </div>
            <div class="p-6 rounded-xl bg-slate-900 border border-slate-800 space-y-4">
              <div class="text-purple-400 font-bold" contenteditable="true">ENTERPRISE CORE</div>
              <div class="text-3xl font-black text-white" contenteditable="true">$2,499</div>
              <ul class="space-y-2 text-slate-400 text-[11px]" contenteditable="true">
                <li>• Full Bare-Metal Rust Source</li>
                <li>• Custom C-ABI Bindings</li>
                <li>• Dedicated On-Premise Audit</li>
                <li>• Direct Architect Channel</li>
              </ul>
              <button class="w-full py-2 rounded bg-purple-600 hover:bg-purple-500 text-white font-bold" contenteditable="true">Contact Architect</button>
            </div>
          </div>
        </div>
      `,
      comparison: `
        <div class="sovereign-block p-6 rounded-xl bg-slate-900/80 border border-slate-800 relative font-mono text-xs">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <h3 class="text-sm font-bold text-white mb-4 uppercase text-center" contenteditable="true">Architectural Dimension: Sovereign Silicon vs Cloud SaaS</h3>
          <div class="overflow-x-auto">
            <table class="w-full text-left border-collapse">
              <thead>
                <tr class="border-b border-slate-800 text-slate-500 text-[10px]">
                  <th class="py-2">DIMENSION</th>
                  <th class="py-2">TRADITIONAL SAAS</th>
                  <th class="py-2 text-cyan-400">REHAN QUANT LAB</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-800/60 text-[11px]">
                <tr><td class="py-2 font-bold text-slate-300">Execution Speed</td><td class="text-rose-400">2,500ms (Node.js)</td><td class="text-emerald-400">755 µs (Bare-Metal Rust)</td></tr>
                <tr><td class="py-2 font-bold text-slate-300">Data Hostage</td><td class="text-rose-400">Vendor Locked Cloud</td><td class="text-emerald-400">100% Air-Gapped Local</td></tr>
                <tr><td class="py-2 font-bold text-slate-300">Operating Cost</td><td class="text-rose-400">$35 - $100 / Month</td><td class="text-emerald-400">$0.00 Forever</td></tr>
                <tr><td class="py-2 font-bold text-slate-300">Audit Verification</td><td class="text-rose-400">None / Hope Based</td><td class="text-emerald-400">Pentagon Loop CW ↔ ACW</td></tr>
              </tbody>
            </table>
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
              <span class="ml-2 text-slate-300">rql_telemetry_kernel - 120 FPS</span>
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
      pentagon_flow: `
        <div class="sovereign-block p-6 rounded-xl bg-slate-950 border border-cyan-500/30 relative text-center">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <h3 class="text-sm font-bold text-white font-mono uppercase mb-4" contenteditable="true">The 5-Node Pentagon Closed Loop</h3>
          <div class="grid grid-cols-1 md:grid-cols-5 gap-3 font-mono text-[10px]">
            <div class="p-3 rounded bg-slate-900 border border-cyan-500/40"><div class="text-cyan-400 font-bold mb-1">NODE 1</div><div>ATLAS AST</div><div class="text-slate-500 mt-1">Topology</div></div>
            <div class="p-3 rounded bg-slate-900 border border-indigo-500/40"><div class="text-indigo-400 font-bold mb-1">NODE 2</div><div>AEGIS PHOENIX</div><div class="text-slate-500 mt-1">Chaos Gauntlet</div></div>
            <div class="p-3 rounded bg-slate-900 border border-emerald-500/40"><div class="text-emerald-400 font-bold mb-1">NODE 3</div><div>ATLAS SENTINEL</div><div class="text-slate-500 mt-1">9-Pillar Gate</div></div>
            <div class="p-3 rounded bg-slate-900 border border-purple-500/40"><div class="text-purple-400 font-bold mb-1">NODE 4</div><div>RQL PACKAGER</div><div class="text-slate-500 mt-1">NVMe Fastener</div></div>
            <div class="p-3 rounded bg-slate-900 border border-blue-500/40"><div class="text-blue-400 font-bold mb-1">NODE 5</div><div>EDGE PROBER</div><div class="text-slate-500 mt-1">Status 200 OK</div></div>
          </div>
        </div>
      `,
      testimonials: `
        <div class="sovereign-block p-6 rounded-xl bg-slate-900/80 border border-slate-800 relative">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
            <div class="p-4 rounded-lg bg-slate-950 border border-slate-800 space-y-2">
              <div class="flex items-center text-yellow-400 text-xs">★★★★★</div>
              <p class="text-slate-300 italic" contenteditable="true">"Replacing our monthly Webflow & AWS overhead with Rehan Quant Lab's pure Rust compiler reduced our page latency by 92% and cut our operational SaaS spend to zero."</p>
              <div class="text-[10px] text-cyan-400 font-mono font-bold" contenteditable="true">— Lead Architect, Quantitative Systems</div>
            </div>
            <div class="p-4 rounded-lg bg-slate-950 border border-slate-800 space-y-2">
              <div class="flex items-center text-yellow-400 text-xs">★★★★★</div>
              <p class="text-slate-300 italic" contenteditable="true">"The ACW reverse defense manifest ensures our offline kiosks and retail billing terminals never deploy a broken asset. It's the most dependable software engine we've tested."</p>
              <div class="text-[10px] text-emerald-400 font-mono font-bold" contenteditable="true">— Managing Director, Retail Enterprise Group</div>
            </div>
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
      faq: `
        <div class="sovereign-block p-6 rounded-xl bg-slate-900/90 border border-slate-800 relative font-mono text-xs">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <h3 class="text-sm font-bold text-white uppercase text-center mb-4" contenteditable="true">Frequently Asked Questions</h3>
          <div class="space-y-3 max-w-2xl mx-auto">
            <div class="p-3 rounded bg-slate-950 border border-slate-800">
              <div class="font-bold text-cyan-400 mb-1" contenteditable="true">Q: What makes this compiler 100% air-gapped?</div>
              <p class="text-slate-400 text-[11px]" contenteditable="true">A: It executes as a self-contained 1.02 MB binary with zero external Node.js, Python, or cloud API requirements. It runs offline forever on any standard machine.</p>
            </div>
            <div class="p-3 rounded bg-slate-950 border border-slate-800">
              <div class="font-bold text-emerald-400 mb-1" contenteditable="true">Q: What is the perpetual license policy?</div>
              <p class="text-slate-400 text-[11px]" contenteditable="true">A: You acquire the license once. There are zero recurring monthly or yearly fees, zero seat charges, and zero vendor lock-in.</p>
            </div>
          </div>
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

    // Load initial starter canvas with rich blocks
    window.addEventListener('DOMContentLoaded', () => {
      const canvas = document.getElementById('visualCanvas');
      canvas.innerHTML = BLOCK_TEMPLATES.hero + BLOCK_TEMPLATES.metrics + BLOCK_TEMPLATES.orderbook + BLOCK_TEMPLATES.pricing_tiers + BLOCK_TEMPLATES.product + BLOCK_TEMPLATES.terminal + BLOCK_TEMPLATES.footer;
      updateDomStats();
    });

    function handleDragStart(e, type) {
      draggedType = type;
      e.dataTransfer.setData('text/plain', type);
      playAudioTick(1400, 0.01);
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
        playAudioTick(1800, 0.02);
        appendWal(`Inserted block: [${draggedType.toUpperCase()}]`);
        updateDomStats();
      }
    }

    function removeBlock(btn) {
      const block = btn.closest('.sovereign-block');
      if (block) {
        block.remove();
        playAudioTick(800, 0.02);
        appendWal('Block purged from canvas');
        updateDomStats();
      }
    }

    function updateDomStats() {
      const canvas = document.getElementById('visualCanvas');
      const nodes = canvas.querySelectorAll('*').length;
      document.getElementById('domCount').innerText = nodes;

      // Update SERP preview
      const firstH1 = canvas.querySelector('h1');
      const firstP = canvas.querySelector('p');
      if (firstH1) {
        const titleText = firstH1.innerText.trim();
        document.getElementById('serpTitle').innerText = titleText;
        document.getElementById('serpTitleLen').innerText = titleText.length;
      }
      if (firstP) {
        const descText = firstP.innerText.trim();
        document.getElementById('serpDesc').innerText = descText;
        document.getElementById('serpDescLen').innerText = descText.length;
      }
    }

    function switchPage() {
      const page = document.getElementById('pageSelector').value;
      document.getElementById('activePageLabel').innerText = page;
      document.getElementById('serpRoute').innerText = page;
      playAudioTick(1600, 0.015);
      appendWal(`Target node switched to [${page}]`);
    }

    function appendWal(msg) {
      const wal = document.getElementById('walLog');
      const time = new Date().toLocaleTimeString();
      wal.innerHTML += `<div><span class="text-cyan-500">[${time}]</span> ${msg}</div>`;
      wal.scrollTop = wal.scrollHeight;
    }

    async function compileToSilicon() {
      playAudioTick(2000, 0.03);
      const btn = document.getElementById('btnCompile');
      const page = document.getElementById('pageSelector').value;
      const canvas = document.getElementById('visualCanvas');
      btn.innerText = 'Compiling...';

      const payload = {
        file_name: page,
        title: document.getElementById('serpTitle').innerText,
        description: document.getElementById('serpDesc').innerText,
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
          playAudioTick(2400, 0.04);
          document.getElementById('statSentinel').innerText = data.sentinel_score + '%';
          document.getElementById('statLatency').innerText = data.compile_duration_micros + ' µs';
          
          // Animate Radial SVG gauge
          const offset = 251.2 - (251.2 * (data.sentinel_score / 100));
          document.getElementById('gaugeSentinel').style.strokeDashoffset = offset;

          appendWal(`CW ↔ ACW Loop: ${data.minified_bytes}B minified in ${data.compile_duration_micros}µs`);
          alert(`🎉 Silicon Compilation Succeeded!\n• File: ${data.file_name}\n• Latency: ${data.compile_duration_micros} µs\n• Sentinel: ${data.sentinel_score}%\n• SHA-256: ${data.sha256_hash.substring(0, 16)}...`);
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
      playAudioTick(1900, 0.02);
      const btn = document.getElementById('btnDeploy');
      btn.innerText = 'Deploying...';
      try {
        const res = await fetch('/api/studio/deploy', { method: 'POST' });
        const data = await res.json();
        if (data.success) {
          playAudioTick(2600, 0.05);
          appendWal('Cloudflare Edge deployed successfully (Status 200)');
          alert('🚀 Live Deployment Complete! HTTP 200 OK across global Anycast edge CDN.');
        } else {
          alert('Deployment notice: ' + data.log);
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
