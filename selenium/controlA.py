import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
driver.get("https://www.diffchecker.com/text-compare/")
driver.find_element(By.XPATH,"//div[@aria-label='Original text input']//div[@class='cm-line']").send_keys("shanmukh")
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# driver.find_element(By.XPATH,"//div[@aria-label='Changed text input']")
# actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(10)
