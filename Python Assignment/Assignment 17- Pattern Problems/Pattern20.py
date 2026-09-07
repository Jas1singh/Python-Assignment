# Assignment 17
# Pattern 20 : 

n = int(input("Enter the value of n : "))

for i in range(n+1):
    for j in range(1,i+1):
        if i == n or j == 1 or j == i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()