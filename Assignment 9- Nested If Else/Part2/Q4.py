# Assignment 9
# Question 4 : Airline Ticket Pricing Engine

travel_class = input("Enter Class (business/economy): ")
distance = int(input("Enter Distance (km): "))
booking = input("Booking Time (early/late): ")

if travel_class.lower() == "business":
    if distance > 1000:
        price = 8000
    else:
        price = 5000
else:
    if distance > 1000:
        if booking.lower() == "early":
            price = 4000
        else:
            price = 5000
    else:
        price = 2500

print("Ticket Price =", price)