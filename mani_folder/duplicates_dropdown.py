from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice.expandtesting.com/dropdown")

# Find the dropdown by its ID and wrap it in a Select object
select_element = Select(driver.find_element(By.ID, "country"))

# Get all available options in the dropdown
options = select_element.options

# Extract text from each option
option_texts = [option.text for option in options]

# Initialize a set to track unique items
seen = set()
duplicates = []

# Check for duplicates
for option in option_texts:
    if option in seen:
        duplicates.append(option)
    else:
        seen.add(option)

if duplicates:
    print("Duplicate items found in the dropdown:", duplicates)
else:
    print("No duplicate items found in the dropdown.")

driver.quit()
