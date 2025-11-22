word = "level"
if word == word[::-1]:
    print(f"given string{word} is palindrome")
else:
    print(f"given string{word} is not palindrome")


def is_palindrome(mystring):
    if mystring == mystring[::-1]:
        return f"{mystring} is Palindrome string"
    else:
        return f"{mystring} is not a palindrome string"

#mystring = "level"
mystring = "Hello"
output = is_palindrome(mystring)
print(output)


def palindrome_check():
    word = "level"
    if word == word[::-1]:
        print(f"given string{word} is palindrome")
    else:
        print(f"given string{word} is not palindrome")

pc=palindrome_check()

def palindrome_check(word):

    if word == word[::-1]:
        print(f"given string{word} is palindrome")
    else:
        print(f"given string{word} is not palindrome")

pal_check=palindrome_check("level")
palindrome_check("hello")
palindrome_check("bananA")















