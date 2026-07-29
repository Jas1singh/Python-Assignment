# Assignment 17
# Pattern 73 : 

n = int(input("Enter the value of n : "))

for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ", end="")

    for k in range(0,i):
            print(i,end=" ")    

    print()