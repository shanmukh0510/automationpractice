from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")

if "shirt" in driver.page_source:
    print("text found")
    print(driver.page_source)

else:
    print("text not found")

driver.quit()