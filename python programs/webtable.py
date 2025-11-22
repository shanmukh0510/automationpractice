from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")
numberofrows = driver.find_elements(By.XPATH,"//div[@class='rt-table']/div[@class='rt-thead -header']/div[@class='rt-tr']")
print(len(numberofrows))