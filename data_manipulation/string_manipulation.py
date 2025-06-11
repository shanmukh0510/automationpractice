#Concatenation (Joining Strings)

str1 = "Hello"
str2 = "world"
result =  str1 + " " + str2
print(result)

#String Repetition

str1 = "Hello"
print(str1 * 3)

#String Slicing

text = "Python Programming"
print(text[0:6])     # Output: Python
print(text[:6])      # Output: Python (same as above)
print(text[7:])      # Output: Programming
print(text[-3:])     # Output: ing (last 3 characters)[-3:-1]
print(text[::-1])    # Output: gnimmargorP nohtyP (reverse string)

# Changing Case
name = "shanmukh"
text = "hello world"
print(text.upper())
print(text.lower())
print("-".join(name))
print(text.title())
print(text.capitalize())
print(text.swapcase())

# Checking String Content

text = "Python123"
print(text.isalpha())    #False
print(text.isdigit())   #False
print(text.isalnum())    #True
print(text.isspace())    #False
print(text.startswith("Py")) #True
print(text.endswith("123"))  #True

#Replacing Substrings

text = "I Love Python"
text.replace("python","Java")
print(text)

#Splitting and Joining Strings

text = "apple"
letters = list(text)
print(letters) #output: ['a', 'p', 'p', 'l', 'e']

#Splitting a String into a List
text = "apple,banana,orange"
words = text.split(",")
print(words)

#Joining a List into a String
words = ["apple","banana","orange"]
joined = "-" .join(words)
print(joined)

#Removing Spaces

text = "  helllo world  "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#Finding Substrings
text = "python is fun"
print(text.find("python"))
print(text.index("is"))
print(text.count("o"))

NAME = "shanmukh python learning"
print(list(NAME))
print(NAME.split(" "))