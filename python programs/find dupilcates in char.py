def find_duplicate_characters(input_string):
    duplicates = {}
    for char in input_string:
        if char in duplicates:
            duplicates[char] += 1
        else:
            duplicates[char] = 1
    return [char for char, count in duplicates.items() if count > 1]

name = "tester"
print(find_duplicate_characters(name))
