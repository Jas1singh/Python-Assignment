# Assignment 10
# Question 2 : Count Numbers Divisible by 7 Between Two Numbers

a = int(input("Enter the  first Number : "))
b = int(input("Enter the second Number : "))

count = 0 

for i in range (a,b+1):
    if i % 7==0:
        count = count + 1

print ("Count = ",count)