from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org/")
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all("div", {"class": "do-not-print"})
print(results)
