from bs4 import BeautifulSoup

html_doc = """<!DOCTYPE html><html>
    <head> <title>Python Automation Example Page</title>
    </head>
    <body><p>Test Content for automation with Python.</p>
    </body></html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

print("Document title is: " + str(soup.title))
print("Document title tag name is: " + soup.title.name)
print("Document title string is: " + soup.title.string)
print("Document title parent tag name is: " + soup.title.parent.name)
print("Document title paragraph is: " + str(soup.p))
