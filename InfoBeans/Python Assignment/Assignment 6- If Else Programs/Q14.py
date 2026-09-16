# Assignment 6
# Question 14 : Online Course Fee System

course = input("Enter course category: ").lower()
user_type = input("Enter user type: ").lower()

if course == "programming":
    fee = 5000
elif course == "design":
    fee = 4000
elif course == "marketing":
    fee = 3000
else:
    fee = 0

if user_type == "student":
    discount = fee * 0.20
elif user_type == "working professional":
    discount = fee * 0.10
else:
    discount = 0

final_fee = fee - discount

print("Final Course Fee: ₹", final_fee)