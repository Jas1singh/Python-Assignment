# Assignment 6
# Question 4 : E-Commerce Discount Engine

amount = float(input("Enter purchase amount: "))

if amount > 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = amount * 0.05

final_amount = amount - discount

print("Final Amount: ₹", final_amount)