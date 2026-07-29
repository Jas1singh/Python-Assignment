# Assignment 5
# Question 1 : A bank wants to automate its loan approval process.

salary = int(input("Enter the salary amount : "))

if salary>=30000:
    creditScore = int(input("Enter the credit score : "))
    if creditScore>=750:
        loans = int(input("Enter the existing loans : "))
        if loans<2:
            print("Loan status = Conditional Approval ")

        else:
            print("Loan is rejected") 

else:
    print("You are not eligible for Loan")             



