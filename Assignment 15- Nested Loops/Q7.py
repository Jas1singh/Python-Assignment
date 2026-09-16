# Assignment 15
# Question 7 : 

n = int(input("Enter the no. of lines : "))

for i in range(0,n):
    print()
    for j in range(1,n-i+1):
        print(" ",end="")

    for k in range(0,i+1) :
        print("*",end="")   