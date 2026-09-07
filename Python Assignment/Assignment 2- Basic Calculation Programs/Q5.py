# Python Assignment 2
# Question 5 : Shopping Tax Calculator

cart_total = float(input("Enter cart total amount: ₹"))

tax = cart_total * 0.12
final_total = cart_total + tax

print("Tax = ₹", tax)
print("Total = ₹", final_total)