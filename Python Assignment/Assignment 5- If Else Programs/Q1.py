# Assignment 5
# Question 1 : Smart Voting & ID Verification

age = int(input("Enter your age : "))

if age>=18:
    citizen = (input("Do u have ID (yes/no) : "))
    if citizen.lower()=="yes":
        print("\nEligible to vote")
        print("Allowed inside booth")
    
    else:
        print("Not allowed inside the booth")

else:
    print("\nYou are not eligible to vote")        
