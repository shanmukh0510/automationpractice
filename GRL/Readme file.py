import os
<<<<<<< HEAD
=======
from selenium import webdriver




driver = webdriver.Chrome()

driver.maximize_window()
>>>>>>> origin/master

folder_path = r"C:\\GRL\\GRL-C3-MP-TPT"
os.startfile(folder_path)

<<<<<<< HEAD
=======
driver.implicitly_wait(5)

>>>>>>> origin/master
# Check if the "Readme" file exists
readme_file = os.path.join(folder_path, "Readme.txt")
if os.path.exists(readme_file):
    print("Test passed: Readme file exists.")
else:
    print("Test failed: Readme file does not exist.")

<<<<<<< HEAD
=======
driver.quit()
>>>>>>> origin/master






