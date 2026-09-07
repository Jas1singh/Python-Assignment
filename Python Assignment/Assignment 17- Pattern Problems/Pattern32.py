# Assignment 17
# Pattern 32 : 

n = int(input("Enter the value of n : "))

for i in range(n,0,-1):
    for j in range(i):
        print(i, end="")
    print()