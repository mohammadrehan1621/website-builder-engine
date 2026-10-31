import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update deploy_rehan_portfolio.py
deploy_script = r"C:\Users\rehan\Desktop\projects\website_builder\deploy_rehan_portfolio.py"
with open(deploy_script, "r", encoding="utf-8") as f:
    deploy_content = f.read()

target_str = '"11_RQL_LocalMesh_Cover_1080p.png",'
if target_str in deploy_content and '"12_RQL_StoreFlow_Cover_1080p.png"' not in deploy_content:
    new_files = (
        '"11_RQL_LocalMesh_Cover_1080p.png",\n'
        '        "12_RQL_StoreFlow_Cover_1080p.png",\n'
        '        "14_RQL_LedgerGuard_Cover_1080p.png",\n'
        '        "15_RQL_StockAudit_Cover_1080p.png",\n'
        '        "16_RQL_OmniDispatch_Cover_1080p.png",\n'
        '        "17_RQL_Nexus_Cover_1080p.png",'
    )
    deploy_content = deploy_content.replace(target_str, new_files)
    with open(deploy_script, "w", encoding="utf-8") as f:
        f.write(deploy_content)
    print("✅ deploy_rehan_portfolio.py updated with 5 new covers!")

# 2. Check product 11 in index.html to mirror exact styling
portfolio_dir = r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev"
index_html = os.path.join(portfolio_dir, "index.html")
projects_html = os.path.join(portfolio_dir, "projects.html")

with open(index_html, "r", encoding="utf-8", errors="ignore") as f:
    idx_content = f.read()

pos_11 = idx_content.find("11_RQL_LocalMesh")
print("Found 11_RQL_LocalMesh at:", pos_11)

if pos_11 != -1:
    card_start = idx_content.rfind("<div class=", 0, pos_11)
    card_end = idx_content.find("</div>\n</div>", pos_11)
    print("Sample card excerpt:")
    print(idx_content[card_start:card_start+500])
