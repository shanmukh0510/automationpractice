# def find_duplicate_characters(input_string):
#     duplicates = {}
#     for char in input_string:
#         if char in duplicates:
#             duplicates[char] += 1
#         else:
#             duplicates[char] = 1
#
#     for char, count in duplicates.items():
#         if count > 1:
#           return duplicates
#
#     # return [char for char, count in duplicates.items() if count > 1]
#
# name = "tester"
# print(find_duplicate_characters(name))


name = "shanmukharao"
duplicates = {}
for char in name:
    if char in duplicates:
        duplicates[char] += 1
    else:
        duplicates[char] = 1
print(duplicates)
print(duplicates.items())
for key, value in duplicates.items():
    if value >= 2:
        print(f"{key} occurs {value} times")

