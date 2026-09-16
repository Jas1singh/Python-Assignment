# Assignment 17
# Pattern 84 : 

n = int(input("Enter the value of n : "))

for i in range(1, n + 1):
    for j in range(1,n-i+1):
        print(" ",end="")

    for k in range(i,0,-1):
         print(k,end="")

    for l in range(1,i):
        print(l+1,end="")         
    print()
