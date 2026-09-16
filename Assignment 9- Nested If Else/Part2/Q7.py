# Assignment 9
# Question 7 : University Result Classification System

marks = int(input("Enter Marks: "))
backlogs = int(input("Enter Number of Backlogs: "))
project = int(input("Enter Project Score: "))

if marks >= 75:
    if backlogs == 0:
        if project >= 80:
            result = "First Class with Distinction"
        else:
            result = "First Class"
    else:
        result = "First Class"

elif 60 <= marks <= 74:
    if backlogs <= 2:
        result = "Second Class"
    else:
        result = "Pass Class"

elif 50 <= marks <= 59:
    result = "Pass"

else:
    result = "Fail"

print("Result =", result)