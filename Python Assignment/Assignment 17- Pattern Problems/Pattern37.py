# Assignment 17
# Pattern 37 : 

n = int(input("Enter the value of n : "))

for i in range(n,0,-1):
    for j in range(i):
        if i %2==0:
            print("#", end="")
        else:
            print("*",end="")    
    print()