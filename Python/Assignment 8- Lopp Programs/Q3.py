# Assignment 8
# Question 3 : First Digit of Number

number = int(input("Enter your number : "))

while number>= 10:
    number = number // 10

print("First Digit =", number)

