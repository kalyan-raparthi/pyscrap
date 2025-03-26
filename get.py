from playwright.sync_api import sync_playwright

PAGE_LIMIT = 10
LINKS = []
DATA  = []
url = 'https://www.kitsw.ac.in/'

def get_links(url):
    print("getting page from" + url)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        page.goto(url)
        content = page.eval_on_selector_all('a', "elements => elements.map(e => e.href)")
        
        browser.close()
        return content

def get_page(url, element_type):
    print("getting page from" + url)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        content = page.locator(element_type).all_inner_texts()
        browser.close()
        return content

def add_data(link):
    data = get_page(link, 'p')
    print(data) 
    DATA.append(data)

doc = get_page(url, 'p')
ahrefs = set(get_links(url))
# print(ahrefs)

for link in ahrefs:
    try:
        print(PAGE_LIMIT)
        if PAGE_LIMIT == 0: break
        add_data(link)
        PAGE_LIMIT -= 1
    except:
        pass

# file writing =======================================================================================

# print(DATA)

file = open('data.txt', 'a')

print('-----------------------------------------------------------------------------------')
print(len(DATA))
for x in DATA:
    print(x)
    # file.write(d)
file.close()