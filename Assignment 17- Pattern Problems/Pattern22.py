# Assignment 17
# Pattern 22 : 

n = int(input("Enter the value of n : "))

for i in range(n):
    for j in range(0,i+1):
        if i == n-1 or j == 0 or j == i:
            print(chr(65+j), end=" ")
        else:
            print(" ", end=" ")
    print()