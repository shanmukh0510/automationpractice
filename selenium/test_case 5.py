import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
rows = driver.find_elements(By.XPATH,"//table[@class='table-display']//tr")
print(len(rows))
columns = driver.find_elements(By.XPATH,"//table[@class='table-display']//tr[1]/th")
print(len(columns))
time.sleep(20)

#Read  all the rows and column data
for i in range(1,12):
    for c in range(1,4):
        # wait = WebDriverWait(driver,10)
        # all_data = wait.until(EC.element_to_be_clickable(By.XPATH,"//table[@class='table-display']//tr["+ str(i) +"]/td["+ str(c) +"]"))
        driver.implicitly_wait(10)
        all_data = driver.find_element(By.XPATH,"//table[@class='table-display']/tbody/tr['+ str(i) +']/td['+ str(c) +']") #//table[@class="table-display"]/tbody/tr[5]/td[2]
        alldata = all_data.text
        print(alldata, end= "  ")

