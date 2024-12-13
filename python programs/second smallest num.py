num = [10,1,3,1,1,4,5,9]
num = list(set(num))
print(num)
num.sort()
max = num[0]

n = len(num)

for i in range(1,n):
    if num[i] > max:
        max = num[i]

print(max)
print(num[1])




