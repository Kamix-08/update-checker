import json, os, requests
from bs4 import BeautifulSoup

def load_data():
    with open("data.json", "r") as f:
        data = json.load(f)
        return (data["url"], data["selector"])
    
def get_website(url, selector):
    return str(BeautifulSoup(requests.get(url).content, 'html.parser').select_one(selector))

def compare(url, selector):
    if not os.path.isfile("html.txt"):
        with open("html.txt", "w") as f:
            f.write(get_website(url, selector))
            return False
        
    with open("html.txt", "r+", encoding="utf-8") as f:
        old_html = f.read()
        new_html = get_website(url, selector)

        if old_html != new_html:
            f.seek(0)
            f.write(new_html)
            f.truncate()
            return False
    
    return True
