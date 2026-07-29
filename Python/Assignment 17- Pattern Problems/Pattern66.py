# Assignment 17
# Pattern 66 : 

n = int(input("Enter the value of n : "))

for i in range(0,n):
    for j in range(1,n-i+1):
        print(" ", end="")

    for k in range(0,2*i+1):
        if i==0 or i==n-1 or k==0 or k==2*i:
            print("1", end="") 
        else:
            print("*",end="")    

    print()