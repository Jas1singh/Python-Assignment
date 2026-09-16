# Assignment 6
# Question 9 : Student Attendance Eligibility System

attendance = float(input("Enter attendance percentage: "))

if attendance >= 75:
    status = "Eligible"
elif attendance >= 60:
    status = "Eligible with Warning"
else:
    status = "Not Eligible"

print("Status:", status)

