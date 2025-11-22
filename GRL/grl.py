from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Load JSON data from the specified path
try:
    with open(r'C:\Users\shanm\PycharmProjects\automation practice\GRL\grl.json', 'r') as rf:
        data = json.load(rf)
    print(json.dumps(data, indent=4))  # Print JSON structure for debugging
except FileNotFoundError:
    print("Error: JSON file not found at the specified path.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Failed to decode JSON file.")
    exit(1)

# Check if the necessary keys exist before accessing them
brand_info = data.get('Brand_Name', {})
if not brand_info:
    print("Error: 'Brand_Name' key is missing from the JSON file.")
    exit(1)

# Initialize WebDriver and interact with the webpage
try:
    with webdriver.Chrome() as driver:
        driver.get("http://localhost:2004/v30182.html")
        driver.maximize_window()

        # Wait until the "Test Configuration" image is clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='Test Configuration']"))).click()

        # Wait until the project name label is clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='project-name-label cursorPointer']"))).click()

        # Clear and enter a new project name
        project_name_input = driver.find_element(By.XPATH, "//input[@class='project-name-input panelcontrol textbox']")
        project_name_input.clear()
        project_name_input.send_keys("Sample")
        time.sleep(2)  # Sleep after entering project name

        # Click the primary button to proceed
        driver.find_element(By.XPATH, "//button[@class='grl-button btn btn-primary']").click()
        time.sleep(5)  # Wait for the next page to load

        # Loop through each key-value pair in the Brand_Name dictionary
        for key, value in brand_info.items():
            # Get the corresponding XPath for the current field
            xpath = data['Xpaths'].get(key)

            if xpath:
                # Wait for the input field to be clickable
                input_field = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                input_field.click()  # Ensure the input field is focused
                input_field.clear()  # Clear the input before sending new text
                input_field.send_keys(value)  # Input the value corresponding to the key

                # Optional: Print the value to confirm
                print(f"{key} entered:", value)

                time.sleep(2)  # Sleep after filling each field
            else:
                print(f"Warning: No XPath found for '{key}'.")
                # Optional: sleep for a short period before continuing
                time.sleep(1)

except Exception as e:
    print(f"An error occurred: {e}")