import requests, os, re

repo = "garysutton/quant"
api_url = f"https://api.github.com/repos/{repo}/git/trees/main?recursive=1"
save_dir = "csv_files"

os.makedirs(save_dir, exist_ok=True)

r = requests.get(api_url)
for item in r.json().get("tree", []):
    if item["path"].endswith(".csv"):
        raw_url = f"https://raw.githubusercontent.com/{repo}/main/{item['path']}"
        filename = os.path.join(save_dir, os.path.basename(item["path"]))
        print(f"Downloading {filename}...")
        with open(filename, "wb") as f:
            f.write(requests.get(raw_url).content)