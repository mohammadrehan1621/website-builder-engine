import os
import sys
import re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PORTFOLIO_DIR = Path(r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev")
ALL_HTML_FILES = ["index.html", "projects.html", "aegis.html", "experience.html", "contact.html", "legal.html"]

# Comprehensive Lively CSS Stylesheet to inject into <head>
LIVELY_CSS = """
    <!-- 🎨 LIVELY MOTION & INSTITUTIONAL GUI STYLESHEET -->
    <style>
        /* Smooth Custom Scrollbar */
        ::-webkit-scrollbar { width: 7px; height: 7px; }
        ::-webkit-scrollbar-track { background: #f8fafc; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 9999px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

        /* Glassmorphism Panels */
        .glass-panel {
            background: rgba(255, 255, 255, 0.88);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
        }
        .dark-glass {
            background: rgba(15, 23, 42, 0.94);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
        }

        /* Hardware-Accelerated Smooth Animations */
        @keyframes floatSlow {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-7px) rotate(0.4deg); }
        }

        @keyframes pulseGlow {
            0%, 100% { opacity: 0.35; transform: scale(1); filter: blur(50px); }
            50% { opacity: 0.8; transform: scale(1.1); filter: blur(60px); }
        }

        @keyframes shimmerSweep {
            0% { transform: translateX(-150%) skewX(-20deg); }
            40%, 100% { transform: translateX(250%) skewX(-20deg); }
        }

        @keyframes subtleRadar {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes pulseBorder {
            0%, 100% { border-color: rgba(16, 185, 129, 0.4); box-shadow: 0 0 15px rgba(16, 185, 129, 0.1); }
            50% { border-color: rgba(56, 189, 248, 0.8); box-shadow: 0 0 25px rgba(56, 189, 248, 0.25); }
        }

        .animate-float-slow {
            animation: floatSlow 6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
        }

        .animate-pulse-glow {
            animation: pulseGlow 4s ease-in-out infinite;
        }

        .animate-pulse-border {
            animation: pulseBorder 3s infinite ease-in-out;
        }

        /* Shimmer Glint on High-Priority CTAs & Badges */
        .shimmer-badge {
            position: relative;
            overflow: hidden;
        }
        .shimmer-badge::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 60%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            animation: shimmerSweep 4s ease-in-out infinite;
            pointer-events: none;
        }

        /* Fluid Scroll Reveal (Zero Jank, 60fps) */
        .reveal-on-scroll {
            opacity: 0;
            transform: translateY(24px);
            transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: opacity, transform;
        }
        .reveal-on-scroll.is-visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* Card Tilt, Lift & Luminous Hover Physics */
        .project-card, .hover-lift-card {
            transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease, border-color 0.3s ease;
            will-change: transform, box-shadow;
        }
        .project-card:hover, .hover-lift-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 25px 50px -12px rgba(15, 23, 42, 0.35), 0 0 30px -5px rgba(56, 189, 248, 0.2);
        }

        /* Button Hover Micro-Spring Physics */
        .btn-spring {
            transition: transform 0.22s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.22s ease;
        }
        .btn-spring:hover {
            transform: translateY(-2.5px) scale(1.02);
        }
        .btn-spring:active {
            transform: translateY(0px) scale(0.98);
        }

        /* Ambient Glowing Background Orbs */
        .ambient-orb {
            position: absolute;
            border-radius: 9999px;
            pointer-events: none;
            z-index: 0;
        }
    </style>
"""

LIVELY_SCRIPT_TAG = '<script src="lively_motion.js" defer></script>'

def apply_lively_gui():
    print("=" * 70)
    print("🎨 INJECTING MASTER LIVELY GUI & 60FPS ANIMATIONS (ALL PAGES)")
    print("=" * 70)

    for fname in ALL_HTML_FILES:
        fpath = PORTFOLIO_DIR / fname
        if not fpath.exists():
            continue

        content = fpath.read_text(encoding="utf-8")

        # 1. Inject LIVELY_CSS if not present
        if "LIVELY MOTION & INSTITUTIONAL GUI STYLESHEET" not in content:
            content = content.replace('</head>', f'{LIVELY_CSS}\n</head>')
            print(f"[{fname}] Injected master lively stylesheet.")
        else:
            # Update existing lively css block
            content = re.sub(r'<!-- 🎨 LIVELY MOTION.*?/style>', LIVELY_CSS.strip(), content, flags=re.DOTALL)
            print(f"[{fname}] Updated master lively stylesheet.")

        # 2. Inject lively_motion.js script before </body>
        if "lively_motion.js" not in content:
            content = content.replace('</body>', f'{LIVELY_SCRIPT_TAG}\n</body>')
            print(f"[{fname}] Linked lively_motion.js script.")

        # 3. Add responsive classes and micro-interactions
        # Button spring on interactive buttons
        content = re.sub(r'class="([^"]*rounded-xl[^"]*shadow-md[^"]*)"', r'class="\1 btn-spring"', content)
        content = re.sub(r'class="([^"]*rounded-xl[^"]*bg-slate-900[^"]*)"', r'class="\1 btn-spring"', content)

        # 4. Enhance Hero Section on index.html
        if fname == "index.html":
            # Add float animation to hero profile card
            content = content.replace('id="hero-profile-card" class="bg-white/95', 'id="hero-profile-card" class="bg-white/95 animate-float-slow')
            # Enhance ambient glowing orbs
            content = content.replace('class="absolute top-10 left-1/4 w-96 h-96 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none -z-0"',
                                      'class="ambient-orb top-5 left-10 w-96 h-96 bg-gradient-to-tr from-indigo-500/25 to-sky-400/20 blur-3xl pointer-events-none animate-pulse-glow"')
            content = content.replace('class="absolute bottom-10 right-1/4 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none -z-0"',
                                      'class="ambient-orb bottom-10 right-10 w-[30rem] h-[30rem] bg-gradient-to-bl from-emerald-500/20 to-teal-400/25 blur-3xl pointer-events-none animate-pulse-glow"')
            # Top live release ticker shimmer
            content = content.replace('id="live-ticker-container" class="', 'id="live-ticker-container" class="shimmer-badge ')

        # 5. Enhance cards in projects.html
        if fname == "projects.html":
            content = content.replace('class="project-card bg-slate-950', 'class="project-card hover-lift-card bg-slate-950')

        fpath.write_text(content, encoding="utf-8")
        print(f"[{fname}] Saved with lively motion enhancements.")

    print("\n✅ All pages upgraded with lively motion and responsive aesthetics!")

if __name__ == "__main__":
    apply_lively_gui()
