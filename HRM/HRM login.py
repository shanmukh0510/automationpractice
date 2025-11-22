from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from HRM import Utils

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)
driver.maximize_window()

try:
    file_path = r"E:\Book1.xlsx"
    total_rows = Utils.getRowCount(file_path, "Sheet1")

    for row in range(2, total_rows + 1):
        username = Utils.ReadDataFromExcel(file_path, "Sheet1", row, 1)
        password = Utils.ReadDataFromExcel(file_path, "Sheet1", row, 2)

        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        username_input.send_keys(username)

        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        password_input.send_keys(password)

        driver.find_element(By.XPATH, "//*[@type='submit']").click()

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()