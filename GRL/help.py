from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =  webdriver.Chrome()
driver.get("http://localhost:2004/v30150.html")
driver.find_element(By.XPATH,"//img[@id='navItem_Help']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@id='Ref1']").click()
parent_window = driver.current_window_handle
time.sleep(5)
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    if driver.title == "Knowledge Base | Create Support Ticket":
        print(f"test passed:",{driver.title})
        break
    else:
        print("test failed")
driver.switch_to.window(parent_window)
driver.close()
        

    


