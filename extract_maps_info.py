import requests
from bs4 import BeautifulSoup
import re
import json

url = "https://www.google.com/maps/place/ALI+MOBILE/@25.6126551,85.1154862,17z/data=!4m6!3m5!1s0x39ed59eb1d0c48db:0x4b1c7084076ba1b8!8m2!3d25.6126551!4d85.1180611"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

r = requests.get(url, headers=headers)
html = r.text

# Write to a known file
out_path = r"C:\Users\rehan\Desktop\projects\website_builder\maps_page.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved HTML page. Length:", len(html))

# Extract all text blocks that look like reviews
# In Google Maps, reviews often have author names and star ratings
for m in re.finditer(r'\[\"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\",null,null,null,null,\[\[([1-5])\]', html):
    print("Reviewer:", m.group(1), "Rating:", m.group(2))

# Also search for "Ali Mobile" occurrences with context
idx = 0
while True:
    pos = html.find("ALI MOBILE", idx)
    if pos == -1:
        break
    print("Found ALI MOBILE at:", pos, "--> Context:", html[pos:pos+150])
    idx = pos + 1
    if idx > pos + 1000:
        break
