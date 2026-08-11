import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    name = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()
    availability = book.find(
        "p", class_="instock availability"
    ).text.strip()

    rating = book.find("p", class_="star-rating")["class"][1]

    data.append({
        "Book Name": name,
        "Price": price,
        "Availability": availability,
        "Rating": rating
    })

df = pd.DataFrame(data)

df.to_csv("books.csv", index=False)

print("Books scraped successfully!")
print(f"Total books scraped: {len(df)}")
print("Data saved to books.csv")
