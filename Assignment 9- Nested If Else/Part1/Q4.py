# Assignment 9
# Question 4 : Ride Booking Surge Pricing System

demand = int(input("Enter the Demand : "))
time = (input("Enter the time : ")).lower()
distance = int(input("Enter the distance : "))

if demand>=80:
    if time=="peak":
        if distance>=10:
            print("Fare Multiplier = 2x Fare")
        else:
            print("Fare Multiplier = 1.5x Fare")  

    else:
        if demand>=90:
            print("Fare Multiplier = 1.8x Fare")
        else:
            print("Fare Multiplier = 1.3x Fare")

else:
    if demand>=50:
        if time=="peak":
            print("Fare Multiplier = 1.2x Fare")

        else:
            print("Normal Fare")
    else:
            print("Normal Fare")            


