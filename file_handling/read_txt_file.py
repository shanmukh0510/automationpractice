#Read entire file

file = open(r"C:\Users\shanm\Downloads\long-doc.txt","r")
content = file.read()
print(content)
file.close()

#read lone by line

file = open(r"C:\Users\shanm\Downloads\long-doc.txt","r")
for line in file:
    print(line.strip())
file.close()

#read all lines as list

file = open(r"C:\Users\shanm\Downloads\long-doc.txt","r")
lines = file.readlines()
print(lines)
file.close()

#writing into files

file = open(r"C:\Users\shanm\Downloads\long-doc.txt","w")
file.write("hello \n")
file.close()


#append(adds content)
file = open(r"C:\Users\shanm\Downloads\long-doc.txt","a")
file.write("appending new line\n")
file.close()


#using with statement is the best practice

with open(r"C:\Users\shanm\Downloads\long-doc.txt","r") as file:
    content = file.read()
    print(content)


