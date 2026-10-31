import requests

url = "https://raadha-rani-patna.pages.dev"
r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
print("Status Code:", r.status_code)
print("Has React Root:", '<div id="root"></div>' in r.text)
print("Has Title:", "Raadha Rani" in r.text)
print("Asset snippet:", [line for line in r.text.splitlines() if "assets/index-" in line])
