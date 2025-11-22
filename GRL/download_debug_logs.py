from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =  webdriver.Chrome()
driver.get("http://localhost:2004/v30150.html")
driver.find_element(By.XPATH,"//img[@id='navItem_Help']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@id='Ref3']").click()

note1_path = "D:\New folder\Debug_Log.txt"
note2_path = "C:\GRL\GRL-C3-MP-TPT\LogFiles\DebugLogger.log"

with open(note1_path, 'r') as f:
    note1_text = f.read()

with open(note2_path, 'r') as f:
    note2_text = f.read()

if note1_text == note2_text:
    print("The notes are identical!")
else:
    print("The notes are different.")

driver.quit()