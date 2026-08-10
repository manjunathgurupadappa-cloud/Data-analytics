import io
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Wrap response.text in io.StringIO to remove the warning
tables = pd.read_html(io.StringIO(response.text))

print("Number of tables found:", len(tables))

df = tables[0]
print(df.head())

df.to_csv("Task_1_Web_Scraping/countries_population.csv", index=False)
print("Table saved successfully!")