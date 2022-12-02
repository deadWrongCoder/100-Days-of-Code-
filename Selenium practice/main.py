from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

s=Service('/home/user/Downloads/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("https://www.youtube.com/")
search = driver.find_element("name", "search_query")
search.send_keys(("How to learn Python"))
search.send_keys(Keys.ENTER)


time.sleep(10)
