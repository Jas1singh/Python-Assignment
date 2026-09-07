# Assignment 6
# Question 6 : Company Bonus Distribution System

salary = float(input("Enter salary: "))
experience = float(input("Enter years of experience: "))

if experience > 10:
    bonus = salary * 0.20
elif experience >= 5:
    bonus = salary * 0.10
elif experience >= 2:
    bonus = salary * 0.05
else:
    bonus = 0

print("Bonus Amount: ₹", bonus)

