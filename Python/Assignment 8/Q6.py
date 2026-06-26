# Assignment 8
# Question 6 : Sum of Factors

number = int(input())

sum = 0

for i in range(1, number + 1):
    if number % i == 0:
        sum = sum + 1

print("Sum of Factors =", sum)


