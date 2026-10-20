"""
=============================================================================
REHAN QUANT LAB™ — WEBSITE BUILDER KINETIC ADDON (GALL'S LAW EDITION)
Autonomous Awwwards-Grade Motion & Telemetry Injector for Generated Sites
=============================================================================
"""

import re
from pathlib import Path
from typing import Optional, Dict, Any

KINETIC_CORE_JS = """/**
 * REHAN QUANT LAB™ — AWWWARDS KINETIC & TELEMETRY ENGINE (INLINE CORE)
 * Gall's Law Fortified • Zero External Dependencies • 120 FPS Native
 */
(function() {
    'use strict';
    const isTouch = window.matchMedia('(hover: none) and (pointer: coarse)').matches;
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reducedMotion) return;

    // 1. Lenis-Grade Smooth Inertial Scroll (Zero Hijacking)
    if (!isTouch) {
        let targetY = window.scrollY, currentY = window.scrollY, isRunning = false;
        window.addEventListener('wheel', (e) => {
            if (e.target.closest('#chat-messages, textarea, .overflow-y-auto, [data-no-kinetic-scroll]')) return;
            const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
            targetY = Math.max(0, Math.min(maxScroll, targetY + e.deltaY));
            if (!isRunning) { isRunning = true; requestAnimationFrame(tickScroll); }
        }, { passive: true });
        window.addEventListener('scroll', () => {
            if (Math.abs(window.scrollY - currentY) > 80) { currentY = window.scrollY; targetY = window.scrollY; }
        }, { passive: true });
        function tickScroll() {
            const diff = targetY - currentY;
            if (Math.abs(diff) > 0.4) {
                currentY += diff * 0.085;
                window.scrollTo(0, Math.round(currentY));
                requestAnimationFrame(tickScroll);
            } else { currentY = targetY; isRunning = false; }
        }
    }

    // 2. Hardware-Accelerated Viewport Reveal Cascades
    const style = document.createElement('style');
    style.textContent = `
        .kinetic-reveal { opacity: 0; transform: translateY(20px) scale(0.99); transition: opacity 0.7s cubic-bezier(0.16,1,0.3,1), transform 0.7s cubic-bezier(0.16,1,0.3,1); will-change: opacity, transform; }
        .kinetic-reveal.kinetic-active { opacity: 1; transform: translateY(0) scale(1); }
        .kinetic-hover-card { transition: transform 0.35s cubic-bezier(0.16,1,0.3,1), box-shadow 0.35s ease, border-color 0.3s ease; }
        .kinetic-hover-card:hover { transform: translateY(-4px) scale(1.008); box-shadow: 0 16px 36px -10px rgba(6,182,212,0.18); }
    `;
    document.head.appendChild(style);

    window.addEventListener('DOMContentLoaded', () => {
        const obs = new IntersectionObserver((entries, o) => {
            entries.forEach((e, i) => {
                if (e.isIntersecting) {
                    setTimeout(() => e.target.classList.add('kinetic-active'), Math.min(i * 50, 250));
                    o.unobserve(e.target);
                }
            });
        }, { threshold: 0.08 });
        document.querySelectorAll('main > section, article, .grid > div, footer').forEach(el => {
            el.classList.add('kinetic-reveal');
            if (el.classList.contains('border')) el.classList.add('kinetic-hover-card');
            obs.observe(el);
        });
    });
})();
"""

def inject_kinetic_engine(html: str, standalone: bool = True, custom_script_name: str = "rehan_kinetic_engine.js") -> str:
    """
    Injects the Awwwards Kinetic Core into raw HTML.
    - If standalone=True: Inlines the minified engine into a script tag before </body>.
    - If standalone=False: Links <script src="rehan_kinetic_engine.js" defer></script> into <head>.
    """
    if "rehan_kinetic_engine" in html or "AWWWARDS KINETIC" in html:
        return html  # Idempotent: already injected

    if standalone:
        script_block = f"\n<!-- Gall's Law Fortified Kinetic Core -->\n<script>\n{KINETIC_CORE_JS}\n</script>\n</body>"
        if "</body>" in html:
            return html.replace("</body>", script_block, 1)
        return html + script_block
    else:
        link_tag = f'\n<script src="{custom_script_name}" defer></script>\n</head>'
        if "</head>" in html:
            return html.replace("</head>", link_tag, 1)
        return f'<script src="{custom_script_name}" defer></script>\n' + html

def deploy_kinetic_asset_to_dir(target_dir: Path, source_js_path: Optional[Path] = None):
    """
    Ensures rehan_kinetic_engine.js is present in the target deployment directory.
    """
    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    dest_path = target_dir / "rehan_kinetic_engine.js"
    
    if source_js_path and Path(source_js_path).exists():
        dest_path.write_text(Path(source_js_path).read_text(encoding="utf-8"), encoding="utf-8")
    else:
        # Fallback to local source in portfolio directory
        local_src = Path(__file__).resolve().parent / "Deployed_Websites" / "mohammadrehan.pages.dev" / "rehan_kinetic_engine.js"
        if local_src.exists():
            dest_path.write_text(local_src.read_text(encoding="utf-8"), encoding="utf-8")
        else:
            dest_path.write_text(KINETIC_CORE_JS, encoding="utf-8")
    return dest_path
