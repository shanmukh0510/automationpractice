import time
from selenium import webdriver

# Initialize ChromeDriver
driver = webdriver.Chrome()

# Navigate to Google
driver.get('http://www.google.com/')

# Find the search box element and enter the search query
search_box = driver.find_element("name", "q")
search_box.send_keys('ChromeDriver')
search_box.submit()

# Wait for a minute (60 seconds) to let the user see the search results
time.sleep(60)

# Close the browser window
driver.quit()
