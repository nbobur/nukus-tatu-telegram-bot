import requests
from bs4 import BeautifulSoup

def get_info():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

    }
    url="https://tatunf.uz/index.php?r=site%2Fmagliwmat&id=429"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
