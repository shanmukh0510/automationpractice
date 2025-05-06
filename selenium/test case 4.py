import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("shanmukh")
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.accept()
time.sleep(10)
driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.accept()
time.sleep(10)


