# Assignment 9
# Question 8 : E-Commerce Dynamic Pricing System

demand = int(input("Enter Demand: "))
stock = int(input("Enter Stock: "))
user_type = input("Enter User Type (premium/normal): ")
festival = input("Festival Offer? (yes/no): ")

if demand >= 80:
    if stock < 50:
        if user_type.lower() == "premium":
            if festival.lower() == "yes":
                discount = "20%"
            else:
                discount = "10%"
        else:
            discount = "No Discount"
    else:
        discount = "5%"

elif 40 <= demand <= 79:
    if festival.lower() == "yes":
        discount = "10%"
    else:
        discount = "No Discount"

else:
    if stock > 200:
        discount = "15%"
    else:
        discount = "No Discount"

print("Discount =", discount)