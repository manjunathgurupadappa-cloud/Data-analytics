import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    name = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()

    data.append({
        "Book Name": name,
        "Price": price,
        "Availability": availability
    })

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)

print("Books saved successfully!")