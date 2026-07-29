# Assignment 7
# Question 1 : Sum of First N Natural Numbers

number = int(input("Enter n: "))

total = 0

for i in range(1, number + 1):
    total = total + i

print("Total no. of ways = ", total)

