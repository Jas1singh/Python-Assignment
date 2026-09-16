# Assignment 17
# Pattern 82 : 

n = int(input("Enter the value of n : "))

mid = (n + 1) // 2

for i in range(1, mid + 1):
    for j in range(1,n-i+1):
        print(" ",end="")

    for k in range(1, 2*i):
        if i==1 or k==1 or k==2*i-1:
            print("*", end="")

        else:
            print("_",end="")    
    print()

for i in range(mid - 1, 0, -1):
    for j in range(1,n-i+1):
        print(" ",end="")

    for k in range(1, 2*i):
        if i==1 or k==1 or k==2*i-1:
            print("*", end="")

        else:
            print("_",end="")    
    
    print()