# Assignment 8
# Question 8 : Count Multiples of 5 Between Two Numbers

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

count = 0

for i in range(a, b + 1):
    if i % 5 == 0:
        count = count + 1

print("Count =", count)

