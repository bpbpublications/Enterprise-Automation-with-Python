from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org/")
soup = BeautifulSoup(page.content, 'html.parser')

# Get all the external links comtained in the HTML page
for link in soup.find_all('a'):
    print(link.get('href'))
