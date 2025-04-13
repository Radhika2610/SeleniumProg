import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.find_element(By.XPATH,"//img[@class='fb_logo _8ilh img']").screenshot("H:\Radhika\Velocity\screenshort\logo.png")

time.sleep(5)