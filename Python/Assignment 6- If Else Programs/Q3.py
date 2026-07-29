# Assignment 6
# Question 3 : Income Tax Department System

income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + ((income - 500000) * 0.20)
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + ((income - 1000000) * 0.30)

print("Tax Payable: ₹", tax)