#TUPLES

t = (1, 2, 3)
single_item = (5,)  # Don't forget the comma for single-element tuples

# Accessing Elements

print(t[0])
print(t[-1])

# Unpacking Tuples
a,b,c = t
print(a,b,c)

#Concatenation and Repetition

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)   # (1, 2, 3, 4)

print(t1 * 2)    # (1, 2, 1, 2)

# Searching and Counting

t = (1, 2, 3, 2, 4)

print(t.count(2))     # 2
print(t.index(3))     # 2

# Check Membership

if 2 in t:
    print("found")
    
#Convert Tuple to List (for editing)

t = (1,2,3)
temp = list(t)
temp.append(4)
t = tuple(temp)

#Tuple as Dictionary Key
