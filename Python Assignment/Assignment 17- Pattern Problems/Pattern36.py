# Assignment 17
# Pattern 36 : 

n = int(input("Enter the value of n : "))

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n-i-1:
            print(chr(65+j), end="")
        else:
            print(" ", end="")
    print()