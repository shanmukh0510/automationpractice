#febnocci series

num1 =  int(input("enter a number"))
num2 =  int(input("enter a number"))

n = 10

if num1 & num2 > n:
    print("its not valid")
else:
    for i in range(num1, n+1):
        sum = num1 +num2
        print(num1)
        num1 = num2
        num2 = sum

num1 = int(input("enter a number"))

num2 = int(input("enter a number"))

n = 10

if num1 & num2 > n:
    print("its not valid")

else:
    for i in range(num1, n+1):
        sum = num1 +num2
        print(num1)
        num1 = num2
        num2 = sum