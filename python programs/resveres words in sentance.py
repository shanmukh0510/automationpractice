line = "python programming language"
new_list = line.split()
print(new_list)
for i in range(len(new_list)):
    new_list[i] = new_list[i][::-1]
string_line = " ".join(new_list)
print(string_line)
# reversed = new_list[0][::-1]+" "+new_list[1][::-1]+" "+new_list[2][::-1]
# print(reversed)
# string_line = " ".join(reversed)
# print(string_line)
# print(type(string_line))


