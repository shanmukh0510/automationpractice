words  = "count occerance in a string"
letter_count = {}
for char in words:
    if char in letter_count:
        letter_count[char]+= 1
    else:
        letter_count[char] = 1
print(letter_count)
