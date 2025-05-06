num = int(input("enter a number"))
count = 0
if num > 1:
    for i in range(1,num+1):
        if num%i ==0:
            count = count+1
    if count == 2:
        print("its prime number")
    else:
        print("its not a prime number")


num = int(input("enetr a number"))

count = 0
for i in range(1, num + 1):
    if num%i == 0:
        count = count + 1
    if count == 2:
        print("its a prime number")
