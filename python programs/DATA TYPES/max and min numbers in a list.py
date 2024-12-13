mylist = [4,33,66,200,100,55]
#max
max = mylist[0]

len(mylist)

for i in range(0,len(mylist)):
    if mylist[i] > max:
        max = mylist[i]
print(max)

#min

min = mylist[0]
for i in range(0,len(mylist)):
    if mylist[i] < min:
        min = mylist[i]
print(min)


