import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///H:/Radhika/Velocity/HTML/Webtable.html")
time.sleep(2)

allRows=driver.find_elements(By.XPATH,"//table[@id='Booklist']//tr")
print(len(allRows))

time.sleep(10)