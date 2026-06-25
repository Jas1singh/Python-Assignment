# Assignment 6
# Question 13 : Employee Performance Appraisal System

salary = float(input("Enter salary: "))
rating = int(input("Enter rating (1-5): "))

if rating == 5:
    hike = salary * 0.25
elif rating == 4:
    hike = salary * 0.20
elif rating == 3:
    hike = salary * 0.10
elif rating == 2:
    hike = salary * 0.05
else:
    hike = 0

bonus = 2000 if salary < 20000 and rating >= 4 else 0

revised_salary = salary + hike + bonus

print("Revised Salary: ₹", revised_salary)

