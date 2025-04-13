import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///H:/Radhika/Velocity/HTML/Tagname%20locator.html")
time.sleep(2)

#Enter FN
driver.find_element(By.TAG_NAME,"input").send_keys("abc")
#Enter LN
driver.find_element(By.TAG_NAME,"input").send_keys("xyz")
time.sleep(15)

