# Assignment 8
# Question 5 : Count Factors of Number

number = int(input("Enter a Number : "))

count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1

print("Factors Count =", count)

