# Assignment 9
# Question 6 : Banking Fraud Detection System

amount = int(input("Enter Transaction Amount: "))
location = input("Enter Location (international/domestic): ")
device = input("Device (new/old): ")
transactions = int(input("Enter Transaction Count: "))
unusual = input("Unusual Activity (yes/no): ")

if amount >= 50000:
    if location.lower() == "international":
        if device.lower() == "new":
            if transactions > 3:
                risk = "High Risk (Blocked)"
            else:
                risk = "Medium Risk"
        else:
            risk = "Medium Risk"
    else:
        if transactions > 5:
            risk = "Medium Risk"
        else:
            risk = "Low Risk"
else:
    if unusual.lower() == "yes":
        if device.lower() == "new":
            risk = "Medium Risk"
        else:
            risk = "Low Risk"
    else:
        risk = "Safe"

print("Risk Level =", risk)