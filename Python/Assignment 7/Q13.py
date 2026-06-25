# Assignment 7
# Question 13 : Number Range Display System

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    for i in range(a, b + 1):
        print(i, end=" ")

elif a > b:
    for i in range(a, b - 1, -1):
        print(i, end=" ")

else:
    print("Both numbers are same")

