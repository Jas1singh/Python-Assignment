# Assignment 8
# Question 7 : Power of a Number

number = int(input("Enter first number : "))
power = int(input("Enter second number : "))

result = 1

for i in range(power):
    result = result * number

print(result)

