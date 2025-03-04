import re
from playwright.sync_api import sync_playwright

db = []

def get_page(url):
    print("getting page from" + url)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        content = page.locator('p').all_inner_texts()
        browser.close()
        return content

# key = input('ENTER KEWORD: ')
key = 'bull'
# urls ==================================================================================================
urls = ['https://www.wikipedia.org/wiki/' + key, 'https://www.britannica.com/search?query=' + key]
# 'https://www.dictionary.com/browse/' + key, 'https://www.thesaurus.com/browse/' + key]
data = []

for url in urls:
    doc = get_page(url)
    data.append(doc)
# data extraction =======================================================================================

def clean_text(text):
    text = re.sub(r'\[\d+\]', '', text) # remove reference numbers
    text = re.sub(r'\([^)]*\)', '', text) # remove words inside parenthesis
    
    text = re.sub(r'\n+', '\n', text) # remove extra newlines
    text = re.sub(r'\n', ' ', text) # replace newline with space
    text = re.sub(r'\s+', ' ', text) # remove extra spaces
    text = re.sub(r'^\s+|\s+$', '', text) # remove leading and trailing spaces
    return text


for paragraphs in data:
    for paragraph in paragraphs:
        paragraph = clean_text(paragraph)
        sentences = re.split(r'(?<=[.!?]) +', paragraph)
        for sentence in sentences:
            db.append(sentence)

for sentence in db:
    print(sentence)

