# Assignment 9
# Question 3 : Smart Scholarship Allocation System

marks = int(input("Enter Marks: "))
income = int(input("Enter Family Income: "))
category = input("Enter Category: ")

if marks >= 85:
    if income <= 300000:
        if category.lower() != "general":
            scholarship = "Full Scholarship"
        else:
            scholarship = "75% Scholarship"
    else:
        scholarship = "50% Scholarship"

elif 70 <= marks <= 84:
    if income <= 200000:
        scholarship = "50% Scholarship"
    else:
        scholarship = "25% Scholarship"

else:
    scholarship = "No Scholarship"

print("Scholarship =", scholarship)