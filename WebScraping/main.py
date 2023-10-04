import requests
import bs4
result = requests.get("https://en.wikipedia.org/wiki/Mohanlal")
print(type(result))
soup = bs4.BeautifulSoup(result.text, 'lxml')
soup.text
