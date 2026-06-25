# Assignment 7
# Question 7 : Count Even Digits

num = int(input("Enter number: "))

count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        count += 1

    num //= 10

print("Even digits count =", count)

