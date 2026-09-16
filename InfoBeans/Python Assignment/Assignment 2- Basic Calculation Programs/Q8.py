# Python Assignment 2
# Question 8 : Simple Interest Calculator

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)