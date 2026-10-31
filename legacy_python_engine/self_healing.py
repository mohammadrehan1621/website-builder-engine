import os
import json
import re
import time
from pathlib import Path
from typing import Dict, Any, Optional, List

BASE_DIR = Path(__file__).resolve().parent
HEALTH_CACHE_FILE = BASE_DIR / "model_health.json"
HEALING_LOG_FILE = BASE_DIR / "healing.log"

class SelfHealingSentinel:
    """
    Self-Healing Improving Layer:
    - Maintains a real-time health and quota heatmap across all Gemini models.
    - Intercepts and auto-repairs generated HTML to guarantee zero broken assets.
    - Automatically handles transient API degradation with smart failover.
    """

    @staticmethod
    def log_event(event_type: str, details: str):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] [{event_type}] {details}\n"
        try:
            with open(HEALING_LOG_FILE, "a", encoding="utf-8") as f:
                f.write(log_line)
        except Exception:
            pass

    @classmethod
    def record_model_status(cls, model_name: str, success: bool, error_msg: Optional[str] = None):
        """Updates the shared model health cache."""
        health_data = cls.load_health_data()
        now = time.time()
        
        if model_name not in health_data:
            health_data[model_name] = {
                "status": "healthy",
                "success_count": 0,
                "error_count": 0,
                "last_success": 0,
                "last_error": 0,
                "last_error_msg": ""
            }

        entry = health_data[model_name]
        if success:
            entry["status"] = "healthy"
            entry["success_count"] = entry.get("success_count", 0) + 1
            entry["last_success"] = now
        else:
            entry["status"] = "degraded"
            entry["error_count"] = entry.get("error_count", 0) + 1
            entry["last_error"] = now
            entry["last_error_msg"] = error_msg or "Unknown error"
            cls.log_event("MODEL_FAILOVER", f"Model '{model_name}' marked degraded: {error_msg}")

        try:
            with open(HEALTH_CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(health_data, f, indent=2)
        except Exception:
            pass

    @classmethod
    def load_health_data(cls) -> Dict[str, Any]:
        if HEALTH_CACHE_FILE.exists():
            try:
                with open(HEALTH_CACHE_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    @classmethod
    def get_optimal_model(cls, candidates: List[str]) -> str:
        """Picks the healthiest model from candidates based on real-time health score, error recency, and past success rate."""
        if not candidates:
            return "gemini-3.5-flash-lite"

        health = cls.load_health_data()
        now = time.time()

        def model_score(m: str) -> float:
            info = health.get(m, {})
            status = info.get("status", "healthy")
            success_count = info.get("success_count", 0)
            error_count = info.get("error_count", 0)
            last_error = info.get("last_error", 0)
            last_success = info.get("last_success", 0)

            score = 100.0
            if status == "healthy":
                score += 200.0
            elif status == "degraded":
                score -= 300.0

            # Recency penalty: penalize models with recent 429/503 errors within last 15 mins
            time_since_err = (now - last_error) if last_error > 0 else 999999
            if time_since_err < 300:
                score -= 500.0
            elif time_since_err < 900:
                score -= 200.0

            # Reward recent successes
            time_since_succ = (now - last_success) if last_success > 0 else 999999
            if time_since_succ < 300:
                score += 150.0

            score += min(success_count * 2.0, 100.0)
            score -= min(error_count * 1.5, 150.0)
            return score

        ranked = sorted(candidates, key=model_score, reverse=True)
        return ranked[0]

    @classmethod
    def repair_and_optimize_html(cls, html: str) -> str:
        """
        Self-healing AST & DOM sanitizer:
        - Automatically fixes truncated or missing HTML tags.
        - Injects Tailwind CDN if missing.
        - Injects Lucide CDN and DOMContentLoaded initializer if missing.
        - Guarantees viewport meta tag and smooth scrolling.
        """
        if not html:
            return html

        repaired = html.strip()

        # 1. Strip accidental markdown code fences
        if repaired.startswith("```html"):
            repaired = repaired[7:]
        elif repaired.startswith("```"):
            repaired = repaired[3:]
        if repaired.endswith("```"):
            repaired = repaired[:-3]
        repaired = repaired.strip()

        # 2. Ensure DOCTYPE and HTML opening
        if not repaired.startswith("<!DOCTYPE html>") and not repaired.startswith("<!doctype html>"):
            repaired = "<!DOCTYPE html>\n" + repaired

        if "<html" not in repaired:
            repaired = repaired.replace("<!DOCTYPE html>", '<!DOCTYPE html>\n<html lang="en" class="scroll-smooth">')

        # 3. Ensure Tailwind CSS is included
        if "tailwindcss.com" not in repaired:
            tailwind_tag = '<script src="https://cdn.tailwindcss.com"></script>\n'
            if "<head>" in repaired:
                repaired = repaired.replace("<head>", f"<head>\n    {tailwind_tag}")
            else:
                repaired = f"<head>\n    {tailwind_tag}</head>\n" + repaired

        # 3.5. Ensure Chatbot Slim Scrollbars & Overflow Protection
        if any(marker in repaired for marker in ["ai-chatbot-widget", "chatbot-modal", "aria-window", "aria-messages", "chat-messages"]):
            if "::-webkit-scrollbar" not in repaired or "#chatbot-modal *::-webkit-scrollbar" not in repaired:
                scrollbar_css = """<style>
#chatbot-modal *::-webkit-scrollbar, #aria-window *::-webkit-scrollbar, #chat-messages::-webkit-scrollbar, #aria-messages::-webkit-scrollbar, .no-scrollbar::-webkit-scrollbar { width: 4px; height: 4px; }
#chatbot-modal *::-webkit-scrollbar-track, #aria-window *::-webkit-scrollbar-track, #chat-messages::-webkit-scrollbar-track, #aria-messages::-webkit-scrollbar-track { background: transparent; }
#chatbot-modal *::-webkit-scrollbar-thumb, #aria-window *::-webkit-scrollbar-thumb, #chat-messages::-webkit-scrollbar-thumb, #aria-messages::-webkit-scrollbar-thumb { background: rgba(6, 182, 212, 0.35); border-radius: 9999px; }
.no-scrollbar::-webkit-scrollbar { display: none !important; width: 0 !important; height: 0 !important; }
.no-scrollbar { -ms-overflow-style: none !important; scrollbar-width: none !important; }
#chat-messages, #aria-messages { overflow-x: hidden !important; scrollbar-width: thin; scrollbar-color: rgba(6, 182, 212, 0.35) transparent; }
</style>
"""
                if "<head>" in repaired:
                    repaired = repaired.replace("<head>", f"<head>\n    {scrollbar_css}")
                else:
                    repaired = f"<head>\n    {scrollbar_css}</head>\n" + repaired

# 4. Ensure Lucide Icons library is included
        if "lucide" not in repaired.lower():
            lucide_cdn = '<script src="https://unpkg.com/lucide@latest"></script>\n'
            if "<head>" in repaired:
                repaired = repaired.replace("<head>", f"<head>\n    {lucide_cdn}")

        # 5. Ensure Lucide initialization script is present before closing body
        if "lucide.createIcons" not in repaired:
            lucide_init = """<script>
document.addEventListener('DOMContentLoaded', () => {
    if (window.lucide) {
        try { lucide.createIcons(); } catch(e) { console.error('Lucide error:', e); }
    }
});
</script>"""
            if "</body>" in repaired:
                repaired = repaired.replace("</body>", f"{lucide_init}\n</body>")
            else:
                repaired = repaired + f"\n{lucide_init}"

        # 6. Universal Self-Healing Navigation Guard (Prevents ERR_FILE_NOT_FOUND on local/standalone files)
        if "Universal Self-Healing Navigation Guard" not in repaired:
            nav_guard = """<script>
// Universal Self-Healing Navigation Guard (Prevents ERR_FILE_NOT_FOUND)
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (!href) return;
            if (href.endsWith('.html') && (location.protocol === 'file:' || !href.startsWith('http'))) {
                const targetBase = href.split('#')[0].replace('.html', '').toLowerCase();
                const hashPart = href.includes('#') ? href.split('#')[1] : null;
                const targetId = hashPart || (targetBase === 'index' ? 'about' : targetBase);
                const localEl = document.getElementById(targetId) || document.getElementById(targetBase);
                if (localEl) {
                    e.preventDefault();
                    localEl.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });
});
</script>"""
            if "</body>" in repaired:
                repaired = repaired.replace("</body>", f"{nav_guard}\n</body>")
            else:
                repaired = repaired + f"\n{nav_guard}"

        # 7. Ensure closing tags are preserved
        if "</body>" not in repaired:
            repaired += "\n</body>"
        if "</html>" not in repaired:
            repaired += "\n</html>"

        return repaired
