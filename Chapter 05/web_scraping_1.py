from bs4 import BeautifulSoup
html_doc = """<!DOCTYPE html><html>
    <head> <title>Python Automation Example Page</title>
    </head>
    <body><p>Test Content for automation with Python.</p>
    </body></html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

