import os

folder_path = r"C:\\GRL\\GRL-C3-MP-TPT"
os.startfile(folder_path)

# Check if the "Readme" file exists
release_file = os.path.join(folder_path, "GRL-C3-MP-TPT Release Notes.pdf")
if os.path.exists(release_file):
    print("Test passed: relese file exists.")
else:
    print("Test failed: relese file does not exist.")