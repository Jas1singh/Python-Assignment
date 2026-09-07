# Assignment 9
# Question 9 : Smart Loan Eligibility System

salary = int(input("Enter Salary: "))
age = int(input("Enter Age: "))
credit_score = int(input("Enter Credit Score: "))
emi = int(input("Enter EMI Amount: "))

if salary >= 40000:
    if 21 <= age <= 60:
        if credit_score >= 750:
            if emi <= salary * 0.40:
                status = "Approved at 8%"
            else:
                status = "Approved at 10%"
        else:
            if credit_score >= 650:
                status = "Approved at 12%"
            else:
                status = "Rejected"
    else:
        status = "Rejected"
else:
    if salary >= 25000 and credit_score >= 700:
        status = "Approved at 13%"
    else:
        status = "Rejected"

print("Loan Status =", status)