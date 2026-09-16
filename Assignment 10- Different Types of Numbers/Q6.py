# Assignment 10
# Question 6 : Automorphic Number Checker

num = int(input("Enter the Number : "))

squre = num * num

count = 0
temp = num

while temp>0:
       count = count + 1
       temp = temp // 10

if squre%(10**count)==num:
       print("Automorphic Number")

else:
       print("Not Automorphic Number ")



