s ="shanmukha"

l_name = list(s)
print(l_name)
l_name = list(set(l_name))

output = "".join(l_name)

print(output)
s ="shanmukha"
l_name = list(s)
print(l_name)

l_name = []
for char in s:
    if char not in l_name:
        l_name.append(char)
print(l_name)




