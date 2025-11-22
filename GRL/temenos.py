import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.temenos.com/")
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='onetrust-accept-btn-handler']")))
element.click()
# element = driver.find_element(By.XPATH,"//button[@id='onetrust-accept-btn-handler']")
# element.click()
driver.find_element(By.XPATH,"//a[@class='button button--default site-footer__insights-button-text']").click()
driver.implicitly_wait(10)
iframe = driver.find_element(By.XPATH,"//iframe[@type='text/html']")
driver.switch_to.frame(iframe)
#driver.find_element(By.XPATH,"//input[@id='768313_19679pi_768313_19679']").send_keys("shanmukharao9010@gmail.com")
driver.find_element(By.ID,"768313_19679pi_768313_19679").send_keys("shanmukharao9010@gmail.com")
driver.implicitly_wait(5)
dropdown_ele = driver.find_element(By.XPATH,"//select[@id='768313_19681pi_768313_19681']")
dropdown = Select(dropdown_ele)
all_options = dropdown.options
print(len(all_options))
for option in all_options:
    print(option.text)
    if option.text == "Zambia":
        option.click()
        break
driver.find_element(By.XPATH,"//div[@class='recaptcha-checkbox-border']").click()
time.sleep(10)

