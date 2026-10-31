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
    <div class="flex items-center space-x-2.5">
      <!-- 1-Click Sovereign Archetypes Blueprint -->
      <select id="blueprintSelector" onchange="loadBlueprint(this.value)" class="bg-indigo-950/80 hover:bg-indigo-900 text-xs font-mono border border-indigo-500/40 rounded px-2 py-1.5 text-indigo-300 focus:outline-none cursor-pointer">
        <option value="">⚡ Load Archetype Blueprint...</option>
        <option value="quant_fund">🏛️ Quantitative Hedge Fund</option>
        <option value="cyber_secops">🛡️ Cyber Defense & SecOps</option>
        <option value="sovereign_saas">💎 Sovereign Perpetual SaaS</option>
        <option value="local_titan">🏪 High-Conversion Retail & POS</option>
      </select>

      <!-- Leads CRM CSV Export -->
      <a href="/api/leads/export.csv" target="_blank" class="px-2.5 py-1.5 rounded-lg bg-emerald-950/80 hover:bg-emerald-900 text-emerald-400 border border-emerald-500/30 text-xs font-mono transition flex items-center gap-1.5" title="Export Offline WAL Leads as CSV">
        <span>📋</span> Leads CSV
      </a>

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

      <button id="btnCompile" onclick="compileToSilicon()" class="px-3.5 py-1.5 rounded-lg bg-gradient-to-r from-cyan-500 to-blue-600 text-black font-bold text-xs uppercase tracking-wider shadow-lg shadow-cyan-500/25 hover:opacity-90 active:scale-95 transition flex items-center gap-1.5">
        <span>⚡</span> Compile Silicon
      </button>

      <button id="btnDeploy" onclick="deployToEdge()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-400 border border-cyan-500/30 text-xs font-mono uppercase tracking-wider transition flex items-center gap-1.5">
        <span>🚀</span> Edge Deploy
      </button>
    </div>
  </header>

  <!-- MAIN STUDIO WORKSPACE -->
  <div class="flex flex-1 overflow-hidden z-20 relative">

    <!-- LEFT PALETTE: 24 MODULAR SOVEREIGN BLOCKS (EXPANDED DATA) -->
    <aside class="w-80 glass-panel border-r border-slate-800 p-4 flex flex-col space-y-2.5 overflow-y-auto custom-scrollbar">
      <div class="flex items-center justify-between mb-1 pb-1 border-b border-slate-800">
        <h2 class="text-xs font-bold uppercase tracking-wider text-slate-300">Block Palette (24 Blocks)</h2>
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

      <!-- 13. Interactive Quant Financial / Candlestick Chart -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-emerald-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'candlestick')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-emerald-950 flex items-center justify-center text-emerald-400 text-xs">🕯️</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-emerald-400">13. Quant Candlestick Chart</h3>
            <p class="text-[10px] text-slate-400">Live HTML5 canvas finance chart</p>
          </div>
        </div>
      </div>

      <!-- 14. SaaS ROI & Capital Savings Calculator -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-cyan-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'roi_calc')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-cyan-950 flex items-center justify-center text-cyan-400 text-xs">🧮</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-cyan-400">14. Dynamic ROI Calculator</h3>
            <p class="text-[10px] text-slate-400">Interactive SaaS vs Sovereign slider</p>
          </div>
        </div>
      </div>

      <!-- 15. Multi-Language Code Sandbox -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-amber-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'code_tabs')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-amber-950 flex items-center justify-center text-amber-400 text-xs">💻</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-amber-400">15. Multi-Language Code Tabs</h3>
            <p class="text-[10px] text-slate-400">Rust, Python, TS & cURL switcher</p>
          </div>
        </div>
      </div>

      <!-- 16. Bento Grid Feature Matrix -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-blue-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'bento_grid')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-blue-950 flex items-center justify-center text-blue-400 text-xs">🍱</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-blue-400">16. Cyber Bento Grid</h3>
            <p class="text-[10px] text-slate-400">6-cell glassmorphic architecture</p>
          </div>
        </div>
      </div>

      <!-- 17. Cybersecurity Threat Radar -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-rose-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'cyber_radar')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-rose-950 flex items-center justify-center text-rose-400 text-xs">📡</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-rose-400">17. Cyber Threat Radar</h3>
            <p class="text-[10px] text-slate-400">Rotating circular sweep telemetry</p>
          </div>
        </div>
      </div>

      <!-- 18. 4-Stage Execution Pipeline -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-indigo-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'pipeline_steps')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-indigo-950 flex items-center justify-center text-indigo-400 text-xs">⚡</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-indigo-400">18. 4-Stage Laser Pipeline</h3>
            <p class="text-[10px] text-slate-400">Ingest • Quant • Sentinel • Edge</p>
          </div>
        </div>
      </div>

      <!-- 19. Quantitative Fellowship Roster -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-teal-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'team_grid')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-teal-950 flex items-center justify-center text-teal-400 text-xs">👥</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-teal-400">19. Architect & Team Roster</h3>
            <p class="text-[10px] text-slate-400">Founder dossier & verified credentials</p>
          </div>
        </div>
      </div>

      <!-- 20. Enterprise Security Compliance Badges -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-cyan-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'trust_badges')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-cyan-950 flex items-center justify-center text-cyan-400 text-xs">🛡️</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-cyan-400">20. Enterprise Trust Badges</h3>
            <p class="text-[10px] text-slate-400">SOC-2, ISO-27001, OWASP & GDPR</p>
          </div>
        </div>
      </div>

      <!-- 21. Cybernetic VIP Lead Magnet -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-emerald-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'lead_capture')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-emerald-950 flex items-center justify-center text-emerald-400 text-xs">🎯</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-emerald-400">21. VIP Lead Magnet</h3>
            <p class="text-[10px] text-slate-400">Offline WAL-connected lead capture</p>
          </div>
        </div>
      </div>

      <!-- 22. Launch Epoch Countdown HUD -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-yellow-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'countdown_hud')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-yellow-950 flex items-center justify-center text-yellow-400 text-xs">⏱️</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-yellow-400">22. Countdown Epoch HUD</h3>
            <p class="text-[10px] text-slate-400">Live Days : Hours : Mins : Secs clock</p>
          </div>
        </div>
      </div>

      <!-- 23. Sovereign Cyber Video Console -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-purple-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'media_player')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-purple-950 flex items-center justify-center text-purple-400 text-xs">🎬</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-purple-400">23. Cyber Video Console</h3>
            <p class="text-[10px] text-slate-400">Futuristic media player frame</p>
          </div>
        </div>
      </div>

      <!-- 24. Zero-Cookie Sovereign Privacy Ribbon -->
      <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 hover:border-slate-500/50 cursor-grab transition group" draggable="true" ondragstart="handleDragStart(event, 'cookie_banner')">
        <div class="flex items-center space-x-2.5">
          <div class="w-7 h-7 rounded bg-slate-800 flex items-center justify-center text-slate-300 text-xs">🍪</div>
          <div>
            <h3 class="text-xs font-bold text-slate-200 group-hover:text-slate-100">24. Zero-Cookie Ribbon</h3>
            <p class="text-[10px] text-slate-400">Statutory 100% cookie-free banner</p>
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
      `,
      candlestick: `
        <div class="sovereign-block p-6 rounded-xl bg-slate-900/90 border border-emerald-500/30 relative">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="flex items-center justify-between mb-3 pb-2 border-b border-slate-800">
            <div class="flex items-center space-x-2">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
              <h3 class="text-xs font-bold font-mono uppercase text-white" contenteditable="true">High-Frequency Quant Price Action (BTC/USDT)</h3>
            </div>
            <div class="text-[10px] font-mono text-emerald-400">120 FPS SILICON CANVAS • NO EXTERNAL JS</div>
          </div>
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 mb-2 px-1">
            <div>O: <span class="text-white">98,240</span> H: <span class="text-emerald-400">98,920</span> L: <span class="text-rose-400">98,110</span> C: <span class="text-emerald-400 font-bold">98,845</span></div>
            <div>VOL: <span class="text-cyan-400">1,420.8 BTC</span> • RSI: <span class="text-emerald-400">64.2</span></div>
          </div>
          <div class="w-full flex justify-center bg-black/60 rounded-lg p-2 border border-slate-800 overflow-hidden">
            <canvas class="dynamic-candle-canvas w-full h-48" width="680" height="190"></canvas>
          </div>
        </div>
      `,
      roi_calc: `
        <div class="sovereign-block p-8 rounded-2xl bg-gradient-to-b from-slate-900 to-slate-950 border border-cyan-500/30 relative font-mono">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="text-center max-w-xl mx-auto mb-6">
            <span class="text-[10px] uppercase font-bold text-cyan-400 bg-cyan-950/80 px-2.5 py-0.5 rounded-full border border-cyan-500/30">CAPITAL FREEDOM CALCULATOR</span>
            <h3 class="text-xl font-black text-white mt-2" contenteditable="true">Calculate Your 5-Year Cloud SaaS Burn</h3>
            <p class="text-xs text-slate-400 mt-1">See how much capital you incinerate on subscriptions versus acquiring a Sovereign License.</p>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
            <div class="space-y-5 bg-slate-950/70 p-5 rounded-xl border border-slate-800">
              <div>
                <div class="flex justify-between text-xs mb-1">
                  <span class="text-slate-400">Current Monthly SaaS / Cloud Fees:</span>
                  <span class="text-cyan-400 font-bold font-mono" id="valSaasFee">$250 / mo</span>
                </div>
                <input type="range" min="50" max="2500" step="50" value="250" class="w-full accent-cyan-400 cursor-pointer" oninput="calcRoi(this.value, null)">
              </div>
              <div>
                <div class="flex justify-between text-xs mb-1">
                  <span class="text-slate-400">Team / Seat Count:</span>
                  <span class="text-cyan-400 font-bold font-mono" id="valTeamSize">5 Seats</span>
                </div>
                <input type="range" min="1" max="50" step="1" value="5" class="w-full accent-cyan-400 cursor-pointer" oninput="calcRoi(null, this.value)">
              </div>
            </div>
            <div class="bg-slate-950/90 p-6 rounded-xl border border-emerald-500/30 space-y-3 text-center">
              <div class="text-xs text-slate-400 uppercase tracking-wider">5-Year Projected Incineration</div>
              <div class="text-3xl font-black text-rose-500 font-mono line-through" id="burnTotal">$75,000</div>
              <div class="text-xs text-emerald-400 uppercase tracking-wider font-bold">1-Time Sovereign Acquisition</div>
              <div class="text-3xl font-black text-emerald-400 font-mono">$499</div>
              <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/20 text-xs text-emerald-300">
                Net Capital Retained: <strong id="savedTotal" class="font-bold text-white">$74,501</strong>
              </div>
            </div>
          </div>
        </div>
      `,
      code_tabs: `
        <div class="sovereign-block rounded-xl overflow-hidden bg-slate-950 border border-slate-800 font-mono text-xs relative">
          <div class="block-actions absolute top-3 right-3 space-x-1 z-10">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="bg-slate-900 px-4 py-2 border-b border-slate-800 flex items-center justify-between">
            <div class="flex space-x-2">
              <button onclick="switchTab(this, 'cRust')" class="tab-btn px-2.5 py-1 rounded bg-slate-800 text-cyan-400 font-bold text-[11px]">Rust</button>
              <button onclick="switchTab(this, 'cPython')" class="tab-btn px-2.5 py-1 rounded text-slate-400 hover:text-white text-[11px]">Python</button>
              <button onclick="switchTab(this, 'cTs')" class="tab-btn px-2.5 py-1 rounded text-slate-400 hover:text-white text-[11px]">TypeScript</button>
              <button onclick="switchTab(this, 'cCurl')" class="tab-btn px-2.5 py-1 rounded text-slate-400 hover:text-white text-[11px]">cURL</button>
            </div>
            <button onclick="copySnippet(this)" class="text-[10px] bg-slate-800 hover:bg-slate-700 text-slate-300 px-2 py-0.5 rounded transition">Copy Code</button>
          </div>
          <div class="p-4 overflow-x-auto text-[11px] leading-relaxed">
            <pre id="cRust" class="code-pane text-slate-300"><code><span class="text-purple-400">use</span> rql_website_builder::pentagon::PentagonEngine;

<span class="text-cyan-400">fn</span> <span class="text-yellow-400">main</span>() -> <span class="text-emerald-400">Result</span>&lt;(), Box&lt;<span class="text-purple-400">dyn</span> std::error::Error&gt;&gt; {
    <span class="text-slate-500">// CW Forward Propulsion ↔ ACW Reverse Verification</span>
    <span class="text-cyan-400">let</span> engine = PentagonEngine::new(<span class="text-emerald-300">"Deployed_Websites"</span>);
    engine.execute_closed_loop(<span class="text-emerald-300">"rehanquantlab.com"</span>)?;
    <span class="text-cyan-400">println!</span>(<span class="text-emerald-300">"Titanium Sentinel Verified in 755 microseconds!"</span>);
    <span class="text-emerald-400">Ok</span>(())
}</code></pre>
            <pre id="cPython" class="code-pane hidden text-slate-300"><code><span class="text-purple-400">import</span> urllib.request, json

<span class="text-slate-500"># Direct Zero-Cloud Sovereign Telemetry Bridge</span>
req = urllib.request.Request(<span class="text-emerald-300">"http://127.0.0.1:3000/api/studio/compile"</span>, 
    data=json.dumps({<span class="text-emerald-300">"file_name"</span>: <span class="text-emerald-300">"index.html"</span>}).encode(),
    headers={<span class="text-emerald-300">"Content-Type"</span>: <span class="text-emerald-300">"application/json"</span>})
resp = urllib.request.urlopen(req)
print(<span class="text-emerald-300">"Compilation status:"</span>, resp.status)</code></pre>
            <pre id="cTs" class="code-pane hidden text-slate-300"><code><span class="text-purple-400">import</span> { AegisClient } <span class="text-purple-400">from</span> <span class="text-emerald-300">"@rql/sovereign-client"</span>;

<span class="text-cyan-400">const</span> client = <span class="text-cyan-400">new</span> AegisClient({ endpoint: <span class="text-emerald-300">"http://127.0.0.1:3000"</span> });
<span class="text-cyan-400">const</span> status = <span class="text-cyan-400">await</span> client.verifyPentagonLoop();
console.log(<span class="text-emerald-300">`Titanium Score: ${status.score}%`</span>);</code></pre>
            <pre id="cCurl" class="code-pane hidden text-slate-300"><code>curl -s -X POST "http://127.0.0.1:3000/api/studio/compile" \
  -H "Content-Type: application/json" \
  -d '{"file_name":"index.html"}' | jq .</code></pre>
          </div>
        </div>
      `,
      bento_grid: `
        <div class="sovereign-block p-6 rounded-2xl bg-slate-950 border border-slate-800 relative font-mono">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <h3 class="text-sm font-bold text-white uppercase text-center mb-6 tracking-wider" contenteditable="true">Cybernetic Architecture Bento Grid</h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
            <div class="md:col-span-2 p-5 rounded-xl bg-gradient-to-br from-slate-900 to-cyan-950/40 border border-cyan-500/30 flex flex-col justify-between">
              <div>
                <span class="text-[10px] text-cyan-400 uppercase font-bold">CORE VALUE #1</span>
                <h4 class="text-base font-bold text-white mt-1" contenteditable="true">Deterministic Microsecond Latency</h4>
                <p class="text-slate-400 text-[11px] mt-2" contenteditable="true">Compiled to native x86_64/ARM64 machine code with Fat Link-Time Optimization. Zero GC pauses, zero Python runtime overhead.</p>
              </div>
              <div class="mt-4 flex items-center gap-2 text-cyan-300 text-[10px]">
                <span>⚡ AVX2 HARDWARE ACCELERATED</span> • <span>755 µs SYNTHESIS</span>
              </div>
            </div>
            <div class="p-5 rounded-xl bg-slate-900 border border-slate-800 flex flex-col justify-between">
              <div>
                <span class="text-[10px] text-indigo-400 uppercase font-bold">CORE VALUE #2</span>
                <h4 class="text-sm font-bold text-white mt-1" contenteditable="true">Air-Gapped WAL Ledger</h4>
                <p class="text-slate-400 text-[11px] mt-2" contenteditable="true">Append-only crash-resilient write-ahead log. Every edit and compile is hashed and persisted with zero cloud dependency.</p>
              </div>
              <span class="text-[10px] text-indigo-400 mt-3 font-mono">SHA-256 FLIGHT RECORDER</span>
            </div>
            <div class="p-5 rounded-xl bg-slate-900 border border-slate-800 flex flex-col justify-between">
              <div>
                <span class="text-[10px] text-emerald-400 uppercase font-bold">CORE VALUE #3</span>
                <h4 class="text-sm font-bold text-white mt-1" contenteditable="true">RFC IndexNow Broadcaster</h4>
                <p class="text-slate-400 text-[11px] mt-2" contenteditable="true">Instant edge signaling to Bing, Yandex, and Naver search engines within 12 milliseconds of publishing.</p>
              </div>
              <span class="text-[10px] text-emerald-400 mt-3 font-mono">SUB-SECOND SERP BROADCAST</span>
            </div>
            <div class="md:col-span-2 p-5 rounded-xl bg-gradient-to-r from-slate-900 to-indigo-950/40 border border-slate-800 flex flex-col justify-between">
              <div>
                <span class="text-[10px] text-purple-400 uppercase font-bold">CORE VALUE #4</span>
                <h4 class="text-sm font-bold text-white mt-1" contenteditable="true">Perpetual Sovereign Ownership</h4>
                <p class="text-slate-400 text-[11px] mt-2" contenteditable="true">No monthly extortion, no usage limits, no credit card lockouts. The binary belongs to you unconditionally.</p>
              </div>
              <div class="mt-3 flex gap-2 text-[10px] text-slate-400 font-mono">
                <span class="text-purple-300">100% AIR-GAPPED</span> • <span>$0 RECURRING INVOICES</span>
              </div>
            </div>
          </div>
        </div>
      `,
      cyber_radar: `
        <div class="sovereign-block p-6 rounded-2xl bg-slate-950 border border-rose-500/30 relative font-mono text-xs">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="flex items-center justify-between mb-4 pb-2 border-b border-slate-800">
            <div class="flex items-center space-x-2">
              <span class="w-2.5 h-2.5 rounded-full bg-rose-500 animate-ping"></span>
              <h3 class="text-xs font-bold uppercase text-white" contenteditable="true">Zero-Trust Threat Panopticon Radar</h3>
            </div>
            <span class="text-[10px] text-rose-400">ACTIVE REAL-TIME SWEEP</span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
            <div class="flex justify-center">
              <canvas class="dynamic-radar-canvas w-44 h-44 rounded-full bg-slate-950 border border-rose-500/40" width="180" height="180"></canvas>
            </div>
            <div class="space-y-3">
              <div class="p-2.5 rounded bg-slate-900/80 border border-slate-800 flex justify-between items-center">
                <span class="text-slate-400 text-[11px]">DDoS Attacks Mitigated:</span>
                <span class="text-emerald-400 font-bold">48,219 BLOCKED</span>
              </div>
              <div class="p-2.5 rounded bg-slate-900/80 border border-slate-800 flex justify-between items-center">
                <span class="text-slate-400 text-[11px]">Zero-Day Exploit Surface:</span>
                <span class="text-cyan-400 font-bold">0.00% (AIR-GAPPED)</span>
              </div>
              <div class="p-2.5 rounded bg-slate-900/80 border border-slate-800 flex justify-between items-center">
                <span class="text-slate-400 text-[11px]">TLS 1.3 Strict HSTS:</span>
                <span class="text-emerald-400 font-bold">PRELOAD CERTIFIED</span>
              </div>
              <div class="p-2.5 rounded bg-slate-900/80 border border-slate-800 flex justify-between items-center">
                <span class="text-slate-400 text-[11px]">Permissions-Policy:</span>
                <span class="text-white font-bold">CAM=(), MIC=(), GEO=()</span>
              </div>
            </div>
          </div>
        </div>
      `,
      pipeline_steps: `
        <div class="sovereign-block p-6 rounded-xl bg-slate-900/80 border border-indigo-500/30 relative font-mono text-xs">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <h3 class="text-xs font-bold text-white uppercase text-center mb-6 tracking-wider" contenteditable="true">4-Stage Laser Execution Pipeline</h3>
          <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div class="p-4 rounded-lg bg-slate-950 border border-slate-800 text-center space-y-2 relative">
              <div class="w-6 h-6 mx-auto rounded-full bg-cyan-950 text-cyan-400 flex items-center justify-center font-bold text-[10px]">01</div>
              <div class="font-bold text-white text-[11px]" contenteditable="true">Ingest AST</div>
              <p class="text-[10px] text-slate-400" contenteditable="true">Parse raw HTML tags into a lightweight DOM tree in 1.4ms.</p>
            </div>
            <div class="p-4 rounded-lg bg-slate-950 border border-slate-800 text-center space-y-2 relative">
              <div class="w-6 h-6 mx-auto rounded-full bg-indigo-950 text-indigo-400 flex items-center justify-center font-bold text-[10px]">02</div>
              <div class="font-bold text-white text-[11px]" contenteditable="true">Stream Minify</div>
              <p class="text-[10px] text-slate-400" contenteditable="true">1.2 GB/s zero-copy stream compression shaving 22.65% bandwidth.</p>
            </div>
            <div class="p-4 rounded-lg bg-slate-950 border border-slate-800 text-center space-y-2 relative">
              <div class="w-6 h-6 mx-auto rounded-full bg-emerald-950 text-emerald-400 flex items-center justify-center font-bold text-[10px]">03</div>
              <div class="font-bold text-white text-[11px]" contenteditable="true">Titanium Sentinel</div>
              <p class="text-[10px] text-slate-400" contenteditable="true">9-Pillar quality and security gate validating 100/100 integrity.</p>
            </div>
            <div class="p-4 rounded-lg bg-slate-950 border border-slate-800 text-center space-y-2 relative">
              <div class="w-6 h-6 mx-auto rounded-full bg-purple-950 text-purple-400 flex items-center justify-center font-bold text-[10px]">04</div>
              <div class="font-bold text-white text-[11px]" contenteditable="true">Edge Broadcast</div>
              <p class="text-[10px] text-slate-400" contenteditable="true">RFC IndexNow instant push to search engines and Anycast CDN.</p>
            </div>
          </div>
        </div>
      `,
      team_grid: `
        <div class="sovereign-block p-6 rounded-2xl bg-slate-950 border border-slate-800 relative">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="text-center max-w-xl mx-auto mb-6">
            <h3 class="text-lg font-black text-white" contenteditable="true">Architects & Quantitative Fellows</h3>
            <p class="text-xs text-slate-400 mt-1" contenteditable="true">The minds engineering unkillable sovereign infrastructure.</p>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs font-mono">
            <div class="p-4 rounded-xl bg-slate-900 border border-slate-800 text-center space-y-2">
              <div class="w-12 h-12 mx-auto rounded-full bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center text-white font-bold text-sm">MR</div>
              <div class="font-bold text-white text-[11px]" contenteditable="true">Mohammad Rehan</div>
              <div class="text-[10px] text-cyan-400" contenteditable="true">Founder & Principal Systems Architect</div>
              <p class="text-[10px] text-slate-400" contenteditable="true">Bare-metal Rust systems, John Gall's Law, and deterministic HFT engines.</p>
            </div>
            <div class="p-4 rounded-xl bg-slate-900 border border-slate-800 text-center space-y-2">
              <div class="w-12 h-12 mx-auto rounded-full bg-slate-800 flex items-center justify-center text-slate-300 font-bold text-sm">QF</div>
              <div class="font-bold text-white text-[11px]" contenteditable="true">Quantitative Fellow</div>
              <div class="text-[10px] text-indigo-400" contenteditable="true">Stochastic Volatility & Order Flow</div>
              <p class="text-[10px] text-slate-400" contenteditable="true">Sub-millisecond LMAX disruptor ring buffers and market-making risk HUDs.</p>
            </div>
            <div class="p-4 rounded-xl bg-slate-900 border border-slate-800 text-center space-y-2">
              <div class="w-12 h-12 mx-auto rounded-full bg-slate-800 flex items-center justify-center text-slate-300 font-bold text-sm">SE</div>
              <div class="font-bold text-white text-[11px]" contenteditable="true">Security Systems Engineer</div>
              <div class="text-[10px] text-emerald-400" contenteditable="true">Zero-Trust Cryptographic Hardening</div>
              <p class="text-[10px] text-slate-400" contenteditable="true">Air-gapped WAL integrity, SHA-256 seal verification, and OWASP defense.</p>
            </div>
          </div>
        </div>
      `,
      trust_badges: `
        <div class="sovereign-block p-4 rounded-xl bg-slate-950 border border-slate-800/80 relative font-mono text-[11px]">
          <div class="block-actions absolute top-2 right-2 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="flex flex-wrap items-center justify-around gap-4 text-slate-400 text-center">
            <div class="flex items-center space-x-1.5"><span class="text-cyan-400">🛡️</span><span>SOC-2 TYPE II READY</span></div>
            <div class="flex items-center space-x-1.5"><span class="text-emerald-400">🔒</span><span>ISO/IEC 27001</span></div>
            <div class="flex items-center space-x-1.5"><span class="text-indigo-400">⚡</span><span>OWASP TITANIUM CLEARED</span></div>
            <div class="flex items-center space-x-1.5"><span class="text-purple-400">🌐</span><span>100% DATA SOVEREIGNTY</span></div>
            <div class="flex items-center space-x-1.5"><span class="text-rose-400">🚫</span><span>ZERO CLOUD LOCK-IN</span></div>
          </div>
        </div>
      `,
      lead_capture: `
        <div class="sovereign-block p-8 rounded-2xl bg-gradient-to-r from-slate-900 via-indigo-950/40 to-slate-900 border border-indigo-500/40 relative font-mono">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="text-center max-w-xl mx-auto mb-6">
            <span class="text-[10px] uppercase font-bold text-emerald-400 bg-emerald-950/80 px-2.5 py-0.5 rounded-full border border-emerald-500/30">VIP ALPHA ACCESS</span>
            <h3 class="text-2xl font-black text-white mt-2" contenteditable="true">Join the Sovereign Silicon Vanguard</h3>
            <p class="text-xs text-slate-400 mt-1" contenteditable="true">Acquire early releases, raw source distributions, and private quantitative research notes directly to your terminal.</p>
          </div>
          <form class="max-w-md mx-auto space-y-3" onsubmit="handleLeadSubmit(event, this)">
            <input type="text" name="name" required placeholder="Full Name or Institution" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3.5 py-2.5 text-xs text-white focus:outline-none focus:border-cyan-500">
            <input type="email" name="email" required placeholder="Confidential Terminal Email" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3.5 py-2.5 text-xs text-white focus:outline-none focus:border-cyan-500">
            <button type="submit" class="w-full py-3 rounded-lg bg-gradient-to-r from-emerald-500 to-cyan-500 text-black font-bold text-xs uppercase tracking-wider hover:opacity-90 transition shadow-lg shadow-emerald-500/20">
              Request Sovereign Credentials
            </button>
            <div class="lead-success-msg hidden p-2 rounded bg-emerald-950/60 border border-emerald-500/30 text-center text-[11px] text-emerald-300">
              ✅ Lead sealed into Sovereign WAL! Dispatched to offline CRM.
            </div>
          </form>
        </div>
      `,
      countdown_hud: `
        <div class="sovereign-block p-6 rounded-2xl bg-slate-950 border border-yellow-500/30 relative text-center font-mono">
          <div class="block-actions absolute top-3 right-3 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="text-[10px] uppercase tracking-widest text-yellow-400 font-bold mb-2">NEXT SOVEREIGN RELEASE EPOCH</div>
          <h3 class="text-xl font-bold text-white mb-6" contenteditable="true">Genesis Node Alpha 3.0 Deployment</h3>
          <div class="flex justify-center items-center gap-4 text-center">
            <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 min-w-[70px]">
              <div class="text-2xl font-black text-yellow-400" id="cdDays">14</div>
              <div class="text-[9px] text-slate-500 uppercase mt-1">Days</div>
            </div>
            <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 min-w-[70px]">
              <div class="text-2xl font-black text-yellow-400" id="cdHours">08</div>
              <div class="text-[9px] text-slate-500 uppercase mt-1">Hours</div>
            </div>
            <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 min-w-[70px]">
              <div class="text-2xl font-black text-yellow-400" id="cdMins">42</div>
              <div class="text-[9px] text-slate-500 uppercase mt-1">Mins</div>
            </div>
            <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 min-w-[70px]">
              <div class="text-2xl font-black text-yellow-400" id="cdSecs">19</div>
              <div class="text-[9px] text-slate-500 uppercase mt-1">Secs</div>
            </div>
          </div>
        </div>
      `,
      media_player: `
        <div class="sovereign-block rounded-2xl overflow-hidden bg-black border border-purple-500/30 relative font-mono text-xs">
          <div class="block-actions absolute top-3 right-3 space-x-1 z-10">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="aspect-video w-full bg-slate-950 flex flex-col items-center justify-center relative p-8 text-center">
            <div class="w-16 h-16 rounded-full bg-purple-600/30 border border-purple-400 flex items-center justify-center text-white text-xl cursor-pointer hover:scale-110 transition shadow-lg shadow-purple-500/30 mb-4">
              ▶
            </div>
            <h4 class="text-base font-bold text-white tracking-wide" contenteditable="true">Sovereign Silicon Architecture Keynote</h4>
            <p class="text-xs text-slate-400 max-w-md mt-1" contenteditable="true">Watch Founder Mohammad Rehan explain the mathematical destruction of cloud subscription models using John Gall's Law.</p>
            <div class="absolute bottom-3 left-4 flex items-center space-x-2 text-[10px] text-purple-400">
              <span class="w-2 h-2 rounded-full bg-purple-400 animate-pulse"></span>
              <span>4K 120 FPS STREAM • 0 MS BUFFER</span>
            </div>
          </div>
        </div>
      `,
      cookie_banner: `
        <div class="sovereign-block p-4 rounded-xl bg-slate-950 border border-slate-800 flex flex-col md:flex-row items-center justify-between gap-4 font-mono text-xs relative">
          <div class="block-actions absolute top-2 right-2 space-x-1">
            <button onclick="removeBlock(this)" class="px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-500/30 text-xs">Delete</button>
          </div>
          <div class="flex items-center space-x-3">
            <span class="text-xl">🍪</span>
            <div>
              <span class="text-white font-bold" contenteditable="true">100% Zero-Cookie Sovereign Protocol</span>
              <p class="text-[11px] text-slate-400" contenteditable="true">This site operates with 0 surveillance pixels, 0 advertising trackers, and 0 third-party cookies.</p>
            </div>
          </div>
          <div class="flex items-center space-x-2 flex-shrink-0">
            <button class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold text-[10px] uppercase">Acknowledge</button>
          </div>
        </div>
      `
    };

    // Load initial starter canvas with rich blocks
    window.addEventListener('DOMContentLoaded', () => {
      const canvas = document.getElementById('visualCanvas');
      canvas.innerHTML = BLOCK_TEMPLATES.hero + BLOCK_TEMPLATES.metrics + BLOCK_TEMPLATES.orderbook + BLOCK_TEMPLATES.pricing_tiers + BLOCK_TEMPLATES.product + BLOCK_TEMPLATES.terminal + BLOCK_TEMPLATES.footer;
      initDynamicBlocks();
      updateDomStats();
    });

    function loadBlueprint(archetype) {
      if (!archetype) return;
      playAudioTick(2400, 0.04);
      const canvas = document.getElementById('visualCanvas');
      if (archetype === 'quant_fund') {
        canvas.innerHTML = BLOCK_TEMPLATES.hero + BLOCK_TEMPLATES.candlestick + BLOCK_TEMPLATES.metrics + BLOCK_TEMPLATES.orderbook + BLOCK_TEMPLATES.comparison + BLOCK_TEMPLATES.terminal + BLOCK_TEMPLATES.footer;
        appendWal("Loaded Blueprint: [QUANTITATIVE HEDGE FUND]");
      } else if (archetype === 'cyber_secops') {
        canvas.innerHTML = BLOCK_TEMPLATES.hero + BLOCK_TEMPLATES.cyber_radar + BLOCK_TEMPLATES.bento_grid + BLOCK_TEMPLATES.trust_badges + BLOCK_TEMPLATES.pipeline_steps + BLOCK_TEMPLATES.form + BLOCK_TEMPLATES.footer;
        appendWal("Loaded Blueprint: [CYBER DEFENSE & SECOPS]");
      } else if (archetype === 'sovereign_saas') {
        canvas.innerHTML = BLOCK_TEMPLATES.hero + BLOCK_TEMPLATES.bento_grid + BLOCK_TEMPLATES.roi_calc + BLOCK_TEMPLATES.pricing_tiers + BLOCK_TEMPLATES.code_tabs + BLOCK_TEMPLATES.comparison + BLOCK_TEMPLATES.faq + BLOCK_TEMPLATES.footer;
        appendWal("Loaded Blueprint: [SOVEREIGN PERPETUAL SAAS]");
      } else if (archetype === 'local_titan') {
        canvas.innerHTML = BLOCK_TEMPLATES.hero + BLOCK_TEMPLATES.product + BLOCK_TEMPLATES.testimonials + BLOCK_TEMPLATES.form + BLOCK_TEMPLATES.trust_badges + BLOCK_TEMPLATES.footer;
        appendWal("Loaded Blueprint: [RETAIL & LOCAL TITAN]");
      }
      initDynamicBlocks();
      updateDomStats();
      document.getElementById('blueprintSelector').value = "";
    }

    function initDynamicBlocks() {
      // 1. Initialize Candlestick Canvases
      document.querySelectorAll('.dynamic-candle-canvas').forEach(cvs => {
        if (cvs.dataset.init) return;
        cvs.dataset.init = "true";
        const ctx = cvs.getContext('2d');
        const W = cvs.width, H = cvs.height;
        let candles = [];
        let price = 98300;
        for (let i = 0; i < 35; i++) {
          const delta = (Math.random() - 0.48) * 90;
          const open = price;
          const close = price + delta;
          const high = Math.max(open, close) + Math.random() * 40;
          const low = Math.min(open, close) - Math.random() * 40;
          candles.push({ open, close, high, low, vol: Math.random() * 50 + 10 });
          price = close;
        }

        function drawCandles() {
          ctx.clearRect(0, 0, W, H);
          const minP = Math.min(...candles.map(c => c.low)) - 20;
          const maxP = Math.max(...candles.map(c => c.high)) + 20;
          const range = maxP - minP || 1;
          const cW = (W - 20) / candles.length;

          // Draw EMA line
          ctx.beginPath();
          ctx.strokeStyle = '#06b6d4';
          ctx.lineWidth = 1.5;
          candles.forEach((c, idx) => {
            const x = 10 + idx * cW + cW / 2;
            const y = H - 35 - ((c.close - minP) / range) * (H - 55);
            if (idx === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
          });
          ctx.stroke();

          // Draw Candles
          candles.forEach((c, idx) => {
            const x = 10 + idx * cW;
            const isGreen = c.close >= c.open;
            ctx.fillStyle = isGreen ? '#10b981' : '#f43f5e';
            ctx.strokeStyle = ctx.fillStyle;

            const yHigh = H - 35 - ((c.high - minP) / range) * (H - 55);
            const yLow = H - 35 - ((c.low - minP) / range) * (H - 55);
            const yOpen = H - 35 - ((c.open - minP) / range) * (H - 55);
            const yClose = H - 35 - ((c.close - minP) / range) * (H - 55);

            // Wick
            ctx.beginPath();
            ctx.moveTo(x + cW / 2, yHigh);
            ctx.lineTo(x + cW / 2, yLow);
            ctx.lineWidth = 1;
            ctx.stroke();

            // Body
            const top = Math.min(yOpen, yClose);
            const height = Math.max(2, Math.abs(yClose - yOpen));
            ctx.fillRect(x + 2, top, cW - 4, height);

            // Volume bar at bottom
            ctx.globalAlpha = 0.3;
            ctx.fillRect(x + 2, H - (c.vol / 60) * 30, cW - 4, (c.vol / 60) * 30);
            ctx.globalAlpha = 1.0;
          });
        }
        drawCandles();
      });

      // 2. Initialize Threat Radar Canvases
      document.querySelectorAll('.dynamic-radar-canvas').forEach(cvs => {
        if (cvs.dataset.init) return;
        cvs.dataset.init = "true";
        const ctx = cvs.getContext('2d');
        const cx = cvs.width / 2, cy = cvs.height / 2, r = cx - 10;
        let angle = 0;

        function drawRadar() {
          ctx.clearRect(0, 0, cvs.width, cvs.height);
          // Concentric circles
          ctx.strokeStyle = '#3f3f46';
          ctx.lineWidth = 1;
          for (let i = 1; i <= 3; i++) {
            ctx.beginPath();
            ctx.arc(cx, cy, (r / 3) * i, 0, Math.PI * 2);
            ctx.stroke();
          }
          // Crosshairs
          ctx.beginPath();
          ctx.moveTo(cx, cy - r); ctx.lineTo(cx, cy + r);
          ctx.moveTo(cx - r, cy); ctx.lineTo(cx + r, cy);
          ctx.stroke();

          // Sweep line
          ctx.save();
          ctx.translate(cx, cy);
          ctx.rotate(angle);
          const grad = ctx.createLinearGradient(0, 0, r, 0);
          grad.addColorStop(0, 'rgba(244, 63, 94, 0.8)');
          grad.addColorStop(1, 'rgba(244, 63, 94, 0)');
          ctx.fillStyle = grad;
          ctx.beginPath();
          ctx.moveTo(0, 0);
          ctx.arc(0, 0, r, 0, 0.4);
          ctx.closePath();
          ctx.fill();
          ctx.restore();

          angle += 0.04;
          requestAnimationFrame(drawRadar);
        }
        drawRadar();
      });

      // 3. Initialize Countdown Clock
      if (!window.countdownStarted) {
        window.countdownStarted = true;
        let targetSecs = 14 * 86400 + 8 * 3600 + 42 * 60 + 19;
        setInterval(() => {
          targetSecs = Math.max(0, targetSecs - 1);
          const d = Math.floor(targetSecs / 86400);
          const h = Math.floor((targetSecs % 86400) / 3600);
          const m = Math.floor((targetSecs % 3600) / 60);
          const s = targetSecs % 60;
          const elD = document.getElementById('cdDays');
          if (elD) {
            elD.innerText = String(d).padStart(2, '0');
            document.getElementById('cdHours').innerText = String(h).padStart(2, '0');
            document.getElementById('cdMins').innerText = String(m).padStart(2, '0');
            document.getElementById('cdSecs').innerText = String(s).padStart(2, '0');
          }
        }, 1000);
      }
    }

    let currentSaasFee = 250;
    let currentTeamSize = 5;
    function calcRoi(fee, team) {
      if (fee !== null) currentSaasFee = Number(fee);
      if (team !== null) currentTeamSize = Number(team);

      const elValFee = document.getElementById('valSaasFee');
      if (elValFee) elValFee.innerText = '$' + currentSaasFee + ' / mo';
      const elValTeam = document.getElementById('valTeamSize');
      if (elValTeam) elValTeam.innerText = currentTeamSize + ' Seats';

      const fiveYearBurn = currentSaasFee * currentTeamSize * 60;
      const netSaved = Math.max(0, fiveYearBurn - 499);

      const elBurn = document.getElementById('burnTotal');
      if (elBurn) elBurn.innerText = '$' + fiveYearBurn.toLocaleString();
      const elSaved = document.getElementById('savedTotal');
      if (elSaved) elSaved.innerText = '$' + netSaved.toLocaleString();
    }

    function switchTab(btn, codeId) {
      const container = btn.closest('.sovereign-block');
      container.querySelectorAll('.tab-btn').forEach(b => {
        b.className = 'tab-btn px-2.5 py-1 rounded text-slate-400 hover:text-white text-[11px]';
      });
      btn.className = 'tab-btn px-2.5 py-1 rounded bg-slate-800 text-cyan-400 font-bold text-[11px]';
      container.querySelectorAll('.code-pane').forEach(p => p.classList.add('hidden'));
      const activePane = container.querySelector('#' + codeId);
      if (activePane) activePane.classList.remove('hidden');
      playAudioTick(1900, 0.01);
    }

    function copySnippet(btn) {
      const container = btn.closest('.sovereign-block');
      const visibleCode = container.querySelector('.code-pane:not(.hidden)');
      if (visibleCode) {
        navigator.clipboard.writeText(visibleCode.innerText);
        btn.innerText = 'Copied!';
        playAudioTick(2400, 0.02);
        setTimeout(() => btn.innerText = 'Copy Code', 2000);
      }
    }

    async function handleLeadSubmit(e, form) {
      e.preventDefault();
      const name = form.querySelector('[name="name"]').value;
      const email = form.querySelector('[name="email"]').value;
      const submitBtn = form.querySelector('button[type="submit"]');
      submitBtn.innerText = 'Sealing to WAL...';
      playAudioTick(2000, 0.02);

      const payload = {
        timestamp: new Date().toISOString(),
        name: name,
        email: email,
        service: "VIP_ALPHA_INGEST",
        message: "Requested sovereign credentials via Visual Studio Lead Magnet"
      };

      try {
        const res = await fetch('/api/leads/submit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        const data = await res.json();
        if (data.success) {
          playAudioTick(2600, 0.04);
          form.querySelector('.lead-success-msg').classList.remove('hidden');
          submitBtn.innerText = '✓ Credentials Sealed';
          appendWal(`Lead Captured: [${email}] sealed in WAL`);
        }
      } catch (err) {
        alert('Offline WAL capture note: ' + err);
      }
    }

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
        initDynamicBlocks();
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
