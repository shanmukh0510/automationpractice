# itarative method
num = 100
factorial = 1
if num<0:
    print("its not valid")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print(factorial)


# resursive method
