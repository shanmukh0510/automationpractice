import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ultimateqa.com/filling-out-forms/")
driver.find_element(By.XPATH,"//input[@id='et_pb_contact_name_0']").send_keys("shanmukh")
driver.find_element(By.XPATH,"//textarea[@id='et_pb_contact_message_0']").send_keys("text entered")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@name='et_builder_submit_button'][1]").click()
time.sleep(5)
message = driver.find_element(By.XPATH,"//div[@class='et-pb--messagecontact']//p")
time.sleep(5)
print(message.text)
if message.text == "Thanks for contacting us":
    print("test passed")
else:
    print("test failed")