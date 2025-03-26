import sys
from playwright.sync_api import sync_playwright

def scrape(url, page_limit):
    data = []
    
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            
            print('Fetching links from source URL...')
            links = page.eval_on_selector_all('a', "elements => elements.map(e => e.href)")
            
            # Ensure we only process unique links
            links = list(set(links))

            if not links:
                print("No links found on the page.")
                return

            with open('data.txt', 'w') as file:
                pass  # Create or clear the file

            for link in links:
                if page_limit == 0:
                    print(" [ PAGE LEVEL REACHED ] ")
                    break

                print(f'Fetching page from: {link}')
                
                try:
                    page.goto(link, timeout=10000)  # Set timeout to avoid hanging
                    content = page.locator('body').inner_text()
                    
                    # Save to file
                    with open("data.txt", 'a', encoding="utf-8") as f:
                        f.write(content + "\n\n")

                    data.append(content)
                    page_limit -= 1
                    print(f"Remaining pages to fetch: {page_limit}")

                except Exception as e:
                    print(f"Error fetching {link}: {e}")
                    continue

            browser.close()
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("""
        Usage:
        argument 1: URL 
        argument 2: Page limit (integer)
        """)
        sys.exit(1)

    try:
        url = sys.argv[1]
        page_limit = int(sys.argv[2])
        
        if page_limit <= 0:
            raise ValueError("Page limit must be a positive integer.")

        print(f"\nURL: {url}\nPage Limit: {page_limit}\n")
        scrape(url, page_limit)

    except ValueError as ve:
        print(f"Invalid input: {ve}")
        sys.exit(1)
