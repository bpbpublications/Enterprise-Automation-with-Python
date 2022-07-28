import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

print(x.text)

