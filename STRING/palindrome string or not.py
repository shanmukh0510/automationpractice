def is_palindrome(mystring):
    if mystring == mystring[::-1]:
        return f"{mystring} is Palindrome string"
    else:
        return f"{mystring} is not a palindrome string"

#mystring = "level"
mystring = "Hello"
output = is_palindrome(mystring)
print(output)


