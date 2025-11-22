list = [20,10.55,32,84,71]
# first = list[0]
# list[0] = list[-1]
# list[-1]= first
# print(list)
n = len(list)

first = list[0]
list[0]= list[n-1]
list[n-1]= first
print(list)