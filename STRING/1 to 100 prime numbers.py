
prime_string = ""
num = 100
for num in range(1,num+1):
    count = 0
    for i in range(1, num+1):
        if num% i == 0:
            count +=1
    if count == 2:
        #prime_string += str(num)+ " "
        prime_string += str(num)

print(prime_string)
print(len(prime_string))
updated_string = ""
for i in range(len(prime_string)):
    if i % 4 != 0:
        updated_string +=prime_string[i]
print(updated_string)






