// ============================================================================
// REHAN QUANT LAB™ — SLIDE GENERATOR COMPILER (PRESENTON-CLASS SLIDE ENGINE)
// "Markdown-to-Interactive HTML5/CSS Presentation Deck Compiler"
// Features: Dual-Screen Presenter Mode, Line Highlighting, Math Formulas,
//           Laser Pointer, Drawing Canvas, Per-Slide Themes & Auto-Play Kiosk.
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
    pub code_snippet: Option<(String, String, Vec<usize>)>, // (language, code, highlighted_lines)
    pub metrics: Vec<MetricCard>,
    pub notes: String,
    pub custom_bg: Option<String>,
    pub theme: Option<String>,
}

#[derive(Debug, Clone)]
pub struct PresentationDeck {
    pub title: String,
    pub author: String,
    pub date: String,
    pub theme: String,
    pub autoplay_sec: u32,
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
        let mut autoplay_sec = 0u32;

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
                            "autoplay" => {
                                autoplay_sec = val.trim_end_matches('s').parse().unwrap_or(0);
                            }
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

        // 2. Split into slides by `\n---`
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
                notes: "Introduction slide".to_string(),
                custom_bg: None,
                theme: None,
            });
        }

        PresentationDeck {
            title,
            author,
            date,
            theme,
            autoplay_sec,
            slides,
        }
    }

    fn parse_single_slide(index: usize, raw: &str) -> Slide {
        let mut title = String::new();
        let mut subtitle = String::new();
        let mut notes = String::new();
        let mut layout = if index == 1 { SlideLayout::Title } else { SlideLayout::Standard };
        let mut custom_bg = None;
        let mut theme = None;

        let mut body_lines = Vec::new();
        let mut left_lines = Vec::new();
        let mut right_lines = Vec::new();
        let mut current_column: Option<&str> = None;

        let mut in_code_block = false;
        let mut code_lang = String::new();
        let mut code_highlights = Vec::new();
        let mut code_buffer = String::new();
        let mut code_snippet: Option<(String, String, Vec<usize>)> = None;
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

            // Extract custom background: <!-- bg: #0f172a --> or <!-- bg: url(...) -->
            if trimmed.starts_with("<!--") && trimmed.contains("bg:") {
                if let Some(pos) = trimmed.find("bg:") {
                    custom_bg = Some(trimmed[pos + 3..].trim_end_matches("-->").trim().to_string());
                }
                continue;
            }

            // Extract custom theme: <!-- theme: light -->
            if trimmed.starts_with("<!--") && trimmed.contains("theme:") {
                if let Some(pos) = trimmed.find("theme:") {
                    theme = Some(trimmed[pos + 6..].trim_end_matches("-->").trim().to_lowercase());
                }
                continue;
            }

            // Code block handling with step line-highlight support: ```rust {2-3,5}
            if trimmed.starts_with("```") {
                if in_code_block {
                    in_code_block = false;
                    code_snippet = Some((code_lang.clone(), code_buffer.clone(), code_highlights.clone()));
                    code_buffer.clear();
                    code_highlights.clear();
                    if layout == SlideLayout::Standard {
                        layout = SlideLayout::Code;
                    }
                } else {
                    in_code_block = true;
                    let meta = trimmed.trim_start_matches('`').trim();
                    let (lang, highlights) = Self::parse_code_meta(meta);
                    code_lang = lang;
                    code_highlights = highlights;
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
            custom_bg,
            theme,
        }
    }

    /// Parses code metadata like: `rust {2-3,5}`
    fn parse_code_meta(meta: &str) -> (String, Vec<usize>) {
        let mut lang = meta.to_string();
        let mut highlights = Vec::new();

        if let Some(brace_start) = meta.find('{') {
            if let Some(brace_end) = meta.find('}') {
                lang = meta[..brace_start].trim().to_string();
                let spec = &meta[brace_start + 1..brace_end];
                for part in spec.split(',') {
                    let p = part.trim();
                    if let Some((start_s, end_s)) = p.split_once('-') {
                        if let (Ok(s), Ok(e)) = (start_s.trim().parse::<usize>(), end_s.trim().parse::<usize>()) {
                            for i in s..=e {
                                highlights.push(i);
                            }
                        }
                    } else if let Ok(num) = p.parse::<usize>() {
                        highlights.push(num);
                    }
                }
            }
        }

        if lang.is_empty() {
            lang = "rust".to_string();
        }

        (lang, highlights)
    }

    fn render_markdown_block(input: &str) -> String {
        let mut html = String::new();
        let mut in_list = false;
        let mut in_display_math = false;
        let mut display_math_buf = String::new();

        for line in input.lines() {
            let trimmed = line.trim();

            // Display math block: $$ ... $$
            if trimmed.starts_with("$$") {
                if in_display_math {
                    in_display_math = false;
                    let rendered_math = Self::render_math_formula(&display_math_buf);
                    html.push_str(&format!("<div class=\"display-math\">{}</div>\n", rendered_math));
                    display_math_buf.clear();
                } else {
                    if in_list {
                        html.push_str("</ul>\n");
                        in_list = false;
                    }
                    if trimmed.ends_with("$$") && trimmed.len() > 4 {
                        let inner = &trimmed[2..trimmed.len() - 2];
                        let rendered_math = Self::render_math_formula(inner);
                        html.push_str(&format!("<div class=\"display-math\">{}</div>\n", rendered_math));
                    } else {
                        in_display_math = true;
                    }
                }
                continue;
            }

            if in_display_math {
                display_math_buf.push_str(line);
                display_math_buf.push(' ');
                continue;
            }

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
            // Inline math: $ ... $
            if c == '$' {
                let mut math = String::new();
                let mut found_closing = false;
                while let Some(&next_c) = chars.peek() {
                    chars.next();
                    if next_c == '$' {
                        found_closing = true;
                        break;
                    }
                    math.push(next_c);
                }
                if found_closing && !math.is_empty() {
                    out.push_str(&format!("<span class=\"inline-math\">{}</span>", Self::render_math_formula(&math)));
                } else {
                    out.push('$');
                    out.push_str(&Self::escape_html(&math));
                }
            } else if c == '`' {
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

    /// Renders basic mathematical symbols and fractions into clean typography
    fn render_math_formula(raw: &str) -> String {
        let mut s = raw.trim().to_string();

        // Handle \frac{a}{b}
        while let Some(pos) = s.find(r"\frac") {
            if let Some(first_brace) = s[pos..].find('{') {
                let p1 = pos + first_brace;
                if let Some(first_close) = s[p1..].find('}') {
                    let num = &s[p1 + 1..p1 + first_close];
                    let rest = &s[p1 + first_close + 1..];
                    if let Some(sec_brace) = rest.find('{') {
                        let p2 = p1 + first_close + 1 + sec_brace;
                        if let Some(sec_close) = s[p2..].find('}') {
                            let den = &s[p2 + 1..p2 + sec_close];
                            let replacement = format!(
                                r#"<span class="m-frac"><span class="m-num">{}</span><span class="m-den">{}</span></span>"#,
                                num, den
                            );
                            s = format!("{}{}{}", &s[..pos], replacement, &s[p2 + sec_close + 1..]);
                            continue;
                        }
                    }
                }
            }
            break;
        }

        // Common mathematical operator replacements
        s = s.replace(r"\times", "&times;")
            .replace(r"\cdot", "&sdot;")
            .replace(r"\le", "&le;")
            .replace(r"\ge", "&ge;")
            .replace(r"\ne", "&ne;")
            .replace(r"\approx", "&asymp;")
            .replace(r"\to", "&rarr;")
            .replace(r"\sum", "<span class=\"m-sym\">&sum;</span>")
            .replace(r"\int", "<span class=\"m-sym\">&int;</span>")
            .replace(r"\sigma", "<i>&sigma;</i>")
            .replace(r"\pi", "<i>&pi;</i>")
            .replace(r"\alpha", "<i>&alpha;</i>")
            .replace(r"\beta", "<i>&beta;</i>")
            .replace(r"\Delta", "<i>&Delta;</i>")
            .replace(r"\sqrt", "&radic;");

        // Format subscripts and superscripts: x_i -> x<sub>i</sub>, x^2 -> x<sup>2</sup>
        let mut formatted = String::new();
        let mut chars = s.chars().peekable();
        while let Some(c) = chars.next() {
            if c == '_' {
                let mut sub = String::new();
                if chars.peek() == Some(&'{') {
                    chars.next();
                    while let Some(&nc) = chars.peek() {
                        chars.next();
                        if nc == '}' { break; }
                        sub.push(nc);
                    }
                } else if let Some(&nc) = chars.peek() {
                    chars.next();
                    sub.push(nc);
                }
                formatted.push_str(&format!("<sub>{}</sub>", sub));
            } else if c == '^' {
                let mut sup = String::new();
                if chars.peek() == Some(&'{') {
                    chars.next();
                    while let Some(&nc) = chars.peek() {
                        chars.next();
                        if nc == '}' { break; }
                        sup.push(nc);
                    }
                } else if let Some(&nc) = chars.peek() {
                    chars.next();
                    sup.push(nc);
                }
                formatted.push_str(&format!("<sup>{}</sup>", sup));
            } else {
                formatted.push(c);
            }
        }

        formatted
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
    /* Themes */
    .slide.theme-light {{
      background: #f8fafc !important;
      color: #0f172a !important;
    }}
    .slide.theme-light .title-h1, .slide.theme-light .slide-h2 {{ color: #0f172a !important; }}
    .slide.theme-light .slide-p, .slide.theme-light .slide-list li {{ color: #334155 !important; }}
    .slide.theme-light .metric-card {{ background: #ffffff !important; border: 1px solid #cbd5e1 !important; }}
    .slide.theme-light .code-box {{ background: #f1f5f9 !important; color: #0f172a !important; }}

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

    /* Math Formulas */
    .inline-math, .display-math {{
      font-family: 'Cambria Math', 'KaTeX_Math', 'Times New Roman', serif;
      font-style: italic;
      color: #38bdf8;
    }}
    .display-math {{
      font-size: 34px;
      margin: 28px 0;
      padding: 24px 32px;
      background: rgba(14, 165, 233, 0.06);
      border: 1px solid rgba(14, 165, 233, 0.2);
      border-radius: 16px;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
    }}
    .m-frac {{
      display: inline-flex;
      flex-direction: column;
      vertical-align: middle;
      text-align: center;
      padding: 0 4px;
      font-size: 0.9em;
    }}
    .m-num {{ border-bottom: 2px solid #38bdf8; padding-bottom: 2px; }}
    .m-den {{ padding-top: 2px; }}
    .m-sym {{ font-size: 1.25em; font-style: normal; margin: 0 4px; }}

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

    /* Code Box with Line Numbers & Highlighting */
    .code-box {{
      background: #040711;
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 24px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 22px;
      line-height: 1.6;
      color: #cbd5e1;
      overflow-x: auto;
    }}
    .code-line {{
      display: flex;
      padding: 2px 8px;
      border-radius: 6px;
    }}
    .code-line.highlighted {{
      background: rgba(14, 165, 233, 0.2);
      border-left: 4px solid #38bdf8;
      color: #ffffff;
      font-weight: 600;
    }}
    .code-line.dimmed {{
      opacity: 0.45;
    }}
    .line-num {{
      width: 40px;
      color: #475569;
      user-select: none;
      flex-shrink: 0;
      text-align: right;
      padding-right: 16px;
      font-size: 18px;
    }}

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

    /* Laser Pointer & Drawing Canvas */
    #laser-pointer {{
      position: fixed;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: #ef4444;
      box-shadow: 0 0 16px 4px #ef4444, 0 0 32px 8px rgba(239, 68, 68, 0.6);
      pointer-events: none;
      z-index: 10000;
      display: none;
      transform: translate(-50%, -50%);
    }}
    #drawing-canvas {{
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      z-index: 50;
      pointer-events: none;
    }}
    body.drawing-mode #drawing-canvas {{
      pointer-events: auto;
      cursor: crosshair;
    }}

    /* Blackout Overlay */
    #blackout-overlay {{
      position: fixed;
      inset: 0;
      background: #000000;
      z-index: 9999;
      display: none;
    }}
    #blackout-overlay.active {{ display: block; }}

    /* HUD Overlay Controls */
    .hud-controls {{
      position: fixed;
      bottom: 24px;
      right: 32px;
      display: flex;
      align-items: center;
      gap: 8px;
      z-index: 100;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border);
      padding: 8px 14px;
      border-radius: 9999px;
    }}
    .hud-btn {{
      background: transparent;
      border: none;
      color: var(--text);
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      padding: 6px 10px;
      border-radius: 6px;
      transition: background 150ms;
    }}
    .hud-btn:hover, .hud-btn.active {{ background: rgba(255, 255, 255, 0.15); }}
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

    /* Dual-Screen Presenter Mode */
    #presenter-dashboard {{
      display: none;
      position: fixed;
      inset: 0;
      background: #0b0f19;
      z-index: 500;
      padding: 32px;
      flex-direction: column;
      gap: 24px;
    }}
    body.is-presenter #viewport,
    body.is-presenter .hud-controls,
    body.is-presenter .progress-bar {{
      display: none !important;
    }}
    body.is-presenter #presenter-dashboard {{
      display: flex !important;
    }}
    .presenter-topbar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #111827;
      border: 1px solid var(--border);
      padding: 16px 28px;
      border-radius: 16px;
    }}
    .presenter-clock {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 24px;
      font-weight: bold;
      color: #38bdf8;
    }}
    .presenter-grid {{
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 32px;
      flex-grow: 1;
      height: calc(100vh - 140px);
    }}
    .presenter-box {{
      background: #111827;
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}
    .presenter-box-title {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 14px;
      font-weight: bold;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 16px;
    }}
    .notes-content {{
      font-size: 20px;
      line-height: 1.6;
      color: #f1f5f9;
      overflow-y: auto;
      flex-grow: 1;
      white-space: pre-wrap;
    }}

    /* Print Stylesheet for PDF */
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
      .hud-controls, .progress-bar, #grid-overview, #laser-pointer, #presenter-dashboard {{ display: none !important; }}
    }}
  </style>
</head>
<body>
  <div id="laser-pointer"></div>
  <div id="blackout-overlay"></div>

  <div id="viewport">
    <div id="stage">
      <canvas id="drawing-canvas"></canvas>
      {slides_html}
    </div>
  </div>

  <div class="progress-bar" id="progress"></div>

  <!-- Main HUD Controls -->
  <div class="hud-controls">
    <button class="hud-btn" id="btn-prev" title="Previous Slide (← / Backspace)">◀</button>
    <span class="hud-btn" id="hud-counter">1 / {total_slides}</span>
    <button class="hud-btn" id="btn-next" title="Next Slide (→ / Space)">▶</button>
    <button class="hud-btn" id="btn-laser" title="Laser Pointer (L)">Laser</button>
    <button class="hud-btn" id="btn-draw" title="Draw Pen (D)">Draw</button>
    <button class="hud-btn" id="btn-clear" title="Clear Drawing (C)">Clear</button>
    <button class="hud-btn" id="btn-presenter" title="Presenter Dual-Screen View (P)">Speaker</button>
    <button class="hud-btn" id="btn-grid" title="Overview Grid (O / Esc)">Grid</button>
    <button class="hud-btn" id="btn-autoplay" title="Auto-Play Kiosk (A)">Auto: OFF</button>
    <button class="hud-btn" id="btn-fs" title="Fullscreen (F)">FS</button>
  </div>

  <!-- Grid Overview Modal -->
  <div id="grid-overview">
    <div style="max-width: 1600px; margin: 0 auto 32px; display: flex; justify-content: space-between; align-items: center;">
      <h2 style="font-family: 'Outfit', sans-serif; font-size: 32px; color: #fff;">Slide Index Overview</h2>
      <button class="hud-btn" id="btn-close-grid" style="font-size: 18px; padding: 8px 18px;">Close (Esc)</button>
    </div>
    <div class="grid-container" id="grid-container"></div>
  </div>

  <!-- Dual-Screen Presenter Dashboard -->
  <div id="presenter-dashboard">
    <div class="presenter-topbar">
      <div>
        <span style="font-size: 14px; color: #94a3b8; font-family: 'JetBrains Mono', monospace;">SPEAKER VIEW: </span>
        <strong style="color: #fff; font-size: 18px;">{title}</strong>
      </div>
      <div style="display: flex; align-items: center; gap: 24px;">
        <div class="presenter-clock" id="pres-clock">00:00:00</div>
        <div class="presenter-clock" id="pres-timer" style="color: #34d399;">00:00</div>
        <button class="hud-btn" id="pres-reset-timer" style="border: 1px solid var(--border);">Reset Timer</button>
        <span class="hud-btn" id="pres-counter" style="background: rgba(255,255,255,0.1);">1 / {total_slides}</span>
      </div>
    </div>
    <div class="presenter-grid">
      <div class="presenter-box">
        <div class="presenter-box-title">CURRENT SLIDE (AUDIENCE VIEW)</div>
        <div id="pres-current-view" style="flex-grow: 1; position: relative; overflow: hidden; border-radius: 12px; background: #000;"></div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 24px;">
        <div class="presenter-box" style="height: 40%;">
          <div class="presenter-box-title">NEXT SLIDE PREVIEW</div>
          <div id="pres-next-view" style="flex-grow: 1; position: relative; overflow: hidden; border-radius: 12px; background: #000;"></div>
        </div>
        <div class="presenter-box" style="height: 60%;">
          <div class="presenter-box-title">SPEAKER NOTES</div>
          <div class="notes-content" id="pres-notes-content">No notes recorded for this slide.</div>
        </div>
      </div>
    </div>
  </div>

  <script>
    (function() {{
      const totalSlides = {total_slides};
      const initialAutoplaySec = {autoplay_sec};
      let currentSlide = 0;
      let autoplayActive = initialAutoplaySec > 0;
      let autoplayInterval = null;
      let laserActive = false;

      // BroadcastChannel for instant dual-screen multi-window synchronization
      const syncChannel = new BroadcastChannel('rql_slides_sync_channel');

      // 1. Check Presenter View Mode via URL query
      const urlParams = new URLSearchParams(window.location.search);
      const isPresenter = urlParams.get('presenter') === 'true';
      if (isPresenter) {{
        document.body.classList.add('is-presenter');
      }}

      // 2. Viewport Transform Scale Engine
      const stage = document.getElementById('stage');
      function updateScale() {{
        if (isPresenter) return;
        const w = window.innerWidth;
        const h = window.innerHeight;
        const scale = Math.min((w - 32) / 1920, (h - 32) / 1080);
        stage.style.transform = `scale(${{scale}})`;
      }}
      window.addEventListener('resize', updateScale);
      updateScale();

      // 3. Drawing Canvas Setup
      const canvas = document.getElementById('drawing-canvas');
      const ctx = canvas.getContext('2d');
      function resizeCanvas() {{
        canvas.width = 1920;
        canvas.height = 1080;
      }}
      resizeCanvas();

      let drawing = false;
      let lastX = 0;
      let lastY = 0;

      canvas.addEventListener('mousedown', (e) => {{
        if (!document.body.classList.contains('drawing-mode')) return;
        drawing = true;
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        lastX = (e.clientX - rect.left) * scaleX;
        lastY = (e.clientY - rect.top) * scaleY;
      }});

      canvas.addEventListener('mousemove', (e) => {{
        if (!drawing) return;
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        const curX = (e.clientX - rect.left) * scaleX;
        const curY = (e.clientY - rect.top) * scaleY;

        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 5;
        ctx.lineCap = 'round';
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(curX, curY);
        ctx.stroke();

        lastX = curX;
        lastY = curY;
      }});

      window.addEventListener('mouseup', () => drawing = false);

      function clearCanvas() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }}

      // 4. Laser Pointer
      const laserDot = document.getElementById('laser-pointer');
      window.addEventListener('mousemove', (e) => {{
        if (laserActive) {{
          laserDot.style.left = `${{e.clientX}}px`;
          laserDot.style.top = `${{e.clientY}}px`;
        }}
      }});

      function toggleLaser() {{
        laserActive = !laserActive;
        laserDot.style.display = laserActive ? 'block' : 'none';
        document.getElementById('btn-laser').classList.toggle('active', laserActive);
      }}

      function toggleDraw() {{
        document.body.classList.toggle('drawing-mode');
        const active = document.body.classList.contains('drawing-mode');
        document.getElementById('btn-draw').classList.toggle('active', active);
      }}

      function toggleBlackout() {{
        document.getElementById('blackout-overlay').classList.toggle('active');
      }}

      // 5. Slide Navigation State Machine
      const slides = Array.from(document.querySelectorAll('.slide'));
      const counter = document.getElementById('hud-counter');
      const progress = document.getElementById('progress');

      function goToSlide(idx, broadcast = true) {{
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

        if (counter) counter.textContent = `${{currentSlide + 1}} / ${{totalSlides}}`;
        if (progress) progress.style.width = `${{((currentSlide + 1) / totalSlides) * 100}}%`;
        window.location.hash = `#slide-${{currentSlide + 1}}`;

        clearCanvas();

        if (isPresenter) {{
          updatePresenterDashboard();
        }}

        if (broadcast) {{
          syncChannel.postMessage({{ type: 'SLIDE_CHANGE', index: currentSlide }});
        }}
      }}

      // Listen for broadcasts from secondary window
      syncChannel.onmessage = (event) => {{
        if (event.data && event.data.type === 'SLIDE_CHANGE') {{
          goToSlide(event.data.index, false);
        }}
      }};

      // Initial Slide Hash Resolution
      const hashMatch = window.location.hash.match(/#slide-(\d+)/);
      if (hashMatch) {{
        const target = parseInt(hashMatch[1], 10) - 1;
        goToSlide(target >= 0 && target < totalSlides ? target : 0, false);
      }} else {{
        goToSlide(0, false);
      }}

      // 6. Keyboard Controller
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
        }} else if (e.key === 'l' || e.key === 'L') {{
          toggleLaser();
        }} else if (e.key === 'd' || e.key === 'D') {{
          toggleDraw();
        }} else if (e.key === 'c' || e.key === 'C') {{
          clearCanvas();
        }} else if (e.key === 'b' || e.key === 'B') {{
          toggleBlackout();
        }} else if (e.key === 'p' || e.key === 'P') {{
          openPresenterWindow();
        }} else if (e.key === 'a' || e.key === 'A') {{
          toggleAutoplay();
        }}
      }});

      // 7. Touch Navigation
      let touchStartX = 0;
      window.addEventListener('touchstart', (e) => {{
        touchStartX = e.changedTouches[0].screenX;
      }}, false);
      window.addEventListener('touchend', (e) => {{
        const deltaX = e.changedTouches[0].screenX - touchStartX;
        if (deltaX < -50) goToSlide(currentSlide + 1);
        if (deltaX > 50) goToSlide(currentSlide - 1);
      }}, false);

      // HUD Button Events
      document.getElementById('btn-prev')?.addEventListener('click', () => goToSlide(currentSlide - 1));
      document.getElementById('btn-next')?.addEventListener('click', () => goToSlide(currentSlide + 1));
      document.getElementById('btn-fs')?.addEventListener('click', toggleFullscreen);
      document.getElementById('btn-laser')?.addEventListener('click', toggleLaser);
      document.getElementById('btn-draw')?.addEventListener('click', toggleDraw);
      document.getElementById('btn-clear')?.addEventListener('click', clearCanvas);
      document.getElementById('btn-presenter')?.addEventListener('click', openPresenterWindow);
      document.getElementById('btn-autoplay')?.addEventListener('click', toggleAutoplay);

      function toggleFullscreen() {{
        if (!document.fullscreenElement) {{
          document.documentElement.requestFullscreen().catch(() => {{}});
        }} else {{
          document.exitFullscreen().catch(() => {{}});
        }}
      }}

      // 8. Presenter Dual-Screen Window
      function openPresenterWindow() {{
        const url = window.location.pathname + '?presenter=true' + window.location.hash;
        window.open(url, 'rql_presenter_view', 'width=1280,height=800,menubar=no,toolbar=no');
      }}

      // Presenter Dashboard Implementation
      let timerStart = Date.now();
      function updatePresenterDashboard() {{
        const curContainer = document.getElementById('pres-current-view');
        const nextContainer = document.getElementById('pres-next-view');
        const notesBox = document.getElementById('pres-notes-content');
        const presCounter = document.getElementById('pres-counter');

        if (presCounter) presCounter.textContent = `${{currentSlide + 1}} / ${{totalSlides}}`;

        const curSlideEl = slides[currentSlide];
        const nextSlideEl = slides[currentSlide + 1];

        if (curContainer && curSlideEl) {{
          curContainer.innerHTML = curSlideEl.outerHTML;
          const s = curContainer.querySelector('.slide');
          if (s) {{
            s.classList.add('active');
            s.style.position = 'relative';
            s.style.transform = 'scale(0.55)';
            s.style.transformOrigin = 'top left';
            s.style.width = '1920px';
            s.style.height = '1080px';
          }}
        }}

        if (nextContainer) {{
          if (nextSlideEl) {{
            nextContainer.innerHTML = nextSlideEl.outerHTML;
            const s = nextContainer.querySelector('.slide');
            if (s) {{
              s.classList.add('active');
              s.style.position = 'relative';
              s.style.transform = 'scale(0.35)';
              s.style.transformOrigin = 'top left';
              s.style.width = '1920px';
              s.style.height = '1080px';
            }}
          }} else {{
            nextContainer.innerHTML = '<div style="color: #64748b; padding: 24px; font-family: monospace;">[End of Presentation]</div>';
          }}
        }}

        if (notesBox) {{
          const notesText = curSlideEl?.dataset?.notes || 'No speaker notes recorded for this slide.';
          notesBox.textContent = notesText;
        }}
      }}

      if (isPresenter) {{
        // Presenter Clock & Stopwatch
        setInterval(() => {{
          const now = new Date();
          const clockEl = document.getElementById('pres-clock');
          if (clockEl) clockEl.textContent = now.toLocaleTimeString();

          const elapsedSec = Math.floor((Date.now() - timerStart) / 1000);
          const mins = String(Math.floor(elapsedSec / 60)).padStart(2, '0');
          const secs = String(elapsedSec % 60).padStart(2, '0');
          const timerEl = document.getElementById('pres-timer');
          if (timerEl) timerEl.textContent = `${{mins}}:${{secs}}`;
        }}, 1000);

        document.getElementById('pres-reset-timer')?.addEventListener('click', () => {{
          timerStart = Date.now();
        }});

        updatePresenterDashboard();
      }}

      // 9. Auto-Play Timer
      function toggleAutoplay() {{
        autoplayActive = !autoplayActive;
        const btn = document.getElementById('btn-autoplay');
        if (autoplayActive) {{
          if (btn) btn.textContent = 'Auto: ON (8s)';
          autoplayInterval = setInterval(() => {{
            goToSlide((currentSlide + 1) % totalSlides);
          }}, 8000);
        }} else {{
          if (btn) btn.textContent = 'Auto: OFF';
          clearInterval(autoplayInterval);
        }}
      }}
      if (initialAutoplaySec > 0) {{
        toggleAutoplay();
      }}

      // 10. Grid Overview Mode
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
      document.getElementById('btn-grid')?.addEventListener('click', toggleGrid);
      document.getElementById('btn-close-grid')?.addEventListener('click', toggleGrid);
    }})();
  </script>
</body>
</html>"#,
            title = Self::escape_html(&deck.title),
            author = Self::escape_html(&deck.author),
            total_slides = total_slides,
            autoplay_sec = deck.autoplay_sec,
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

        let mut inline_styles = String::new();
        if let Some(bg) = &slide.custom_bg {
            inline_styles.push_str(&format!("background: {};", bg));
        }

        let theme_class = match slide.theme.as_deref() {
            Some("light") => " theme-light",
            _ => "",
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
                let (lang, code, highlights) = slide
                    .code_snippet
                    .clone()
                    .unwrap_or_else(|| ("rust".to_string(), "// No code provided".to_string(), Vec::new()));

                let mut code_lines_html = String::new();
                for (line_idx, line) in code.lines().enumerate() {
                    let line_num = line_idx + 1;
                    let is_highlighted = highlights.contains(&line_num);
                    let class = if highlights.is_empty() {
                        "code-line"
                    } else if is_highlighted {
                        "code-line highlighted"
                    } else {
                        "code-line dimmed"
                    };

                    code_lines_html.push_str(&format!(
                        r#"<div class="{}"><span class="line-num">{}</span><span>{}</span></div>"#,
                        class,
                        line_num,
                        Self::escape_html(line)
                    ));
                }

                inner_content.push_str(&format!(
                    r#"<div>
  <h2 class="slide-h2">{}</h2>
  <div class="slide-sub">{}</div>
  <div class="slide-p">{}</div>
</div>
<div class="code-box">
  <div style="color: #64748b; font-size: 14px; margin-bottom: 12px; text-transform: uppercase;">Language: {}</div>
  {}
</div>"#,
                    Self::escape_html(&slide.title),
                    Self::escape_html(&slide.subtitle),
                    slide.body_html,
                    Self::escape_html(&lang),
                    code_lines_html
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
            r#"<div class="slide{theme_class}" id="slide-{index}" data-layout="{layout_attr}" data-notes="{notes}" style="{inline_styles}">
  <div class="slide-header">
    <div class="slide-badge">SLIDE {index:02} / {total_slides:02}</div>
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 14px; color: #64748b;">REHAN QUANT LAB™</div>
  </div>

  {inner_content}

  <div class="slide-footer">
    <div>{title}</div>
    <div>P: Presenter View • L: Laser • D: Draw • F: Fullscreen • O: Grid</div>
  </div>
</div>
"#,
            index = slide.index,
            total_slides = total_slides,
            layout_attr = layout_attr,
            notes = Self::escape_html(&slide.notes),
            theme_class = theme_class,
            inline_styles = inline_styles,
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

    /// Generates a master default enterprise presentation markdown string with all features demonstrated
    pub fn generate_default_deck() -> String {
        r#"---
title: "Rehan Quant Lab Enterprise Architecture"
author: "Mohammad Rehan"
date: "2026-11-02"
theme: "dark"
autoplay: 0
---
<!-- layout: title -->
<!-- notes: Welcome attendees. Highlight our sovereign desktop focus and air-gapped security models. -->
# Rehan Quant Lab
## Air-Gapped Desktop Software & Distributed Systems
High-throughput sovereign software suites engineered for offline enterprise compliance, cryptographic immutability, and deterministic low-latency execution.

---
<!-- layout: metrics -->
<!-- notes: Present the raw silicon benchmarks. Emphasize sub-microsecond latency and zero external dependencies. -->
# Operational Performance
## Deterministic Benchmark Telemetry
Physical measurements recorded on bare-metal x86_64 silicon:

[ <0.01ms | Native C-ABI Latency | Pure-Rust execution without garbage collector jitter ]
[ 100% | Air-Gapped Integrity | Complete isolation with zero telemetry packets ]
[ $199 | Perpetual License | Perpetual license ownership with zero recurring fees ]

---
<!-- layout: split -->
<!-- notes: Walk through the 4 flagship suites. DocumentShield for legal, WhisperVault for voice, RetailPOS for counters, and StoreChain for multi-store sync. -->
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

### 4. RQL StoreChain™
- 5-till local mesh Wi-Fi network
- Store-and-forward Merkle branch sync
- Zero monthly cloud subscriptions
:::

---
<!-- layout: code -->
<!-- notes: Explain the invariant checking mechanism. Emphasize line 6 and 7 where memory state hash is verified. -->
# Deterministic Process Supervision
## AegisDB Continuous Invariant Verification
```rust {4-7}
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
<!-- notes: Mathematical formulation of network latency and memory bandwidth. -->
# Mathematical Invariants
## Formal Bounds on Execution Latency
Total execution latency $T(n)$ adheres to the linear pipeline model:

$$T(n) = \frac{\text{Payload Size}}{\text{Bus Bandwidth}} + \sum_{i=1}^{k} \tau_i$$

- **Computational Bound**: Time complexity remains $\mathcal{O}(1)$ for hot state retrieval.
- **Memory Invariant**: Peak resident memory footprint $\le 32\text{ MB}$ across all execution cycles.
- **Cryptographic Sealing**: Every transaction journals an append-only hash:
  $$H_{t} = \text{SHA-256}(H_{t-1} \parallel \text{Entry}_t)$$

---
<!-- layout: title -->
<!-- notes: Open for questions and discuss licensing terms. -->
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
