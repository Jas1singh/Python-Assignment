# Assignment 10
# Question 4 : Strong Number Checker

a = int(input("Enter the Number : "))

sum = 0
temp = a

while temp>0:
    digit = temp % 10 

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    temp = temp // 10


if sum == a:
    print("Strong Number")

else:
    print ("Not Strong Number")

