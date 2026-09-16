# Assignment 9
# Question 10 : Military Recruitment Fitness System

age = int(input("Enter Age: "))
bmi = float(input("Enter BMI: "))
running_time = float(input("Enter Running Time (minutes): "))
medical = input("Medical Status (fit/unfit): ")

if 18 <= age <= 25:
    if 18 <= bmi <= 25:
        if running_time <= 15:
            if medical.lower() == "fit":
                status = "Selected"
            else:
                status = "Medical Reject"
        else:
            status = "Physical Fail"
    else:
        status = "BMI Fail"

elif 26 <= age <= 30:
    if running_time <= 14 and medical.lower() == "fit":
        status = "Conditional Selection"
    else:
        status = "Rejected"

else:
    status = "Not Eligible"

print("Selection Status =", status)