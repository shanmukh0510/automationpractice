mystring = 'i have 12 apples 33 mangos with 2 melons'
output = ' '
number = ''
for char in mystring:
    if char.isalpha():
        output = output + char
    else:
        number = number + char

print(output)
print(number)

number = number.split()
print(number)
###################################
mystring = 'i have 12 apples 33 mangos with 2 melons'
output = ''

for char in mystring:
    if char.isdigit():  # Check if the character is a digit
        output += char

print(output)
