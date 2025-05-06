mylist1 = ['apple', 'mango', 'cherry', 'apple', 'banana', 'plum']
mylist2 = ['pineapple', 'mango', 'cherry', 'watermelon', 'orange', 'mango']
mylist1 = set(mylist1)
unique_list1 = []
for fruit in mylist1:
    if fruit not in mylist2:
        unique_list1.append(fruit)
print(unique_list1)

unique_list2 = []

for fruit in mylist2:
    if fruit not in mylist1:
        unique_list2.append(fruit)
print(unique_list2)