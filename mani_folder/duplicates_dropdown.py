from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the URL
driver.get("https://practice.expandtesting.com/dropdown")

# Find the dropdown and click to open it
dropdown_element = driver.find_element(By.ID, "country")
dropdown_element.click()

# Locate the dropdown by its ID using Select
select_element = Select(dropdown_element)

# Iterate through the options to find and select 'India'
for option in select_element.options:
    if option.text.lower() == "india":  # case-insensitive comparison
        select_element.select_by_visible_text("India")  # Select the option
        print("Clicked on India")
        break

# Wait for 10 seconds to observe the result
time.sleep(10)

# options = select_element.options

# # Extract text from each option
# option_texts = [option.text for option in options]

# # Initialize a set to track unique items
# seen = set()
# duplicates = []

# # Check for duplicates
# for option in option_texts:
#     if option in seen:
#         duplicates.append(option)
#     else:
#         seen.add(option)

# if duplicates:
#     print("Duplicate items found in the dropdown:", duplicates)
# else:
#     print("No duplicate items found in the dropdown.")

# driver.quit()


#