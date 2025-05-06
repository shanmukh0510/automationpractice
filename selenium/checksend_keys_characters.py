from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
elem = driver.find_element(By.XPATH,"//input[@id='name']")

maxlength = elem.get_attribute('maxlength')
print(f"Maximum characters allowed: {maxlength}")

if maxlength:
    max_chars = int(maxlength)
    input_string = "a" * max_chars
    elem.send_keys(input_string)
    print("Input string sent successfully")
else:
    print("No maxlength attribute found")