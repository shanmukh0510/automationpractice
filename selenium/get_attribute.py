from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://platform.testlio.com/login#/")
username = driver.find_element(By.XPATH,"//input[@placeholder='Email']")
print(username.get_attribute("class"))
