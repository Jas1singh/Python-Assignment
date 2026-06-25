# Assignment 7
# Question 2 : Factorial of a Number

n = int(input("Enter number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Total Ways =", fact)

