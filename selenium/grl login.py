import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By

# with open('C:\GRL\GRL-C3-MP-TPT', 'r') as file:

driver = webdriver.Chrome()
driver.get("http://localhost:2004/v30136.html")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH, "//i[contains(text(),'×')]").click()
driver.find_element(By.XPATH, "//*[@class='rc-select-search__field']").send_keys("192.168.255.1")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@id='connectionsetup_connect_button']").click()
time.sleep(15)
ts = driver.find_element(By.XPATH, "(//*[@class='right-spacing-tester'])[1]").text
tsr = driver.find_element(By.XPATH, "//tbody/tr[1]//td[3]/div/b").text
print(ts)
print(tsr)
if tsr == "Connected":
    print("test passesd")
else:
    print("test failed")
with open('C:\GRL\GRL-C3-MP-TPT\ReadMe.txt', 'r') as file:
    for line in file:
        if line.startswith("Software Version"):
            swv = line.split(" : ")[1].strip()
            print(swv)

read_ver = driver.find_element(By.XPATH, "//*[@class='navbar-primaryText']").text
print(read_ver)
alldet = driver.find_element(By.XPATH, "//div[@class='device-details-container']").text
print(alldet)

data = {
    "alldet": alldet
}

# Write the dictionary to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

if swv in read_ver:
    print("Software versions match. Validation passed.")
else:
    print("Software versions do not match. Validation failed.")








