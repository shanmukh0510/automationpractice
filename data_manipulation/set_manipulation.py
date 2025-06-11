#SET Manipulation
my_set = {1,2,3,4}

another_set = {4, 5, 6}

# Basic Set Operations

my_set.add(5)
print(my_set)

#remove elements

my_set.remove(2)  # Raises KeyError if 2 is not found
my_set.discard(3) # No error if 3 not found
my_set.pop()    # Removes a random element
my_set.clear()       # Empties the set

 #Set Operations
#Union 
set1 = {1,2,3}
set2 =  {3,4,5}
union_set = set1 | set2
print(union_set)    #set1.union(set2)

#Intersection

intersection_set = set1 & set2
print(intersection_set)  #set1.intersection(set2)

#Difference

difference_set = set1 - set2   # Elements in set1 but not in set2
print(f"difference :{difference_set}")

# Symmetric Difference
sym_diff = set1 ^ set2          # Elements in either set, not both
print(f"symmetric difference : {sym_diff}")




