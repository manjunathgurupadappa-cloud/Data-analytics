import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://coinmarketcap.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Website loaded successfully!")
else:
    print("Website blocked the request.")