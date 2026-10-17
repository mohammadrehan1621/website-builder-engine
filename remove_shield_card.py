from pathlib import Path
import re

portfolio_dir = Path(r"c:\Users\rehan\Desktop\website_builder\Deployed_Websites\mohammadrehan.pages.dev")
projects_file = portfolio_dir / "projects.html"
index_file = portfolio_dir / "index.html"

# 1. Clean projects.html
content = projects_file.read_text(encoding="utf-8")

# Remove the card
card_pattern = r'<!-- Project 6: Mathematical Stealth Shield & Zero-Knowledge Defense Mesh -->.*?</div>\s*</div>\s*</div>\s*</div>\s*</section>'
match = re.search(r'<!-- Project 6: Mathematical Stealth Shield.*?</div>\s*</div>\s*</div>\s*</div>\s*</section>', content, flags=re.DOTALL)
if match:
    replacement = "</div>\n        </div>\n    </section>"
    content = content[:match.start()] + replacement + content[match.end():]
    print("Removed Project 6 card from projects.html")
else:
    # Alternative direct slice
    start_tag = "<!-- Project 6: Mathematical Stealth Shield"
    end_tag = "<!-- What I Build & Deliver Section -->"
    s_idx = content.find(start_tag)
    e_idx = content.find(end_tag)
    if s_idx != -1 and e_idx != -1:
        content = content[:s_idx] + "</div>\n        </div>\n    </section>\n    " + content[e_idx:]
        print("Removed Project 6 card via direct index slice")

# Remove the 'Cybersecurity & Cryptography' filter button if present
content = content.replace('<button class="filter-btn px-4 py-2 rounded-xl text-sm font-medium bg-white text-slate-600 border border-slate-200 hover:bg-slate-100 transition" onclick="filterProjects(\'security\')">Cybersecurity &amp; Cryptography</button>', '')

# Update Aria response in projects.html to reference the 5 flagship applications
aria_clean = """response = `Mohammad Rehan has engineered an extraordinary production software suite:
                1. <strong>Indian Trading Bot</strong>: Multi-agent quantitative options sniper with 5-pillar confluence and 4-account family fleet execution.<br>
                2. <strong>Apex-Attendance-Vault</strong>: Biometric and camera attendance system with cryptographic integrity and automated PDF payroll reporting.<br>
                3. <strong>Footwear POS & Sales Dashboard</strong>: Real-world retail inventory ledger, barcode billing, and sales analytics.<br>
                4. <strong>Maison Ladies Zone (ladieszonepatna.in)</strong>: Luxury boutique digital showcase with WhatsApp concierge.<br>
                5. <strong>Autonomous AI Web Studio</strong>: Multi-model generation engine with AST self-healing and 1-click edge deployment.<br>
                <div class="pt-2"><a href="projects.html" class="inline-block bg-indigo-600 hover:bg-indigo-500 text-white px-3 py-1.5 rounded-lg text-xs font-medium">View All Projects &rarr;</a></div>`;"""

content = re.sub(r'response\s*=\s*`Mohammad Rehan has engineered 6 flagship.*?View All 6 Projects &rarr;</a></div>`;', aria_clean, content, flags=re.DOTALL)
projects_file.write_text(content, encoding="utf-8")
print("projects.html saved cleanly!")

# Also check index.html
if index_file.exists():
    c_idx = index_file.read_text(encoding="utf-8")
    c_idx = re.sub(r'response\s*=\s*`Mohammad Rehan has engineered 6 flagship.*?View All 6 Projects &rarr;</a></div>`;', aria_clean, c_idx, flags=re.DOTALL)
    index_file.write_text(c_idx, encoding="utf-8")
    print("index.html checked and saved!")
