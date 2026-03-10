mystring = 'i have 12 apples 33 mangos with 2 melons'
# output = ' '
# number = ''
# for char in mystring:
#     if char.isalpha():
#         output = output + char
#     else:
#         number = number + char
#
# print(output)
# print(number)
#
# number = number.split()
# print(number)
strings = ""
numbers = ""
for i in mystring:
    if i.isdigit():
        numbers = numbers + i
    else:
        strings = strings + i

print(numbers)
print(strings)




