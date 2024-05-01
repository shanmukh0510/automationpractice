# num1 = 1
# num2 = 2
#
# print(num1)
# print(num2)
# for i in range(3,100):
#     sum = num1+num2
#     print(sum)
#     num1=num2
#     num2=sum



num1 = int(input("enter a number "))
num2 = int(input("enter a number "))
n= 10
if num1 & num2 > n:
    print("its not in range")

for i in range(num1, n+1):
    sum = num1 + num2
    print(sum)
    num1 = num2
    num2 = sum
