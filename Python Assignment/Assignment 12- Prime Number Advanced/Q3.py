# Assignment 12
# Question 3 : Perfect Number Reward System

n = int (input("Enter the Number : "))
temp = n
sum = 0
# count = 0

for i in range(1,n):
    if temp % i==0:
        # count = count + 1
        sum = sum + i   
 
if sum==n:
    print("Reward Unlocked")

else:
    print("Try Again")   