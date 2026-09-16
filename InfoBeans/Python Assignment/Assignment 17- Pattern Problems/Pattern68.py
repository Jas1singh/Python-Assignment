# Assignment 17
# Pattern 68 : 

n = int(input("Enter the value of n : "))
 
for i in range(0,n):
    for j in range(1,n-i+1):
        print(" ", end="")

    for k in range(0,2*i+1):
        if i==k:
            print("#", end="") 
        else:
            print("*",end="")    

    print()
