# itarative method

num = int(input("enter a number : "))

factorial = 1

if num < 0:
    print("its not a valid number")

if num == 0:
    print("factorial of 0 is equal to 1")

else:
    for i in range(1,num+1):
        factorial = factorial * i
    print(factorial)





