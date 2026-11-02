// ============================================================================
// REHAN QUANT LAB™ — SLIDE GENERATOR COMPILER (PRESENTON-CLASS SLIDE ENGINE)
// "Markdown-to-Interactive HTML5/CSS Presentation Deck Compiler"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

use std::fs;
use std::path::Path;

#[derive(Debug, Clone, PartialEq)]
pub enum SlideLayout {
    Title,
    Split,
    Metrics,
    Code,
    Standard,
}

#[derive(Debug, Clone)]
pub struct MetricCard {
    pub value: String,
    pub label: String,
    pub detail: String,
}

#[derive(Debug, Clone)]
pub struct Slide {
    pub index: usize,
    pub title: String,
    pub subtitle: String,
    pub layout: SlideLayout,
    pub body_html: String,
    pub left_html: String,
    pub right_html: String,
    pub code_snippet: Option<(String, String)>, // (language, code)
    pub metrics: Vec<MetricCard>,
    pub notes: String,
}

#[derive(Debug, Clone)]
pub struct PresentationDeck {
    pub title: String,
    pub author: String,
    pub date: String,
    pub theme: String,
    pub slides: Vec<Slide>,
}

pub struct SlideCompiler;

impl SlideCompiler {
    /// Compiles a markdown presentation string into a structured PresentationDeck
    pub fn parse_markdown(input: &str) -> PresentationDeck {
        let mut title = "Software Architecture Presentation".to_string();
        let mut author = "Mohammad Rehan".to_string();
        let mut date = "2026-11-02".to_string();
        let mut theme = "dark".to_string();

        let mut lines = input.lines().peekable();
        let mut content_body = String::new();

        // 1. Check for YAML-like frontmatter
        if let Some(&first_line) = lines.peek() {
            if first_line.trim() == "---" {
                lines.next(); // consume opening ---
                while let Some(line) = lines.next() {
                    let trimmed = line.trim();
                    if trimmed == "---" {
                        break;
                    }
                    if let Some((k, v)) = trimmed.split_once(':') {
                        let key = k.trim().to_lowercase();
                        let val = v.trim().trim_matches('"').trim_matches('\'').to_string();
                        match key.as_str() {
                            "title" => title = val,
                            "author" => author = val,
                            "date" => val_if_not_empty(&mut date, val),
                            "theme" => theme = val,
                            _ => {}
                        }
                    }
                }
            }
        }

        // Collect remaining lines for slide splitting
        for line in lines {
            content_body.push_str(line);
            content_body.push('\n');
        }

        // 2. Split into slides by `\n---\n`
        let raw_slides: Vec<&str> = content_body
            .split("\n---")
            .map(|s| s.trim_start_matches('\n').trim_start_matches("---").trim())
            .filter(|s| !s.is_empty())
            .collect();

        let mut slides = Vec::new();
        for (idx, raw_slide) in raw_slides.into_iter().enumerate() {
            let slide = Self::parse_single_slide(idx + 1, raw_slide);
            slides.push(slide);
        }

        if slides.is_empty() {
            slides.push(Slide {
                index: 1,
                title: title.clone(),
                subtitle: format!("Presented by {}", author),
                layout: SlideLayout::Title,
                body_html: "<p>Architecture overview deck.</p>".to_string(),
                left_html: String::new(),
                right_html: String::new(),
                code_snippet: None,
                metrics: Vec::new(),
                notes: String::new(),
            });
        }

        PresentationDeck {
            title,
            author,
            date,
            theme,
            slides,
        }
    }

    fn parse_single_slide(index: usize, raw: &str) -> Slide {
        let mut title = String::new();
        let mut subtitle = String::new();
        let mut notes = String::new();
        let mut layout = if index == 1 { SlideLayout::Title } else { SlideLayout::Standard };

        let mut body_lines = Vec::new();
        let mut left_lines = Vec::new();
        let mut right_lines = Vec::new();
        let mut current_column: Option<&str> = None; // None, Some("left"), Some("right")

        let mut in_code_block = false;
        let mut code_lang = String::new();
        let mut code_buffer = String::new();
        let mut code_snippet: Option<(String, String)> = None;
        let mut metrics = Vec::new();

        for line in raw.lines() {
            let trimmed = line.trim();

            // Extract layout hint: <!-- layout: split -->
            if trimmed.starts_with("<!--") && trimmed.contains("layout:") {
                if let Some(pos) = trimmed.find("layout:") {
                    let hint = trimmed[pos + 7..].trim_end_matches("-->").trim().to_lowercase();
                    match hint.as_str() {
                        "title" => layout = SlideLayout::Title,
                        "split" => layout = SlideLayout::Split,
                        "metrics" => layout = SlideLayout::Metrics,
                        "code" => layout = SlideLayout::Code,
                        _ => layout = SlideLayout::Standard,
                    }
                }
                continue;
            }

            // Extract notes hint: <!-- notes: ... -->
            if trimmed.starts_with("<!--") && trimmed.contains("notes:") {
                if let Some(pos) = trimmed.find("notes:") {
                    notes = trimmed[pos + 6..].trim_end_matches("-->").trim().to_string();
                }
                continue;
            }

            // Code block handling
            if trimmed.starts_with("```") {
                if in_code_block {
                    in_code_block = false;
                    code_snippet = Some((code_lang.clone(), code_buffer.clone()));
                    code_buffer.clear();
                    if layout == SlideLayout::Standard {
                        layout = SlideLayout::Code;
                    }
                } else {
                    in_code_block = true;
                    code_lang = trimmed.trim_start_matches('`').trim().to_string();
                }
                continue;
            }

            if in_code_block {
                code_buffer.push_str(line);
                code_buffer.push('\n');
                continue;
            }

            // Metric card syntax: [ Value | Label | Detail ]
            if trimmed.starts_with('[') && trimmed.ends_with(']') && trimmed.contains('|') {
                let inner = &trimmed[1..trimmed.len() - 1];
                let parts: Vec<&str> = inner.split('|').map(|s| s.trim()).collect();
                if parts.len() >= 2 {
                    metrics.push(MetricCard {
                        value: parts[0].to_string(),
                        label: parts[1].to_string(),
                        detail: parts.get(2).unwrap_or(&"").to_string(),
                    });
                    if layout == SlideLayout::Standard {
                        layout = SlideLayout::Metrics;
                    }
                    continue;
                }
            }

            // Column split syntax: ::: left, ::: right, :::
            if trimmed == "::: left" {
                current_column = Some("left");
                layout = SlideLayout::Split;
                continue;
            } else if trimmed == "::: right" {
                current_column = Some("right");
                layout = SlideLayout::Split;
                continue;
            } else if trimmed == ":::" {
                current_column = None;
                continue;
            }

            // Headers
            if trimmed.starts_with("# ") && title.is_empty() {
                title = trimmed[2..].trim().to_string();
                continue;
            } else if trimmed.starts_with("## ") && subtitle.is_empty() {
                subtitle = trimmed[3..].trim().to_string();
                continue;
            }

            // Content lines
            match current_column {
                Some("left") => left_lines.push(line),
                Some("right") => right_lines.push(line),
                _ => body_lines.push(line),
            }
        }

        let body_html = Self::render_markdown_block(&body_lines.join("\n"));
        let left_html = Self::render_markdown_block(&left_lines.join("\n"));
        let right_html = Self::render_markdown_block(&right_lines.join("\n"));

        Slide {
            index,
            title,
            subtitle,
            layout,
            body_html,
            left_html,
            right_html,
            code_snippet,
            metrics,
            notes,
        }
    }

    fn render_markdown_block(input: &str) -> String {
        let mut html = String::new();
        let mut in_list = false;

        for line in input.lines() {
            let trimmed = line.trim();
            if trimmed.is_empty() {
                if in_list {
                    html.push_str("</ul>\n");
                    in_list = false;
                }
                continue;
            }

            if trimmed.starts_with("- ") || trimmed.starts_with("* ") {
                if !in_list {
                    html.push_str("<ul class=\"slide-list\">\n");
                    in_list = true;
                }
                let item = Self::format_inline_spans(&trimmed[2..]);
                html.push_str(&format!("  <li>{}</li>\n", item));
            } else if trimmed.starts_with("### ") {
                if in_list {
                    html.push_str("</ul>\n");
                    in_list = false;
                }
                html.push_str(&format!("<h4 class=\"slide-h4\">{}</h4>\n", Self::format_inline_spans(&trimmed[4..])));
            } else {
                if in_list {
                    html.push_str("</ul>\n");
                    in_list = false;
                }
                html.push_str(&format!("<p class=\"slide-p\">{}</p>\n", Self::format_inline_spans(trimmed)));
            }
        }

        if in_list {
            html.push_str("</ul>\n");
        }

        html
    }

    fn format_inline_spans(text: &str) -> String {
        let mut out = String::with_capacity(text.len() * 2);
        let mut chars = text.chars().peekable();

        while let Some(c) = chars.next() {
            if c == '`' {
                // inline code
                let mut code = String::new();
                while let Some(&next_c) = chars.peek() {
                    chars.next();
                    if next_c == '`' {
                        break;
                    }
                    code.push(next_c);
                }
                out.push_str(&format!("<code class=\"inline-code\">{}</code>", Self::escape_html(&code)));
            } else if c == '*' && chars.peek() == Some(&'*') {
                chars.next(); // second *
                let mut bold = String::new();
                while let Some(&next_c) = chars.peek() {
                    chars.next();
                    if next_c == '*' && chars.peek() == Some(&'*') {
                        chars.next();
                        break;
                    }
                    bold.push(next_c);
                }
                out.push_str(&format!("<strong>{}</strong>", Self::escape_html(&bold)));
            } else {
                match c {
                    '<' => out.push_str("&lt;"),
                    '>' => out.push_str("&gt;"),
                    '&' => out.push_str("&amp;"),
                    '"' => out.push_str("&quot;"),
                    _ => out.push(c),
                }
            }
        }

        out
    }

    fn escape_html(s: &str) -> String {
        s.replace('&', "&amp;")
            .replace('<', "&lt;")
            .replace('>', "&gt;")
            .replace('"', "&quot;")
    }

    /// Compiles the presentation deck into a single standalone HTML5/CSS file
    pub fn compile_to_html(deck: &PresentationDeck) -> String {
        let total_slides = deck.slides.len();
        let mut slides_html = String::new();

        for slide in &deck.slides {
            slides_html.push_str(&Self::render_slide_markup(slide, total_slides));
        }

        format!(r#"<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Presentation Deck</title>
  <meta name="description" content="{title} presentation authored by {author}." />
  <link rel="canonical" href="https://rehanquantlab.com/slides/" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title} — Presentation Deck" />
  <meta property="og:description" content="{title} presentation authored by {author}." />
  <meta property="og:url" content="https://rehanquantlab.com/slides/" />
  <meta property="og:image" content="https://rehanquantlab.com/emblem.jpg" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #090d16;
      --card-bg: rgba(18, 26, 43, 0.85);
      --border: rgba(148, 163, 184, 0.15);
      --accent: #0ea5e9;
      --accent-glow: rgba(14, 165, 233, 0.15);
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --stage-w: 1920px;
      --stage-h: 1080px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
      overflow: hidden;
      width: 100vw;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      user-select: none;
    }}
    #viewport {{
      position: relative;
      width: 100vw;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at 50% 0%, rgba(14, 165, 233, 0.08) 0%, transparent 60%);
    }}
    #stage {{
      position: relative;
      width: var(--stage-w);
      height: var(--stage-h);
      transform-origin: center center;
      background: linear-gradient(180deg, rgba(15, 23, 42, 0.6) 0%, rgba(11, 15, 25, 0.95) 100%);
      border: 1px solid var(--border);
      border-radius: 28px;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.7);
      overflow: hidden;
    }}
    .slide {{
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      padding: 96px 128px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      opacity: 0;
      pointer-events: none;
      transition: opacity 280ms ease, transform 280ms ease;
      transform: scale(0.98);
    }}
    .slide.active {{
      opacity: 1;
      pointer-events: auto;
      transform: scale(1);
    }}
    /* Typography */
    .title-h1 {{
      font-family: 'Outfit', sans-serif;
      font-size: 84px;
      font-weight: 800;
      line-height: 1.05;
      letter-spacing: -0.03em;
      color: #ffffff;
      margin-bottom: 24px;
    }}
    .slide-h2 {{
      font-family: 'Outfit', sans-serif;
      font-size: 54px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #ffffff;
      margin-bottom: 12px;
    }}
    .slide-sub {{
      font-size: 24px;
      color: var(--accent);
      font-weight: 600;
      margin-bottom: 36px;
      font-family: 'JetBrains Mono', monospace;
    }}
    .slide-p {{
      font-size: 26px;
      line-height: 1.6;
      color: var(--text-muted);
      margin-bottom: 24px;
      max-width: 1400px;
    }}
    .slide-list {{
      list-style: none;
      margin-top: 16px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .slide-list li {{
      font-size: 28px;
      color: #e2e8f0;
      line-height: 1.5;
      display: flex;
      align-items: flex-start;
      gap: 16px;
    }}
    .slide-list li::before {{
      content: '■';
      color: var(--accent);
      font-size: 18px;
      margin-top: 6px;
      flex-shrink: 0;
    }}
    .inline-code {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.9em;
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid var(--border);
      color: #38bdf8;
      padding: 4px 10px;
      border-radius: 8px;
    }}
    /* Layouts */
    .layout-split {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 64px;
      align-items: center;
      flex-grow: 1;
    }}
    .layout-metrics {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 40px;
      margin-top: 48px;
    }}
    .metric-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 48px 36px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      backdrop-filter: blur(12px);
    }}
    .metric-value {{
      font-family: 'Outfit', sans-serif;
      font-size: 64px;
      font-weight: 800;
      color: #38bdf8;
      line-height: 1;
    }}
    .metric-label {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 20px;
      font-weight: 700;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .metric-detail {{
      font-size: 18px;
      color: var(--text-muted);
      line-height: 1.4;
    }}
    .code-box {{
      background: #040711;
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 32px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 22px;
      line-height: 1.6;
      color: #cbd5e1;
      overflow-x: auto;
      white-space: pre;
    }}
    .code-box .keyword {{ color: #f43f5e; font-weight: bold; }}
    .code-box .fn {{ color: #38bdf8; }}
    .code-box .str {{ color: #34d399; }}
    /* Header & Footer */
    .slide-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
    }}
    .slide-badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 14px;
      font-weight: 700;
      padding: 6px 16px;
      border-radius: 9999px;
      background: var(--accent-glow);
      border: 1px solid var(--accent);
      color: var(--accent);
    }}
    .slide-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      font-family: 'JetBrains Mono', monospace;
      font-size: 16px;
      color: var(--text-muted);
      border-top: 1px solid var(--border);
      padding-top: 24px;
    }}
    /* HUD Overlay Controls */
    .hud-controls {{
      position: fixed;
      bottom: 24px;
      right: 32px;
      display: flex;
      align-items: center;
      gap: 12px;
      z-index: 100;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border);
      padding: 8px 16px;
      border-radius: 9999px;
    }}
    .hud-btn {{
      background: transparent;
      border: none;
      color: var(--text);
      font-family: 'JetBrains Mono', monospace;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      padding: 6px 10px;
      border-radius: 6px;
      transition: background 150ms;
    }}
    .hud-btn:hover {{ background: rgba(255, 255, 255, 0.1); }}
    .progress-bar {{
      position: fixed;
      bottom: 0; left: 0;
      height: 4px;
      background: linear-gradient(90deg, #0ea5e9, #38bdf8);
      transition: width 200ms ease;
      z-index: 200;
    }}
    /* Grid Overview Modal */
    #grid-overview {{
      position: fixed;
      inset: 0;
      background: rgba(9, 13, 22, 0.96);
      backdrop-filter: blur(16px);
      z-index: 300;
      display: none;
      padding: 64px;
      overflow-y: auto;
    }}
    #grid-overview.active {{ display: block; }}
    .grid-container {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 32px;
      max-width: 1600px;
      margin: 0 auto;
    }}
    .grid-card {{
      aspect-ratio: 16 / 9;
      background: #111827;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
      cursor: pointer;
      transition: transform 150ms, border-color 150ms;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .grid-card:hover {{
      transform: translateY(-4px);
      border-color: var(--accent);
    }}
    .grid-card-num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: var(--accent);
      font-weight: bold;
    }}
    .grid-card-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 18px;
      font-weight: 700;
      color: #fff;
    }}
    /* Print Stylesheet for High-Resolution PDF */
    @media print {{
      body {{ background: #fff !important; overflow: visible !important; }}
      #viewport {{ display: block !important; height: auto !important; }}
      #stage {{
        width: 100% !important;
        height: auto !important;
        transform: none !important;
        box-shadow: none !important;
        border: none !important;
        background: none !important;
      }}
      .slide {{
        position: relative !important;
        opacity: 1 !important;
        transform: none !important;
        pointer-events: auto !important;
        page-break-after: always !important;
        page-break-inside: avoid !important;
        height: 100vh !important;
        color: #0f172a !important;
      }}
      .title-h1, .slide-h2, .metric-label {{ color: #0f172a !important; }}
      .slide-p, .slide-list li {{ color: #334155 !important; }}
      .metric-card {{ background: #f8fafc !important; border: 1px solid #cbd5e1 !important; }}
      .code-box {{ background: #f1f5f9 !important; color: #0f172a !important; }}
      .hud-controls, .progress-bar, #grid-overview {{ display: none !important; }}
    }}
  </style>
</head>
<body>
  <div id="viewport">
    <div id="stage">
      {slides_html}
    </div>
  </div>

  <div class="progress-bar" id="progress"></div>

  <div class="hud-controls">
    <button class="hud-btn" id="btn-prev" title="Previous Slide (← / Backspace)">◀</button>
    <span class="hud-btn" id="hud-counter">1 / {total_slides}</span>
    <button class="hud-btn" id="btn-next" title="Next Slide (→ / Space)">▶</button>
    <button class="hud-btn" id="btn-grid" title="Overview Grid (O / Esc)">Grid</button>
    <button class="hud-btn" id="btn-fs" title="Fullscreen (F)">FS</button>
  </div>

  <!-- Grid Overview Mode -->
  <div id="grid-overview">
    <div style="max-width: 1600px; margin: 0 auto 32px; display: flex; justify-content: space-between; align-items: center;">
      <h2 style="font-family: 'Outfit', sans-serif; font-size: 32px; color: #fff;">Slide Index Overview</h2>
      <button class="hud-btn" id="btn-close-grid" style="font-size: 18px; padding: 8px 18px;">Close (Esc)</button>
    </div>
    <div class="grid-container" id="grid-container"></div>
  </div>

  <script>
    (function() {{
      const totalSlides = {total_slides};
      let currentSlide = 0;

      // 1. Viewport Transform Scale Engine
      function updateScale() {{
        const stage = document.getElementById('stage');
        const w = window.innerWidth;
        const h = window.innerHeight;
        // Compute scale factor with uniform aspect ratio preservation
        const scale = Math.min((w - 32) / 1920, (h - 32) / 1080);
        stage.style.transform = `scale(${{scale}})`;
      }}
      window.addEventListener('resize', updateScale);
      updateScale();

      // 2. Slide Navigation State Machine
      const slides = Array.from(document.querySelectorAll('.slide'));
      const counter = document.getElementById('hud-counter');
      const progress = document.getElementById('progress');

      function goToSlide(idx) {{
        if (idx < 0) idx = 0;
        if (idx >= totalSlides) idx = totalSlides - 1;
        currentSlide = idx;

        slides.forEach((s, i) => {{
          if (i === currentSlide) {{
            s.classList.add('active');
          }} else {{
            s.classList.remove('active');
          }}
        }});

        counter.textContent = `${{currentSlide + 1}} / ${{totalSlides}}`;
        progress.style.width = `${{((currentSlide + 1) / totalSlides) * 100}}%`;
        window.location.hash = `#slide-${{currentSlide + 1}}`;
      }}

      // Check hash on load
      const hashMatch = window.location.hash.match(/#slide-(\d+)/);
      if (hashMatch) {{
        const target = parseInt(hashMatch[1], 10) - 1;
        if (target >= 0 && target < totalSlides) {{
          goToSlide(target);
        }} else {{
          goToSlide(0);
        }}
      }} else {{
        goToSlide(0);
      }}

      // 3. Keyboard Controller
      window.addEventListener('keydown', (e) => {{
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
          goToSlide(currentSlide + 1);
        }} else if (e.key === 'ArrowLeft' || e.key === 'Backspace' || e.key === 'PageUp') {{
          goToSlide(currentSlide - 1);
        }} else if (e.key === 'Home') {{
          goToSlide(0);
        }} else if (e.key === 'End') {{
          goToSlide(totalSlides - 1);
        }} else if (e.key === 'f' || e.key === 'F') {{
          toggleFullscreen();
        }} else if (e.key === 'o' || e.key === 'O' || e.key === 'Escape') {{
          toggleGrid();
        }}
      }});

      // 4. Touch Navigation (Swipe gestures)
      let touchStartX = 0;
      window.addEventListener('touchstart', (e) => {{
        touchStartX = e.changedTouches[0].screenX;
      }}, false);
      window.addEventListener('touchend', (e) => {{
        const deltaX = e.changedTouches[0].screenX - touchStartX;
        if (deltaX < -50) goToSlide(currentSlide + 1);
        if (deltaX > 50) goToSlide(currentSlide - 1);
      }}, false);

      // HUD Click events
      document.getElementById('btn-prev').addEventListener('click', () => goToSlide(currentSlide - 1));
      document.getElementById('btn-next').addEventListener('click', () => goToSlide(currentSlide + 1));
      document.getElementById('btn-fs').addEventListener('click', toggleFullscreen);

      function toggleFullscreen() {{
        if (!document.fullscreenElement) {{
          document.documentElement.requestFullscreen().catch(() => {{}});
        }} else {{
          document.exitFullscreen().catch(() => {{}});
        }}
      }}

      // 5. Grid Overview Mode
      const grid = document.getElementById('grid-overview');
      const gridContainer = document.getElementById('grid-container');

      function buildGrid() {{
        gridContainer.innerHTML = '';
        slides.forEach((s, idx) => {{
          const card = document.createElement('div');
          card.className = 'grid-card';
          const title = s.querySelector('.title-h1, .slide-h2')?.textContent || `Slide ${{idx + 1}}`;
          card.innerHTML = `
            <div class="grid-card-num">SLIDE ${{String(idx + 1).padStart(2, '0')}}</div>
            <div class="grid-card-title">${{title}}</div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #64748b;">${{s.dataset.layout || 'standard'}}</div>
          `;
          card.addEventListener('click', () => {{
            goToSlide(idx);
            toggleGrid();
          }});
          gridContainer.appendChild(card);
        }});
      }}
      buildGrid();

      function toggleGrid() {{
        grid.classList.toggle('active');
      }}
      document.getElementById('btn-grid').addEventListener('click', toggleGrid);
      document.getElementById('btn-close-grid').addEventListener('click', toggleGrid);
    }})();
  </script>
</body>
</html>"#,
            title = Self::escape_html(&deck.title),
            author = Self::escape_html(&deck.author),
            total_slides = total_slides,
            slides_html = slides_html
        )
    }

    fn render_slide_markup(slide: &Slide, total_slides: usize) -> String {
        let layout_attr = match slide.layout {
            SlideLayout::Title => "title",
            SlideLayout::Split => "split",
            SlideLayout::Metrics => "metrics",
            SlideLayout::Code => "code",
            SlideLayout::Standard => "standard",
        };

        let mut inner_content = String::new();

        match slide.layout {
            SlideLayout::Title => {
                inner_content.push_str(&format!(
                    r#"<div style="margin-top: 120px;">
  <h1 class="title-h1">{}</h1>
  <div class="slide-sub">{}</div>
  <div class="slide-p">{}</div>
</div>"#,
                    Self::escape_html(&slide.title),
                    Self::escape_html(&slide.subtitle),
                    slide.body_html
                ));
            }
            SlideLayout::Split => {
                inner_content.push_str(&format!(
                    r#"<div>
  <h2 class="slide-h2">{}</h2>
  <div class="slide-sub">{}</div>
</div>
<div class="layout-split">
  <div>{}</div>
  <div>{}</div>
</div>"#,
                    Self::escape_html(&slide.title),
                    Self::escape_html(&slide.subtitle),
                    slide.left_html,
                    slide.right_html
                ));
            }
            SlideLayout::Metrics => {
                let mut cards_html = String::new();
                for m in &slide.metrics {
                    cards_html.push_str(&format!(
                        r#"<div class="metric-card">
  <div class="metric-value">{}</div>
  <div class="metric-label">{}</div>
  <div class="metric-detail">{}</div>
</div>"#,
                        Self::escape_html(&m.value),
                        Self::escape_html(&m.label),
                        Self::escape_html(&m.detail)
                    ));
                }

                inner_content.push_str(&format!(
                    r#"<div>
  <h2 class="slide-h2">{}</h2>
  <div class="slide-sub">{}</div>
  <div>{}</div>
</div>
<div class="layout-metrics">
  {}
</div>"#,
                    Self::escape_html(&slide.title),
                    Self::escape_html(&slide.subtitle),
                    slide.body_html,
                    cards_html
                ));
            }
            SlideLayout::Code => {
                let (lang, code) = slide
                    .code_snippet
                    .clone()
                    .unwrap_or_else(|| ("rust".to_string(), "// No code provided".to_string()));

                inner_content.push_str(&format!(
                    r#"<div>
  <h2 class="slide-h2">{}</h2>
  <div class="slide-sub">{}</div>
  <div class="slide-p">{}</div>
</div>
<div class="code-box"><div style="color: #64748b; font-size: 14px; margin-bottom: 12px; text-transform: uppercase;">Language: {}</div>{}</div>"#,
                    Self::escape_html(&slide.title),
                    Self::escape_html(&slide.subtitle),
                    slide.body_html,
                    Self::escape_html(&lang),
                    Self::escape_html(&code)
                ));
            }
            SlideLayout::Standard => {
                inner_content.push_str(&format!(
                    r#"<div>
  <h2 class="slide-h2">{}</h2>
  <div class="slide-sub">{}</div>
</div>
<div style="flex-grow: 1;">
  {}
</div>"#,
                    Self::escape_html(&slide.title),
                    Self::escape_html(&slide.subtitle),
                    slide.body_html
                ));
            }
        }

        format!(
            r#"<div class="slide" id="slide-{index}" data-layout="{layout_attr}">
  <div class="slide-header">
    <div class="slide-badge">SLIDE {index:02} / {total_slides:02}</div>
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 14px; color: #64748b;">REHAN QUANT LAB™</div>
  </div>

  {inner_content}

  <div class="slide-footer">
    <div>{title}</div>
    <div>Press Space or ➔ to advance • F for Fullscreen • O for Grid</div>
  </div>
</div>
"#,
            index = slide.index,
            total_slides = total_slides,
            layout_attr = layout_attr,
            inner_content = inner_content,
            title = Self::escape_html(&slide.title)
        )
    }

    /// Compiles a markdown file on disk into an HTML file on disk
    pub fn compile_file(input_file: &Path, output_file: &Path) -> std::io::Result<usize> {
        let content = fs::read_to_string(input_file)?;
        let deck = Self::parse_markdown(&content);
        let slide_count = deck.slides.len();
        let html = Self::compile_to_html(&deck);

        if let Some(parent) = output_file.parent() {
            fs::create_dir_all(parent)?;
        }
        fs::write(output_file, html.as_bytes())?;
        Ok(slide_count)
    }

    /// Generates a master default enterprise presentation markdown string
    pub fn generate_default_deck() -> String {
        r#"---
title: "Rehan Quant Lab Enterprise Architecture"
author: "Mohammad Rehan"
date: "2026-11-02"
theme: "dark"
---
<!-- layout: title -->
# Rehan Quant Lab
## Air-Gapped Desktop Software & Distributed Systems
High-throughput sovereign software suites engineered for offline enterprise compliance, cryptographic immutability, and deterministic low-latency execution.

---
<!-- layout: metrics -->
# Operational Performance
## Deterministic Benchmark Telemetry
Physical measurements recorded on bare-metal x86_64 silicon:

[ <0.01ms | Native C-ABI Latency | Pure-Rust execution without garbage collector jitter ]
[ 100% | Air-Gapped Integrity | Complete isolation with zero telemetry packets ]
[ $199 | Perpetual License | Perpetual license ownership with zero recurring fees ]

---
<!-- layout: split -->
# Flagship Commercial Software
## Verified Production Suites
::: left
### 1. RQL DocumentShield™
- Forensic PDF redaction engine
- Destructive vector & text purge
- Automated SSN, EIN & card scanner
- Court-admissible SHA-256 compliance audit

### 2. RQL WhisperVault™
- Offline voice intelligence & transcription
- Zero external cloud telemetry
- Millisecond word-level subtitle generation (.SRT / .VTT)
::: right
### 3. RQL Sovereign Retail POS™
- High-speed retail billing workstation
- 80mm & 58mm thermal receipt printing
- Double-entry SQLite WAL shift ledger
- Direct WhatsApp digital bill delivery

### 4. RQL Enterprise Core™
- Low-latency risk calculation
- Multi-WAN link bonding engine
- Automated GSTR tax ledger reconciliation
:::

---
<!-- layout: code -->
# Deterministic Process Supervision
## AegisDB Continuous Invariant Verification
```rust
pub struct ProcessSupervisor {
    pub process_id: u32,
    pub max_restarts: u32,
    pub restart_count: u32,
    pub state_hash: [u8; 32],
}

impl ProcessSupervisor {
    pub fn verify_invariants(&self) -> bool {
        // Enforce crash resilience and instant memory restoration
        self.restart_count <= self.max_restarts
    }
}
```

---
<!-- layout: standard -->
# Commercial Licensing Framework
## Perpetual Sovereignty vs. Subscription Fatigue
- **Perpetual Master License**: $199 / ₹16,500 one-time payment.
- **Complete Machine Ownership**: Installs directly on local disk with 0 recurring subscriptions.
- **Offline Integrity**: Operates fully on isolated, air-gapped workstations without network access.
- **Instant Delivery**: Download wizard with signed cryptographic checksums.

---
<!-- layout: title -->
# Conclusion & Briefing
## Rehan Quant Lab Headquarters
Patna, Bihar, India • Direct Founder Contact: +91 7091518548
Official Website: https://rehanquantlab.com
"#
        .to_string()
    }
}

fn val_if_not_empty(target: &mut String, val: String) {
    if !val.is_empty() {
        *target = val;
    }
}
