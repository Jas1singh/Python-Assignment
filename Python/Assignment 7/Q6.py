# Assignment 7
# Question 6 : Armstrong Number

num = int(input("Enter number: "))

original = num
sum1 = 0

while num > 0:
    digit = num % 10
    sum1 += digit ** 3
    num //= 10

if original == sum1:
    print("Armstrong")
else:
    print("Not Armstrong")

