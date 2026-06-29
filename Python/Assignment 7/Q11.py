# Assignment 7
# Question 11 : Count Occurrence of a Digit

num = int(input("Enter number: "))
search = int(input("Enter searching digit: "))

count = 0

while num > 0:
    digit = num % 10

    if digit == search:
        count = count + 1

    num = num // 10

print(count)

