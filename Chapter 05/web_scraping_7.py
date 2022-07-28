from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org/")
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.select_one('.do-not-print')
print(results)
