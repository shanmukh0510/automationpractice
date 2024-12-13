def common_numbers(list1,list2):
    for item in list1:
        if item in list2:
            return True
    return False
list1 = [100, 2, 333, 44, 555]
list2 = [123, 88, 44, 448, 5998]
output = common_numbers(list1,list2)
print(output)

