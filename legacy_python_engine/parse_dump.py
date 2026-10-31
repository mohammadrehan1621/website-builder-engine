import re
import json

with open(r"C:\Users\rehan\Desktop\projects\website_builder\maps_dump.html", "r", encoding="utf-8") as f:
    data = f.read()

# Let's search for JSON arrays inside window.APP_INITIALIZATION_STATE
match = re.search(r"window\.APP_INITIALIZATION_STATE\s*=\s*(.*?);window\.APP_FLAGS", data, re.DOTALL)
if match:
    raw = match.group(1)
    print("Found APP_INITIALIZATION_STATE, length:", len(raw))
    # Search for strings in the data
    strings = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', raw)
    print(f"Total strings extracted: {len(strings)}")
    
    # Filter interesting strings
    interesting = []
    for s in strings:
        s_clean = s.replace('\\"', '"')
        if any(w in s_clean.lower() for w in ['ali mobile', 'boring road', 'patna', 'star', 'service', 'price', 'phone', 'discount', 'varma', 'shop']):
            if len(s_clean) > 8 and len(s_clean) < 200:
                if not any(b in s_clean for b in ['http', 'www', 'css', 'function', '.js']):
                    interesting.append(s_clean)
    
    print("\n--- INTERESTING STRINGS ---")
    for item in set(interesting[:30]):
        print("•", item)
else:
    print("No APP_INITIALIZATION_STATE match.")
