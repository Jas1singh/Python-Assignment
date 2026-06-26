# Assignment 9
# Question 5 : Smart Exam Evaluation System

marks = int(input("Enter Marks: "))
attendance = int(input("Enter Attendance (%): "))
internal = int(input("Enter Internal Marks: "))

if marks >= 40:
    if attendance >= 75:
        if internal >= 20:
            result = "Pass"
        else:
            result = "Grace Pass"
    else:
        result = "Detained"
else:
    if marks >= 35 and internal >= 25:
        result = "Reappear"
    else:
        result = "Fail"

print("Result =", result)