
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
wait = WebDriverWait(driver,10)
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='checkBoxOption1']")))
checkbox.click()
if checkbox.is_selected():
    print("Test passed")
else:
    print("Test failed")

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)
check_boxes = wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='checkbox']")))

#check_boxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
#method 1
print(len(check_boxes))
# for check in check_boxes:
#     check.click()
#method 2
for i in range(len(check_boxes)):
    check_boxes[i].click()
driver.implicitly_wait(10)

if check_boxes.is_selected():
    print("Test passed")
else:
    print("Test failed")


