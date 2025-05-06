my_dict = {"city" : "banglore", "age": 40}

my_dic = dict(name = "alice",age = 45)

print(my_dic)
print(my_dict)
#access dictionary
print(my_dict["city"])
#update
my_dict["age"] = 50
print(my_dict)
#add
my_dict["name"] = "alice"
print(my_dict)
#iterate over a dictionary

for key in my_dict:
    print(key,my_dict[key])

for value in my_dict.values():
    print(value)

for key,value in my_dict.items():
    print(key,value)
#merge two dictionaries
merged_dict = my_dict | my_dic
print(merged_dict)

print(my_dict.update(my_dic))

my_dictt = {"name":"john","age":20,"city":"new york","job":"engineer"}

print(my_dictt)
print(my_dictt["name"])

#update
my_dictt["country"] = "USA"
print(my_dictt)

for key in my_dictt:
    print(f"{key} : {my_dictt[key]}")

for value in my_dictt:
    print(value, my_dictt[value])

for key,value in my_dictt.items():
    print(key ,value)

merged_dicts = my_dictt | my_dict
print(merged_dicts)

print(my_dictt.update(my_dict))