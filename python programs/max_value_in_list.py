list = [5,3,8,11,3,18,53,1,100]
max_num = max(list)
print(max_num)

list = [5,3,8,11,3,18,53,1,100]

max = list[0]
n = len(list)
for i in range(0,n):
    if list[i]>max:
        max = list[i]
print(max)


