import sys
import urllib.request
import json
import os
from datetime import datetime


def check_url(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            print(f"Response code for {url}: {response.status}")
            return response.status == 200
    except Exception:
        print(f"Error occurred while checking {url}")
        return False


failed_urls = []

""" with open("urls.txt", "r") as file:
    urls = [line.strip() for line in file if line.strip()] """

url_list = os.environ.get("URLS")

if url_list:
    urls = [url.strip() for url in url_list.split(",")]
else:
    with open("urls.txt", "r") as file:
        urls = [line.strip() for line in file if line.strip()]

for url in urls:
    print(f"Checking {url}...")

    if check_url(url):
        print(f"PASS: {url}")
    else:
        print(f"FAIL: {url}")
        failed_urls.append(url)

report = {
    "timestamp": datetime.now().isoformat(),
    "checked": len(urls),
    "passed": len(urls) - len(failed_urls),
    "failed": failed_urls
}

with open("results.json", "w") as f:
    json.dump(report, f, indent=2)

if failed_urls:
    print("\nThe following URLs failed:")
    for url in failed_urls:
        print(f" - {url}")

    sys.exit(1)

print("\nAll URL checks passed.")
