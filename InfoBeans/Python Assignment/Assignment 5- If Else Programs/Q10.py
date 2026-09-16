# Assignment 5
# Question 10 : Online Exam System

marks = int(input("Enter your marks : "))


if marks>=40:
    attendance = int(input("Enter the attendance value : "))
    print("Pass")
    if attendance>=75:
        print("Eligible for certificate")
    
    else:
        print("Not eligible for certificate")

else:
    print("You are Fail")  
