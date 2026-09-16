# Assignment 10
# Question 5 : Harshad Number Checker

num = int(input("Enter the Number : "))

temp = num
sum = 0

while temp>0:
    digit = temp % 10

    sum = sum + digit
    temp = temp // 10

if num % sum==0:
    print("Harshad Number")

else:
    print("Not Harshad Number")        




