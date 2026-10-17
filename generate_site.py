import os
import sys
import json
import argparse
import webbrowser
import http.server
import socketserver
import threading
from pathlib import Path

# Force UTF-8 encoding for Windows terminals
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from generator import WebsiteGenerator, get_api_key

def serve_directory(directory: Path, port: int = 8080):
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"\n🚀 Serving site at: http://localhost:{port}")
        print("Press Ctrl+C to stop preview server.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nPreview server stopped.")

def main():
    parser = argparse.ArgumentParser(
        description="Autonomous AI & Data Website Builder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  1. Generate from Prompt:
     python generate_site.py --prompt "Modern SaaS landing page for an AI voice agent platform called EchoAI"
  
  2. Generate from JSON data:
     python generate_site.py --data sample_business.json
     
  3. Hybrid (Data + Prompt + Custom Style):
     python generate_site.py --data sample_business.json --prompt "Emphasize enterprise security and add a FAQ section" --theme "Clean Minimal Light"

  4. Generate and immediately launch live preview:
     python generate_site.py --prompt "Cybersecurity consultancy firm" --serve
        """
    )
    parser.add_argument("--prompt", "-p", type=str, help="Natural language description or instructions for the website")
    parser.add_argument("--data", "-d", type=str, help="Path to JSON file containing business or product data")
    parser.add_argument("--output", "-o", type=str, default="output_site", help="Output directory (default: ./output_site)")
    parser.add_argument("--api-key", "-k", type=str, help="Gemini API Key (optional if already in .env or GEMINI_API_KEY env var)")
    parser.add_argument("--theme", "-t", type=str, default="Modern Dark Slate & Purple Gradient", help="Theme style hint")
    parser.add_argument("--type", "-y", type=str, default="High-Converting SaaS Landing Page", help="Site architecture type (e.g. E-Commerce, Static Business, Portfolio, SaaS)")
    parser.add_argument("--model", "-m", type=str, default="gemini-3.5-flash-lite", help="Gemini model to use (default: gemini-3.5-flash-lite)")
    parser.add_argument("--multipage", action="store_true", help="Generate full 4-page connected site (index.html, about.html, services.html, contact.html)")
    parser.add_argument("--auth", action="store_true", help="Embed client-side User Authentication modal & session portal")
    parser.add_argument("--security", action="store_true", help="Embed Content-Security-Policy, anti-tamper form sanitization & trust badges")
    parser.add_argument("--mascot", action="store_true", help="Embed interactive holographic anime companion guide (Aria v2.5)")
    parser.add_argument("--serve", "-s", action="store_true", help="Launch local preview server and open in browser")
    parser.add_argument("--port", type=int, default=8080, help="Port for preview server (default: 8080)")

    args = parser.parse_args()

    if not args.prompt and not args.data:
        print("❌ Error: Please provide at least --prompt, --data, or both.")
        parser.print_help()
        sys.exit(1)

    structured_data = None
    if args.data:
        data_path = Path(args.data)
        if not data_path.exists():
            print(f"❌ Error: Data file not found: {data_path}")
            sys.exit(1)
        with open(data_path, "r", encoding="utf-8") as f:
            try:
                structured_data = json.load(f)
                print(f"✅ Loaded business data from: {data_path.name}")
            except Exception as e:
                print(f"❌ Error parsing JSON file: {e}")
                sys.exit(1)

    # Initialize generator
    api_key = args.api_key or get_api_key()
    if api_key:
        print("🔑 Gemini API Key detected! Using autonomous AI reasoning mode.")
    else:
        print("⚠️ No Gemini API Key found in arguments or .env. Using fallback responsive builder.")
        print("💡 Hint: Add GEMINI_API_KEY=your_key in .env to unlock full autonomous AI generation.")

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    generator = WebsiteGenerator(api_key=api_key, model=args.model)

    if args.multipage:
        print(f"\n⏳ Generating complete Multi-Page website (4 pages) autonomously...")
        pages_dict = generator.generate_multipage_site(
            prompt=args.prompt or "",
            data=structured_data,
            theme_hint=args.theme,
            enable_auth=args.auth,
            enable_security=args.security,
            include_interactive_character=args.mascot
        )
        for fname, content in pages_dict.items():
            (out_dir / fname).write_text(content, encoding="utf-8")
            print(f"  ✓ Generated & Saved: {fname}")
        print(f"🎉 Multi-page website successfully created at: {out_dir.resolve()}")
    else:
        print(f"\n⏳ Generating [{args.type}] website autonomously...")
        html_content = generator.generate_site(
            prompt=args.prompt or "",
            data=structured_data,
            theme_hint=args.theme,
            site_type=args.type,
            enable_auth=args.auth,
            enable_security=args.security,
            include_interactive_character=args.mascot
        )
        index_file = out_dir / "index.html"
        index_file.write_text(html_content, encoding="utf-8")
        print(f"🎉 Website successfully created at: {index_file.resolve()}")

    if args.serve:
        webbrowser.open(f"http://localhost:{args.port}")
        serve_directory(out_dir, port=args.port)

if __name__ == "__main__":
    main()
