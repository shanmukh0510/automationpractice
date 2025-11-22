mystring = 'i have 12 apples 33 mangos with 2 melons'

alpha_string = "seleniumpython"

digit_string = "98788367873"
#Case conversion

print(mystring.lower())

print(mystring.upper())

print(mystring.capitalize())

print(mystring.title())

print(mystring.swapcase())


#Alignment and padding









#Searching and Checking

print(mystring.startswith("i"))

print(mystring.endswith("ons"))

print(mystring.find("12"))

print(mystring.index("melons"))

print(mystring.count("a"))

#Testing

print(alpha_string.isalpha())

print(digit_string.isdigit())

print(mystring.isalnum())

print(mystring.split())

print("".join(mystring.split()))


