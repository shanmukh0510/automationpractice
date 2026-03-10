words  = "count occerance in a string"
# letter_count = {}
# for char in words:
#     if char in letter_count:
#         letter_count[char]+= 1
#     else:
#         letter_count[char] = 1
# print(letter_count)

letter_count = {}

for i in words:
    if i in letter_count:
        letter_count[i] = letter_count[i] + 1

    else:
        letter_count[i] = 1

print(letter_count)


