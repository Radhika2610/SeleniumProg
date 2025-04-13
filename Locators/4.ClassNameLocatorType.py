import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///H:/Radhika/Velocity/HTML/FileNameLocatorType.html")
time.sleep(2)

#Enter FN
driver.find_element(By.CLASS_NAME,"xyz123").send_keys("abc")
#Enter LN
driver.find_element(By.CLASS_NAME,"xyz123").send_keys("xyz")
time.sleep(15)

