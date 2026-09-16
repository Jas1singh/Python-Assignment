# Assignment 14
# Question 1 : Multiplication Table Generator

n = int(input("Enter the range : "))
limit = int(input("Enter the Limit : "))

for i in range(1, n+1):
    
    for j in range(1,limit+1):
        print(i,"*",j,"=",i*j)

    print()    