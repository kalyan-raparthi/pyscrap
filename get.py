from playwright.sync_api import sync_playwright

def get_page(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        content = page.locator('html').inner_text()
        browser.close()
        return content


url = 'https://www.livemint.com/news'

doc = get_page(url)
print(doc)
