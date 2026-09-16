# Assignment 6
# Question 11 : Railway Ticket Fare System

distance = int(input("Enter distance: "))
travel_class = input("Enter class (Sleeper/AC): ")

if distance <= 100:
    if travel_class.lower() == "sleeper":
        fare = 100
    else:
        fare = 200

elif distance <= 500:
    if travel_class.lower() == "sleeper":
        fare = 300
    else:
        fare = 600

else:
    if travel_class.lower() == "sleeper":
        fare = 500
    else:
        fare = 1000

print("Total Fare: ₹", fare)

