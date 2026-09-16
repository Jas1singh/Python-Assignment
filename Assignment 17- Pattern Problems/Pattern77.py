# Assignment 17
# Pattern 77 : 

n = int(input("Enter the value of n : "))

mid = (n + 1) // 2

for i in range(1, mid + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(mid - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()