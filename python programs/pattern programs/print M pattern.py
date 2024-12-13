n = 7

for row in range(n):
    for col in range(n):
        if col == 0 or col == n-1 or (row == col and col > 0 and col < n//2) or (row == 1 and col == n-2) or (row == 2 and col == n-3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 7

for row in range(n):
    for col in range(n):
        if col == 0 or col == 6 or (row == col and col >0 and col <4) or (row== 1 and col == 5) or (row == 2, col == 4):
            print("*",end = " ")
        else:
            print(end = " ")
    print()
