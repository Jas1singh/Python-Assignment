# Assignment 8
# Question 10 : Student ID Validity Checker (Count Odd Digits)

number = int(input("Enter the number : "))

count = 0

while number > 0:
    digit = number % 10
    if digit % 2 != 0:
        count = count + 1
    number = number // 10

print("Odd Digits Count =", count)