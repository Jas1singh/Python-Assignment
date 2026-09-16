# Assignment 10
# Question 10 : Prime Security Code Checker

num = int(input("Enter the Number : "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print("Prime Number")
    
else:
    print("Not Prime Number")