import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=webdriver.ChromeOptions())
driver.get('https://www.google.com/?gws_rd=ssl')

# sleep timer to accept chrome terms and conditions and do some manual operations
time.sleep(5)
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('ChromeDriver')
search_box.submit()
