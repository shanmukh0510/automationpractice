mystring =  "welcome to python programming world"

substring1 = "world"

substring2 = "worldabc"

if substring1 in mystring:
    print(f"{substring1} is present in {mystring}")
else:
    print(f"{substring1} is not present in {mystring}")

if substring2 in mystring:
    print(f"{substring2} is present in {mystring}")
else:
    print(f"{substring2} is not present in {mystring}")


