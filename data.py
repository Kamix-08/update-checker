import json, os, requests
import hashlib
from bs4 import BeautifulSoup

def load_data():
    with open("data.json", "r") as f:
        data = json.load(f)
        return (data["url"], data["selector"], data["webhook_url"])
    
# storing hashes is more efficient than storing the whole files
def hash(input: str) -> str:
    return hashlib.sha256(input.encode('utf-8')).hexdigest() 
    
def get_website(url, selector) -> str:
    return hash(str(BeautifulSoup(requests.get(url).content, 'html.parser').select_one(selector)))

def compare(url, selector) -> bool:
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
