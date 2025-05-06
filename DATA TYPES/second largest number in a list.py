def second_largest_num(mylist):
    mylist.sort()
    print(mylist)
    return mylist[-2]
mylist = [11,33,22,10,123,55,300]
output = second_largest_num(mylist)


