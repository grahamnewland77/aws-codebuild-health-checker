import sys
import urllib.request


def check_url(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            print(f"Response code for {url}: {response.status}")
            return response.status == 200
    except Exception:
        print(f"Error occurred while checking {url}")
        print(f"ERROR: {e}")
        return False


failed_urls = []

with open("urls.txt", "r") as file:
    urls = [line.strip() for line in file if line.strip()]

for url in urls:
    print(f"Checking {url}...")

    if check_url(url):
        print(f"PASS: {url}")
    else:
        print(f"FAIL: {url}")
        failed_urls.append(url)

if failed_urls:
    print("\nThe following URLs failed:")
    for url in failed_urls:
        print(f" - {url}")

    sys.exit(1)

print("\nAll URL checks passed.")
