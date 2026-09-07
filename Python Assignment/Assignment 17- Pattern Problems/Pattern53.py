# Assignment 17
# Pattern 53 : 

n = int(input("Enter the value of n : "))
x=5
for i in range(1,n+1):
    for j in range(1,i):
        print(" ", end="")

    for k in range(1,n+2-i):
        if k==1 or i==1 or k==n+1-i:
            print(x,end="")

        else:      
            print("_",end="")   
    x-=1    
    print()