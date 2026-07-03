# Assignment 15
# Question 9 : 

n = int(input("Enter the no. of lines : "))

for i in range(1,n+1):
    print()
    for j in range(1,n-i+1):
        print(" ",end="")
    
    for k in range(0,i):
        if k % 2==0:
            print(k,end=" ")

        else:
            print(k+1,end=" ")    