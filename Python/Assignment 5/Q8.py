# Assignment 5
# Question 8 : Number Property Checker

number = int(input("Enter the number : "))

if number%2==0:
    print("Even number")
    if number%5==0:
        print("Divisible by 5")

else:
    print("Number should be even")

