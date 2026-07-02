# Assignment 14
# Question 1 : Multiplication Table Generator

n = int(input("Enter the limit : "))

for i in range(1, n+1):
    for j in range(1,n+1):
        print(i,"*",j,"=",i*j)

    print()    