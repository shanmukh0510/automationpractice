from datetime import time
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://localhost:2004/v30150.html")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//i[@class='fa fa-bell']").click()
notification = driver.find_element(By.XPATH,"//h3[@class='popover-header']").text
print(notification)
body = driver.find_element(By.XPATH,"//div[@class='popover-body']").text
print(body)

