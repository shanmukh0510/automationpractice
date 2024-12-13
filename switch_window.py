from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
parent_window = driver.current_window_handle
driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
windows = driver.window_handles
for window in windows:
    driver.switch_to.window(window)
    print(driver.title)
    if driver.title == "QAClick Academy - A Testing Academy to Learn, Earn and Shine":
        course_button = driver.find_element(By.LINK_TEXT,"Access all our Courses").text
        print(course_button)
        driver.close()
        break
driver.switch_to.window(parent_window)
driver.close() 
<<<<<<< HEAD
=======

>>>>>>> origin/master
