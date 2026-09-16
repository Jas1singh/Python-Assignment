# Assignment 17
# Pattern 86 : 

n = int(input("Enter the value of n : "))

for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")

    for k in range(2*(n-i)+1):
         print(" ",end="")

    for l in range(i):
        print("*",end="")         
    print()