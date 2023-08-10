import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s=Service('/usr/local/bin/chromedriver')
driver=webdriver.Chrome()
driver.get("https://www.codechef.com/")
while True:
    time.sleep(7)
    driver.refresh()
