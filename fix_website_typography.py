import os
import re

anti_break_css = """
/* 🛡️ Institutional Typography & Zero-Break Protections */
*, *::before, *::after {
    hyphens: none !important;
    -webkit-hyphens: none !important;
    -ms-hyphens: none !important;
}

code, kbd, samp, pre, .font-mono, [class*="font-mono"] {
    white-space: nowrap !important;
    word-break: normal !important;
    overflow-wrap: normal !important;
    display: inline-block;
}

h1, h2, h3, h4, h5, h6 {
    text-wrap: balance !important;
    hyphens: none !important;
    word-break: keep-all !important;
}

p, li, span, a {
    text-wrap: pretty;
    hyphens: none !important;
}

.whitespace-nowrap {
    white-space: nowrap !important;
}
"""

def update_file(filepath):
    print(f"Processing: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Inject anti-break CSS inside <style>
    if "/* 🛡️ Institutional Typography & Zero-Break Protections */" not in content:
        content = content.replace("</style>", f"{anti_break_css}\n</style>", 1)

    # 2. Fix awkward "is $60" in banner
    content = content.replace(
        "Bare-Metal Rust Multi-WAN is <span class=\"text-sky-400 font-bold\">$60 / &#8377;4,999</span>",
        "Bare-Metal Rust Multi-WAN (<span class=\"text-sky-400 font-bold\">$60 / &#8377;4,999</span>)"
    )
    content = content.replace(
        "Bare-Metal Rust Multi-WAN is <span class='text-sky-400 font-bold'>$60 / ₹4,999</span>",
        "Bare-Metal Rust Multi-WAN (<span class='text-sky-400 font-bold'>$60 / ₹4,999</span>)"
    )

    # 3. Fix High-Throughput in hero title of projects.html
    content = re.sub(
        r'<h1([^>]*)>\s*Architectural Engineering &amp; High-Throughput Systems\s*</h1>',
        r'<h1\1 style="text-wrap: balance;">Architectural Engineering &amp; <span class="whitespace-nowrap">High-Throughput</span> Systems</h1>',
        content
    )

    # 4. Fix typo "systems engines" in subtitle
    content = content.replace(
        "distributed high-availability systems engines, offline-first retail POS platforms",
        "distributed high-availability systems, offline-first retail POS platforms"
    )

    # 5. Fix hyphenated role in rotator
    content = content.replace(
        '"Apex-Attendance-Vault (Biometric Enterprise Security)",',
        '"Apex Attendance Vault — Biometric Enterprise Security",'
    )

    # 6. Ensure all <code> tags have whitespace-nowrap
    def add_whitespace_nowrap(match):
        code_tag = match.group(0)
        if "whitespace-nowrap" not in code_tag:
            if 'class="' in code_tag:
                return code_tag.replace('class="', 'class="whitespace-nowrap ')
            else:
                return code_tag.replace('<code', '<code class="whitespace-nowrap"')
        return code_tag

    content = re.sub(r'<code[^>]*>', add_whitespace_nowrap, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully updated: {filepath}")

base_dir = r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev"
for fname in ["projects.html", "index.html", "aegis.html", "experience.html", "contact.html", "legal.html"]:
    fpath = os.path.join(base_dir, fname)
    if os.path.exists(fpath):
        update_file(fpath)

print("Website typography fixes complete.")
