import sys
from playwright.sync_api import sync_playwright

def scrape(url, page_limit):
    data = []

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            
            print('FETCHING LINKS FROM URL')
            links = page.eval_on_selector_all('a', "elements => elements.map(e => e.href)")
            links = list(set(links))

            if not links:
                print("NO LINKS FOUND.")
                return

            with open('data.txt', 'w') as file: pass

            for link in links:
                if page_limit == 0:
                    print("----------- [ PAGE LEVEL REACHED ] ----------")
                    break

                print(f'FETCHING PAGE FROM : {link}')
                
                try:
                    page.goto(link, timeout=10000)
                    t_links = page.eval_on_selector_all('a', "elements => elements.map(e => e.href)")

                    t_links = list(set(links))
                    link.join(t_links)
                    
                    content = page.locator('body').inner_text()
                    
                    with open("data.txt", 'a', encoding="utf-8") as f:
                        f.write(content + "\n\n")

                    data.append(content)
                    page_limit -= 1
                    print(f"REMAINING PAGE TO SCRAPE : {page_limit}")

                except Exception as e:
                    print(f"ERROR WHILE FECTHING -> {link}: {e}")
                    continue

            browser.close()
        except Exception as e:
            print(f"\n[ ERROR OCCURED ]\n{e}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("""
        Usage:
        argument 1: URL 
        argument 2: PAGE LIMIT (integer)
        """)
        sys.exit(1)

    try:
        url = sys.argv[1]
        page_limit = int(sys.argv[2])
        
        if page_limit <= 0:
            raise ValueError("INVALID PAGE LIMIT.")

        print(f"\nURL: {url}\PAGE LIMIT: {page_limit}\n")
        scrape(url, page_limit)

    except ValueError as ve:
        print(f"INVALID PARAMS : {ve}")
        sys.exit(1)
