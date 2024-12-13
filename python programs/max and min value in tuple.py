tuple = (20,10,15,18,55,77,92,2,12)

max = tuple[0]

n = len(tuple)

for i in range(1,n):
    if tuple[i] > max:
        max = tuple[i]
print(max)