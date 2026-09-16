# Assignment 7
# Question 2 : Factorial of a Number

number = int(input("Enter number: "))

fact = 1

for i in range(1, number + 1):
    fact = fact * i

print("Total points earned = ", fact)

