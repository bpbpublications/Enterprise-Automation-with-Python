from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# creating chrome driver servicer - the path is the location of your chromedriver
service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=webdriver.ChromeOptions())

# Opening chrome with Python website
driver.get("http://www.python.org")
