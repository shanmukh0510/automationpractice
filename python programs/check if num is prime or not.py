#
# num = int(input("enter a number"))
# count = 0
# if num > 1:
#     for i in range(1,num+1):
#         if num % i == 0:
#             count = count + 1
#     if count == 2:
#         print("its a prime number")
#     else:
#         print("its not a prime number")
#
# num = int(input("enter a number"))
#
# count = 0
# if num > 1:
#     for i in range(1, num+1):
#         if num % i == 0:
#             count = count +1
#     if count == 2:
#         print("its a prime number ")
#     else:
#         print("its not a prime number")

import os
import shutil
path = input("Enter the path: ")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
    if os.path.exists(path+"/"+extension):
        shutil.move(path+"/"+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
