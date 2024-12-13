num =  [1, 2, 5, 7, 10]
output = []

for i in range(1,11):
    if i not in num:
        output.append(i)
print(output)

combined = num + output
combined.sort()
print(combined)



