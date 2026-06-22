# Assignment 3
# Question 9 : Fuel Cost Calculator

distance = int(input("Enter distance in km : "))
mileage = int(input("Enter mileage (km/litre): "))
petrolPrice = int(input("Enter petrol price per litre: "))

fuel_needed = distance / mileage
cost = fuel_needed * petrolPrice

print("Cost =", cost)



