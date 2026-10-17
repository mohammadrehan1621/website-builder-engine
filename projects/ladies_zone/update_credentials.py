import re

file_path = r"C:\Users\rehan\Desktop\website_builder\projects\ladies_zone\generate_haute_site.py"
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update telephone in schema
code = code.replace('["+91-7091518548", "+91-8986047584"]', '["+91-8986047584", "+91-9835699398"]')

# 2. Update ticker
code = code.replace(
    'CONCIERGE: <a href="tel:+917091518548">+91 70915 18548</a>',
    'CONCIERGE: <a href="tel:+918986047584">+91 89860 47584</a> | <a href="https://wa.me/918986047584">💬 WhatsApp</a>'
)

# 3. Update hero whatsapp
code = code.replace('wa.me/917091518548', 'wa.me/918986047584')

# 4. Update salon contact row
old_salon_row = '''<div class="salon-row">
            <span class="salon-label">Direct Concierge</span>
            <span class="salon-val">
              <a href="tel:+917091518548" style="color:var(--terracotta); font-weight:700;">+91 70915 18548</a> / 
              <a href="tel:+918986047584" style="color:var(--terracotta); font-weight:700;">+91 89860 47584</a>
            </span>
          </div>'''

new_salon_row = '''<div class="salon-row">
            <span class="salon-label">Direct Concierge</span>
            <span class="salon-val">
              <a href="tel:+918986047584" style="color:var(--terracotta); font-weight:700;">+91 89860 47584</a> / 
              <a href="tel:+919835699398" style="color:var(--terracotta); font-weight:700;">+91 98356 99398</a>
            </span>
          </div>'''
code = code.replace(old_salon_row, new_salon_row)

# 5. Update footer whatsapp
code = code.replace('+91 70915 18548', '+91 89860 47584')

# 6. Update login modal placeholder
code = code.replace('placeholder="Enter PIN (8986)"', 'placeholder="Enter Secure Password"')
code = code.replace('placeholder="admin or 8986047584"', 'placeholder="admin or 8986047584 or ladieszone"')

# 7. Update JS PRIMARY_WA
code = code.replace('const PRIMARY_WA = "917091518548";', 'const PRIMARY_WA = "918986047584";\n    const SECONDARY_PHONE = "+91 98356 99398";')

# 8. Update quick view call link
code = code.replace('href="tel:+917091518548"', 'href="tel:+918986047584"')

# 9. Update login submit logic
old_login_logic = """if ((u.toLowerCase() === 'admin' || u === '8986047584' || u === '7091518548') && p === '8986') {"""
new_login_logic = """const validUsers = ['admin', 'ladieszone', '8986047584', '9835699398'];
      const validPass = 'MwvS!fSE_93t.aa';

      if (validUsers.includes(u.toLowerCase()) && p === validPass) {"""
code = code.replace(old_login_logic, new_login_logic)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated generate_haute_site.py successfully!")
