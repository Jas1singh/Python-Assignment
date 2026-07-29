# Assignment 15
# Question 1 : Sum of all integer between 100 and 200 which are divisible by 9

a = int(input("Enter the range : "))
b = int(input("Enter the range : "))
sum = 0

for i in range(a, b+1):
          if i % 9 ==0:
                sum = sum + i
                print(sum, end=" ")