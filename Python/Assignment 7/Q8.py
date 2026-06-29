# Assignment 7
# Question 8 : Count Odd Digits

num = int(input("Enter number: "))

count = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        count = count + 1

    num = num // 10

print("Odd digits count =", count)

