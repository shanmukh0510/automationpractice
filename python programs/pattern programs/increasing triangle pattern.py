#input
n = 5

for row in range(0,n):
    for col in range(0,row+1):
        print("*", end = "  ")
    print()
