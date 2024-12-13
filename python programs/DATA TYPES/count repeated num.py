my_list = [22,33,44,22,5,22,56,245,674,57,69,2]

len(my_list)
count = 0
for i in range(0,len(my_list)):
    if my_list[0] == my_list[i]:
        count = count + 1
print(count)