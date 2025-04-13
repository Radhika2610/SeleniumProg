import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///H:/Radhika/Velocity/HTML/LinkText%20&%20PartialText%20Locator%20Type.html")
time.sleep(2)

#click on facebook link
#driver.find_element(By.LINK_TEXT,"facebook").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"book").click()

time.sleep(5)
