# Assignment 45 -Polymorphism 
''' Question 2: 
Vehicle Rental System

Create a parent class Vehicle with:

vehicle_no
brand
rent_per_day

Create two child classes:

Car
Bike


Requirements
Take vehicle details and number of rental days from the user.
Use super() to initialize common attributes.
Create a method calculate_rent(days) in the parent class.
Override the method in both child classes.
For a Car, add ₹500 service charge to the rental amount.
For a Bike, add ₹200 service charge.
Display the final rental amount.
Sample Input
Enter Vehicle Number: MP09AB1234
Enter Brand: Honda
Enter Rent Per Day: 800
Enter Number of Days: 3
Enter Vehicle Type: Car
Expected Output
----- Rental Details -----
Vehicle Number : MP09AB1234
Brand          : Honda
Rent Per Day   : 800
Number of Days : 3
Vehicle Type   : Car
Rental Amount  : 2400
Service Charge : 500
Final Amount   : 2900
 
'''

class Vehicle:
    def __init__(self, vehicle_no, brand, rent_per_day):
        self.vehicle_no = vehicle_no
        self.brand = brand
        self.rent_per_day = rent_per_day

    def calculate_rent(self, days):
        return self.rent_per_day * days


class Car(Vehicle):
    def __init__(self, vehicle_no, brand, rent_per_day):
        super().__init__(vehicle_no, brand, rent_per_day)

    def calculate_rent(self, days):
        return super().calculate_rent(days) + 500


class Bike(Vehicle):
    def __init__(self, vehicle_no, brand, rent_per_day):
        super().__init__(vehicle_no, brand, rent_per_day)

    def calculate_rent(self, days):
        return super().calculate_rent(days) + 200


# Taking input
vehicle_no = input("Enter Vehicle Number: ")
brand = input("Enter Brand: ")
rent_per_day = int(input("Enter Rent Per Day: "))
days = int(input("Enter Number of Days: "))
vehicle_type = input("Enter Vehicle Type: ")

# Create object based on vehicle type
if vehicle_type.lower() == "car":
    vehicle = Car(vehicle_no, brand, rent_per_day)
    service_charge = 500
elif vehicle_type.lower() == "bike":
    vehicle = Bike(vehicle_no, brand, rent_per_day)
    service_charge = 200
else:
    print("Invalid Vehicle Type")
    exit()


rental_amount = rent_per_day * days

final_amount = vehicle.calculate_rent(days)

print("\n----- Rental Details -----")
print("Vehicle Number :", vehicle.vehicle_no)
print("Brand          :", vehicle.brand)
print("Rent Per Day   :", vehicle.rent_per_day)
print("Number of Days :", days)
print("Vehicle Type   :", vehicle_type)
print("Rental Amount  :", rental_amount)
print("Service Charge :", service_charge)
print("Final Amount   :", final_amount)
