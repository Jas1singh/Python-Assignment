# Assignment 6
# Question 5 : Cinema Ticket Booking System

age = int(input("Enter age: "))

if age < 12:
    price = 100
elif age <= 60:
    price = 200
else:
    price = 150

print("Ticket Price: ₹", price)

