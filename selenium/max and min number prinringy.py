arr = [20,10,50,88,99,54,72]
max = arr[0]
n = len(arr)
for i in range(1,n):
    if arr[i]>max:
        max = arr[i]
print(max)


