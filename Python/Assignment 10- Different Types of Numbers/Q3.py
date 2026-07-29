# Assignment 10
# Question 3 : Display Numbers Ending with 5

a = int(input("Enter the  first Number : "))
b = int(input("Enter the second Number : "))


for i in range (a,b+1):
       if i%10==5:
             print(i, end=" ")

