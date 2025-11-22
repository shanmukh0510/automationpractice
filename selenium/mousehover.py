from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/tooltip/")
frame_ele = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(frame_ele)
mouse = driver.find_element(By.XPATH,"//input[@id='age']")
action = ActionChains(driver)
action.move_to_element(mouse).perform()
mouse.send_keys("25")
hidden = driver.find_element(By.XPATH,"//div[@style='display: none;''][1]").text
print(hidden)
time.sleep(5)
driver.switch_to.default_content()
driver.close()
 