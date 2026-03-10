
# area = 0.5 * b * h

# b= int(input("enter a number :"))
#
# h = int(input("enter a number :"))
#
# area = 0.5 * b * h
# print("the area of the triangle is ", area)

# check if the number is prime or not

# number should be divisible 1 and by itself
def check_num_is_prime():
    number = int(input("enter a number :"))  # 17
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count = count + 1

    if count == 2:
        print("its prime number")
    else:
        print("its not prime number")

prime_check = check_num_is_prime()









