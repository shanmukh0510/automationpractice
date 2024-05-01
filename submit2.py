import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ultimateqa.com/filling-out-forms/")
driver.find_element(By.XPATH,"//input[@name='et_pb_contact_name_1']").send_keys("shanmukh")
driver.find_element(By.XPATH,"//*[@id='et_pb_contact_message_1']").send_keys("text entered")
time.sleep(5)


texts = driver.find_element(By.XPATH, "//span[@class='et_pb_contact_captcha_question']").text

new_text = texts.split(' ')
num1=int(new_text[0])
num2 = new_text[1] 
num3=int(new_text[2])
print(num1,num2)

in_value = num1, num2, num3

driver.find_element(By.XPATH, "//input[@class='input et_pb_contact_captcha']").send_keys(in_value)
time.sleep(5)
driver.find_element(By.XPATH, "(//button[@class='et_pb_contact_submit et_pb_button'])[2]").click()
time.sleep(5)



