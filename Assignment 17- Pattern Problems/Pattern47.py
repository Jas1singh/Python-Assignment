# Assignment 17
# Pattern 47 : 

n = int(input("Enter the value of n : "))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ", end="")

    for k in range(1,i+1):
        if k==i or k==1 or i==n:
            print("1",end="")  
        else:      
            print("*",end="")    
    print()