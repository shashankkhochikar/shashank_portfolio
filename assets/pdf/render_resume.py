from pathlib import Path
from playwright.sync_api import sync_playwright

html = Path(__file__).with_name("resume-design.html").resolve()
out = Path(__file__).with_name("Shashank-Khochikar-Resume.pdf").resolve()

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(html.as_uri(), wait_until="networkidle")
    page.emulate_media(media="print")
    page.pdf(
        path=str(out),
        format="A4",
        print_background=True,
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
    )
    browser.close()

print("wrote", out, "size", out.stat().st_size)
