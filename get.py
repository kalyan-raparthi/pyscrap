import re
from playwright.sync_api import sync_playwright

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
# urls ===============================================================================================================================
urls = ['https://www.wikipedia.org/wiki/' + key, 'https://www.britannica.com/search?query=' + key]
# 'https://www.dictionary.com/browse/' + key, 'https://www.thesaurus.com/browse/' + key]
data = []

for url in urls:
    doc = get_page(url)
    data.append(doc)
# data extraction =====================================================================================================================

def clean_text(text):
    text = re.sub(r'\[\d+\]', '', text) # remove reference numbers
    text = re.sub(r'\n+', '\n', text) # remove extra newlines
    text = re.sub(r'\n', ' ', text) # replace newline with space
    text = re.sub(r'\s+', ' ', text) # remove extra spaces
    text = re.sub(r'^\s+|\s+$', '', text) # remove leading and trailing spaces
    text = re.sub(r'\s*\.\s*', '.\n', text) # add newline after fullstop
    text = re.sub(r'\s*,\s*', ', ', text) # add space after comma
    text = re.sub(r'\s*;\s*', '; ', text) # add space after semicolon
    text = re.sub(r'\s*:\s*', ': ', text) # add space after colon
    text = re.sub(r'\s*\?\s*', '? ', text) # add space after question mark
    text = re.sub(r'\s*!\s*', '! ', text) # add space after exclamation mark
    text = re.sub(r'\s*"\s*', '" ', text) # add space after double quote
    text = re.sub(r'\s*\'\s*', "' ", text) # add space after single quote
    text = re.sub(r'\s*-\s*', '- ', text) # add space after hyphen
    text = re.sub(r'\s*–\s*', '– ', text) # add space after en dash
    text = re.sub(r'\s*—\s*', '— ', text) # add space after em dash
    text = re.sub(r'\s*…\s*', '… ', text) # add space after ellipsis
    text = re.sub(r'\s*\(\s*', ' (', text) # add space before opening parenthesis
    text = re.sub(r'\s*\)\s*', ') ', text) # add space after closing parenthesis
    text = re.sub(r'\s*\[\s*', ' [', text) # add space before opening square bracket
    text = re.sub(r'\s*\]\s*', '] ', text) # add space after closing square bracket
    text = re.sub(r'\s*{\s*', ' {', text) # add space before opening curly brace
    text = re.sub(r'\s*}\s*', '} ', text) # add space after closing curly brace
    return text

for i in data:
    print('\n\n\n')
    for j in i:
        print(j)
