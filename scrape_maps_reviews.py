import requests
import json
import re

url = "https://www.google.com/maps/place/ALI+MOBILE/@25.6126551,85.1154862,17z/data=!4m6!3m5!1s0x39ed59eb1d0c48db:0x4b1c7084076ba1b8!8m2!3d25.6126551!4d85.1180611!16s%2Fg%2F11tx6hgtg1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

r = requests.get(url, headers=headers)

# Find all review blocks in raw json/text
with open("maps_dump.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print(f"Dumped {len(r.text)} bytes.")

# Search for rating & review count
rating_match = re.search(r'\[null,null,([1-5]\.[0-9]),([0-9]+)\]', r.text)
if rating_match:
    print(f"Rating: {rating_match.group(1)} stars from {rating_match.group(2)} reviews")

# Look for reviews array
snippets = re.findall(r'\[\"(.*?)\",null,null,\[\[([1-5])\]', r.text)
print(f"Found {len(snippets)} snippets")
for s in snippets[:10]:
    if len(s[0]) > 15:
        print(f"Rating: {s[1]} stars - Text: {s[0]}")
