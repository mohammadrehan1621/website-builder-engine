path = r"C:\Users\rehan\Desktop\projects\website_builder\deploy_rehan_portfolio.py"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

needle = '"index.html",'
replacement = '"index.html",\n        "aegis.html",'
c = c.replace(needle, replacement, 1)

needle2 = '"Mohammad_Rehan_Resume.pdf",'
replacement2 = '"Mohammad_Rehan_Resume.pdf",\n        "RQL-Aegis-v1.0-Release.zip",'
c = c.replace(needle2, replacement2, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

print("Updated deploy_rehan_portfolio.py successfully!")
