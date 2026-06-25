# Assignment 5
# Question 4 : Gym Membership Eligibility Checker

age = int(input("Enter your age : "))


if age>=18:
    BMI = int(input("Enter the BMI value : "))
    if BMI>25:
        print("\nGym Access Granted")
        print("Enroll in weight loss program")
    
    else:
        print("Weight is ok")
        print("Gym Access Granted")

else:
    print("You are not allowed for the Gym")  