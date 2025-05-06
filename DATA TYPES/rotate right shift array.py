list = [1,2,3,4,5,6,7]

print(list[-3::],list[0:4])

combine_list = list[-3::]+list[0:4]

print(combine_list)


num_list = [1,2,3,4,5,6,7,8,9,20]

odd_num = []
even_num = []

for num in num_list:
    if num % 2 == 1:
        odd_num.append(num)

    if num % 2 == 0:
        even_num.append(num)
print(odd_num)
print(even_num)

updated_list = odd_num + even_num
print(updated_list)