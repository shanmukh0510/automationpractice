
num =  [1, 2, 5, 7, 10]
output = []
for i in range(1,11):
    if i not in num:
        output.append(i)
print(output)

combined_list = num + output
combined_list.sort()
print(combined_list)

