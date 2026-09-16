# Assignment 15
# Question 8 : 

n = int(input("Enter the no. of lines : "))

for i in range(n,0,-1):
    print()
    for j in range(0,n-i):
        print(" ",end="") 

    for k in range(n,n-i,-1) :
        print(k,end="")   