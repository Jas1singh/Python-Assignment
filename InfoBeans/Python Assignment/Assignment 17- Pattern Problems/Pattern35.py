# Assignment 17
# Pattern 35 : 

n = int(input("Enter the value of n : "))

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n-i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()