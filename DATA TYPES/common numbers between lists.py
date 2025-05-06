def common_numbers(list1,list2):
    common_numbs = []
    for num in list1:
        if num in list2:
            common_numbs.append(num)
    return common_numbs
list1 = [100, 2, 333, 44, 555]
list2 = [123, 88, 44, 448, 5998]
output = common_numbers(list1,list2)
print(output)


#common numbers between lists, using sets


list1 = [100, 2, 333, 44, 555]
list2 = [123, 88, 44, 448, 5998]

common_numbers = set(list1) & set(list2)
print(list(common_numbers))
