# Assignment 6
# Question 10 : Mobile Data Plan Advisor

usage = float(input("Enter daily data usage: "))

if usage > 3:
    plan = "Premium Plan"
elif usage >= 1:
    plan = "Standard Plan"
else:
    plan = "Basic Plan"

print("Recommended Plan:", plan)

