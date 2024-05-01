import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
mouse_hover = driver.find_element(By.XPATH,"//button[@id='mousehover']")
Action = ActionChains(driver).move_to_element(mouse_hover)
Action.perform()
driver.find_element(By.LINK_TEXT,"Reload").click()
time.sleep(10)