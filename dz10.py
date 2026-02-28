import requests
import re

for page in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    html = response.text

    titles = re.findall(r'title="(.*?)"', html)

    for title in titles:
        print(title)