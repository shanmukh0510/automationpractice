from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()

driver.get("http://localhost:2004/v30150.html")
time.sleep(5)
driver.maximize_window()

driver.find_element(By.XPATH, "//*[text()='Test Configuration']").click()
time.sleep(5)
# driver.find_element(By.XPATH, "//*[text()='Test Configuration']").click()

action = ActionChains(driver)

clc = driver.find_element(By.XPATH, "//span[@class='project-name-label cursorPointer']")
action.double_click(clc).perform()

# clc = driver.find_element(By.XPATH, "//span[@class='project-name-label cursorPointer']")
# action.double_click(clc).perform()


ele = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]")
value = ele.get_attribute('maxlength')

print(value)