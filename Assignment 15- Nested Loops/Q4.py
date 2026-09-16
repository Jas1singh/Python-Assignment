# Assignment 15
# Question 4 : 

n = int(input("Enter the no. of lines : "))

for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        if i % 2==0:
            print("0",end=" ")

        else:
            print("i",end=" ")    