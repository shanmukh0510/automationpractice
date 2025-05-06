import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
browser = webdriver.Firefox()
browser.maximize_window()

# Open 2048 game
browser.get('https://gabrielecirulli.github.io/2048/')

# Find the correct element (body handles key events)
html_elem = browser.find_element(By.TAG_NAME, 'body')

# Infinite loop to play the game
while True:
    html_elem.send_keys(Keys.UP)
    time.sleep(0.2)  # Delay to prevent excessive input
    html_elem.send_keys(Keys.RIGHT)
    time.sleep(0.2)
    html_elem.send_keys(Keys.DOWN)
    time.sleep(0.2)
    html_elem.send_keys(Keys.LEFT)
    time.sleep(0.2)


