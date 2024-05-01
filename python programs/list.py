 def print_common_numbers(list1, list2):
    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)

    # Find intersection of sets
    common_numbers = set1 & set2

    # Print common numbers
    for number in common_numbers:
        print(number)

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print_common_numbers(list1, list2)
#
# def print_common_numbers(list1, list2):
#     # Create an empty list to store common numbers
#     common_numbers = []
#
#     # Iterate over the first list
#     for number in list1:
#         # If a number in the first list is also in the second list and not already in the common_numbers list
#         if number in list2 and number not in common_numbers:
#             # Append the number to the common_numbers list
#             common_numbers.append(number)
#
#     # Print common numbers
#     for number in common_numbers:
#         print(number)
#
# # Test the function
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# print_common_numbers(list1, list2)
