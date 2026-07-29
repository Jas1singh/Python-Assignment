# Assignment 8
# Question 4 : Numbers Divisible by 3 Between Two Numbers

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

for i in range(a, b + 1):
    if i % 3 == 0:
        print(i)