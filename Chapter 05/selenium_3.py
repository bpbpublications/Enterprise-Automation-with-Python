import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=webdriver.ChromeOptions())
driver.get("https://www.roboform.com/filling-test-all-fields")
first_name = driver.find_element(By.NAME, "02frstname")
first_name.send_keys("Ambuj")
company_name = driver.find_element(By.NAME, "05_company")
company_name.send_keys("ZappyAI")

time.sleep(15)
# close the chrome window
driver.close()
