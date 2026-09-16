# Assignment 3
# Question 12 : Change Return System

amt = int(input("Enter amount: "))

hundreds = amt // 100
amt = amt % 100

fifties = amt // 50
amt = amt % 50

tens = amt // 10

print("₹100 x", hundreds)
print("₹50 x", fifties)
print("₹10 x", tens)