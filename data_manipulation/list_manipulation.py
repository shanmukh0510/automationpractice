#adding elements in a list

my_list = [1,2,3,4]
my_list.append(5)
print(my_list)

#addingb multipule elements

my_list.extend([6,7,8])
print(my_list)

#insert in a specific index

my_list.insert(2,99) # Inserts 99 at index 2
print(my_list)

#removing element

my_list.remove(4) # Removes first occurrence of 99
print(my_list)

#remove wlwment by index
poped_element = my_list.pop(2) # Removes element at index 2
print(poped_element)
print(my_list)

#clear entire list

my_list.clear()
print(my_list)


#accessing elements
#Indexing

my_list = [10,20,30,40]
print(my_list[1])

#Nehgative indexing

print(my_list[-1])
my_list[0] = 0
print(my_list)

#slicing
print(my_list[1:3])  #(from idex 1 to index 3)
print(my_list[:2])   #(from start to index 2)
print(my_list[::2])  #(every 2nd element)

#Sorting and Reversing

#Sort in ascending order
numbers = [5,2,9,1]
numbers.sort()
print(numbers)

#Sort in descending order
numbers.sort(reverse=True)
print(numbers)

#Sort without modifying original list

sorted_list = sorted(numbers)
print(f"sorted_ list:{sorted_list}")

#reverse list

numbers.reverse()
print(numbers)

#LIst Comprehensions

squared = [x**2 for x in range(5)]
print(squared)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

#count

my_list = [1,2,4,3,4,2]
print(my_list.count(4)) #counts occarance od an element

#find index of an element

print(my_list.index(3))

#Copy a list 

copy_list = my_list.copy()
print(copy_list)


# Using + Operator (Concatenation)

list1 = [1,2,3]
list2 = [4,5,6]
joined_list = list1 + list2
print(joined_list)

#Using extend() Method (Modifies Original List)

list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1)

#Using append() with a Loop (Adding Elements One by One)
list1 = [1,2,3]
list2 = [4,5,6]
for NUM in list2:
    list1.append(NUM)
print(list1)    
    








