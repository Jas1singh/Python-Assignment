# Assignment 12
# Question 8 : ATM Note Counter

n = int(input("Enter the Number : "))
temp = n

for i in range(2):
    temp = temp // 10

# Notes = n // 100

print("Notes =",temp)
