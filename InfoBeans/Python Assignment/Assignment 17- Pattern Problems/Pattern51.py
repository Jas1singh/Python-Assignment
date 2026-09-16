# Assignment 17
# Pattern 51 : 

n = int(input("Enter the value of n : "))
x=5
for i in range(1,n+1):
    for j in range(1,i):
        print(" ", end="")

    for k in range(1,n+2-i):
        print(x,end="")
    x-=1    
    print()