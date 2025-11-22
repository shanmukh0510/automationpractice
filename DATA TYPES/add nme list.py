name1 = ["my", "name"]
name2 = ["is",  "john"]

name_list = name1 + name2

str_name = " ".join(name_list)
print(str_name)

list1 = ["a", "b", "c"]
list2 = [1,2,3]

output = dict(zip(list1,list2))
print(output)

keys_list = list(output.keys())
print(keys_list)

for key in output:
    print(key,output[key])
    
for value in output:
    print(value,output[value])



