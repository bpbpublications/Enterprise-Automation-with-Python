from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.python.org/")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

