# importing the requests library
import requests

# Multiple URLs
multiple_urls = {
    "python_logo.png": "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png",
    "python.html": "https://www.python.org/"
}
for file_name, url in multiple_urls.items():
    response = requests.get(url)
    with open(file_name, "wb") as file:
        file.write(response.content)
