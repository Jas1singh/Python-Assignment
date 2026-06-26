# Assignment 9
# Question 1 : Smart Credit Card Approval System

income = int(input("Enter Income: "))
credit_score = int(input("Enter Credit Score: "))
employment = input("Enter Employment Type (government/private): ")
debt = int(input("Enter Existing Debt: "))

if income >= 50000:
    if credit_score >= 750:
        if debt < 20000:
            card = "Premium Card"
        else:
            card = "Gold Card"
    else:
        if employment.lower() == "government" and credit_score >= 650:
            card = "Gold Card"
        else:
            card = "Rejected"
else:
    if income >= 30000 and credit_score >= 700:
        card = "Silver Card"
    else:
        card = "Rejected"

print("Card Type =", card)