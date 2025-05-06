from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

# download_dir = os.path.join(os.path.expanduser(''), 'Download')
file_name = "samplefiljuirtyuuyite.pdf"

file_path = os.path.join(download_dir, file_name)

url = "https://demo.automationtesting.in/FileDownload.html"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

time.sleep(5)

# driver.find_element(By.LINK_TEXT, "Download").click()
# time.sleep(50)
 
if os.path.exists(file_path):
    print("file exists")
else:
    print("file  not exists")