# Assignment 17
# Pattern 78 : 

n = int(input("Enter the value of n : "))

mid = (n + 1) // 2

for i in range(1, mid + 1):
    for j in range(1, mid-i+1):
        print(" ", end="")

    for k in range(1, i + 1):
        print(k, end="")

    print()

for i in range(mid - 1, 0, -1):
     for j in range(1, mid-i+1):
        print(" ", end="")

     for k in range(1, i + 1):
        print(k, end="")

     print()