# Assignment 8
# Question 9 : Neon Number LED Unlock Game

number = int(input("Enter the number : "))

square = number * number
sum = 0

while square > 0:
    digit = square % 10
    sum = sum + digit
    square = square // 10

if sum == number:
    print("Glowing Success! You've found the Neon Number!")
else:
    print("Try again! Not quite glowing yet.")

