from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://magento.softwaretestingboard.com/")
driver.find_element(By.XPATH,"//img[@src='https://magento.softwaretestingboard.com/pub/media/wysiwyg/home/home-performance.jpg']").click()
driver.find_element(By.XPATH,"//img[@alt='Sybil Running Short']").click()
driver.find_element(By.XPATH,"//div[@id='option-label-size-143-item-173']").click()
driver.find_element(By.XPATH,"//div[@id='option-label-color-93-item-57']").click()
quantity = driver.find_element(By.XPATH,"//input[@id='qty']").send_keys("3")
driver.find_element(By.XPATH,"//button[@id='product-addtocart-button']").click()
driver.find_element(By.XPATH,"//a[@class='action showcart']").click()
driver.find_element(By.XPATH,"//button[@id='top-cart-btn-checkout']").click()

