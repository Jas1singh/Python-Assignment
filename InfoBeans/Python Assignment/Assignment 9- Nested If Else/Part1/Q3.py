# Assignment 9
# Question 3 : Banking Fraud Detection System

amount = int(input("Enter the amount : "))
location = (input("Enter the Location : ")).lower()
account_age = int(input("Enter the Account Age (in years) : "))

if amount>=10000:
    if location=="international":
        otp = input("OTP verification (yes/no) : ").lower()

        if otp == "yes":
            print("Transaction Status: Allowed")
        else:
            print("Transaction Status: Blocked")

    elif location=="domestic":
        if amount>=5000:
            if account_age>=2:
                print("Transaction Status = Allowed")

            else:
                print("Transaction Status = Flagged")   

        else:
            print("Transaction Status = Allowed") 
else:
    unusual = input("Is there unusual activity? (yes/no): ").lower()

    if unusual == "yes":
        print("Transaction Status: Flagged")
    else:
        print("Transaction Status: Allowed")                               


