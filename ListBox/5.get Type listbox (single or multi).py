import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
time.sleep(4)

month=driver.find_element(By.XPATH,"//select[@id='month']")
s=Select(month)
print(s.is_multiple)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("file:///D:/6th%20July%202024/Selenium/html%20files/Sample4_Listbox.html")
time.sleep(2)

selectCountry=driver.find_element(By.XPATH,"//select[@id='abc123']") #WebElement Object
s=Select(selectCountry)
print(s.is_multiple)
time.sleep(5)