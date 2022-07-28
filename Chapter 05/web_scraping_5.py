from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org/")
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="nojs")
print(results.prettify())
