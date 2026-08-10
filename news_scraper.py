import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.ycombinator.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(".titleline a")

data = []

for title in titles:
    data.append({
        "Title": title.text,
        "Link": title["href"]
    })

df = pd.DataFrame(data)

df.to_csv("news.csv", index=False)

print("News saved successfully!")