import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com.mx/Nueva-Kindle-Paperwhite/dp/B08N3J8GTX/ref=sr_1_1?keywords=kindle&qid=1666372827&qu=eyJxc2MiOiIzLjIyIiwicXNhIjoiMy4yNSIsInFzcCI6IjMuNzkifQ%3D%3D&smid=AVDBXBAVVSXLQ&sprefix=kindl%2Caps%2C159&sr=8-1"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}


page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

#GET THE TITLE AND THE PRICE

title = soup.find(id="Title")
# price = soup.find(class_ = "a-offscreen")

print(title)
#print(price)
