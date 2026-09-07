# Assignment 9
# Question 2 : Hospital Emergency Priority System

age = int(input("Enter Age: "))
severity = input("Enter Severity (critical/moderate/low): ")
insurance = input("Insurance (yes/no): ")

if severity.lower() == "critical":
    if age >= 60:
        treatment = "Immediate ICU"
    else:
        treatment = "Emergency Ward"

elif severity.lower() == "moderate":
    if insurance.lower() == "yes":
        treatment = "Priority Treatment"
    else:
        treatment = "General Queue"

else:
    if age < 10:
        treatment = "Pediatric Priority"
    else:
        treatment = "Wait"

print("Treatment =", treatment)