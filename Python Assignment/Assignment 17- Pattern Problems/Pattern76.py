# Assignment 17
# Pattern 76 : 

n = int(input("Enter the value of n : "))

for i in range(0,n//2):
    for j in range(0,i+1):
        print("x", end="")
    print()    

for i in range(n//2,n+1):
    for j in range(n+1,i,-1):
        print("x", end="")

    print()