# Assignment 17
# Pattern 24 : 

n = int(input("Enter the value of n : "))

for i in range(n):
    for j in range(n):
        if i == n-1 or j == 0 or j == i:
            print("*", end=" ")
        else:
            if j>i:
                print(" ",end="")
            else:
                print("@", end=" ")
    print()