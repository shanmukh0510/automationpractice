# file_path = r"C:\Users\shanm\Downloads\sample1 (1).json"

# with open(file_path, "r") as file:
#     data = file.read()
#     print(data)

import json
file_path = r"C:\Users\shanm\Downloads\sample1 (1).json"
with open(file_path,"r") as file:
    data = json.load(file)
    print(data)




    
    
    
