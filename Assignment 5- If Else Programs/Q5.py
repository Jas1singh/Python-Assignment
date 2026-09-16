# Assignment 5
# Question 5 : Banking Security System

user = (input("Enter the cart value : "))

if user.lower()=="admin":
    password = (input("Enter the password : "))
    length = len(password)
    if length>=8:
        print("Valid user")
        print("Strong Password")
    
    else:
        print("Create strong password")

else:
    print("Invalid User")