import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///H:/Radhika/Velocity/HTML/Webtable.html")
time.sleep(2)

bookName=driver.find_element(By.XPATH,"//table[@id='abc123']//td[text()='100']//parent::tr/td[3]").text
print(bookName)

time.sleep(10)