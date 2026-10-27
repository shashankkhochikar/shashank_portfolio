from pathlib import Path
from playwright.sync_api import sync_playwright

html = Path(__file__).with_name("resume-design.html").resolve()
out = Path(__file__).with_name("resume-preview.png").resolve()

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 794, "height": 1123}, device_scale_factor=2)
    page.goto(html.as_uri(), wait_until="networkidle")
    page.screenshot(path=str(out), full_page=True)
    browser.close()

print("wrote", out)
