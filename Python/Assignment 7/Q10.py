# Assignment 7
# Question 10 : Even Numbers Between Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a <= b:
    if a % 2 == 0:
        print(a)

    a = a + 1

