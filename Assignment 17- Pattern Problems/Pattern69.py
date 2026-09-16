# Assignment 17
# Pattern 69 : 

n = int(input("Enter the value of n : "))

for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ", end="")

    for k in range(0,2*i-1):
            print("*",end="")    

    print()
