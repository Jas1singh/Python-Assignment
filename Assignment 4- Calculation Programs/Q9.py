# Assignment 4
# Question 9 : Petrol Cost Calculation

distance = int(input("Enter distance in km : "))
mileage = int(input("Enter mileage (km/litre): "))
petrolPrice = int(input("Enter petrol price per litre: "))

Petrol_Used = distance / mileage
cost = Petrol_Used * petrolPrice

print("Petrol Used =", Petrol_Used)
print("Cost =", cost)