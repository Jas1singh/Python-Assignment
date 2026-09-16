# Assignment 17
# Pattern 75 : 

n = int(input("Enter the value of n : "))

for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ", end="")

    for k in range(0,2*i-1):
            if i==n or k==0 or k==2*i-2:
                 print(k+1,end="")

            else:
                 print("+",end="")         

    print()