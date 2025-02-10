from playwright.sync_api import sync_playwright
import requests
from bs4 import BeautifulSoup

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        content_type = response.headers.get("Content-Type", "")
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "No title found"

        return {
            "URL": url,
            "Status": status_code,
            "Content Type": content_type,
            "Title": title,
        }
    
    except requests.exceptions.RequestException as e:
        return {"URL": url, "Status": "Error", "Error": str(e)}

def capture_screenshot(url, output_path="screenshot.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=10000)  # 10s timeout
        page.screenshot(path=output_path, full_page=True)
        browser.close()

# capture_screenshot("https://minimaru.com/", "example.png")

urls = [
    "https://minimaru.com/",
    "https://wolfblass.com"
]

results = [check_website(url) for url in urls]

for result in results:
    print(result)