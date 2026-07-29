# Assignment 5
# Question 7 : Salary Benefits System

salary = int(input("Enter the salary of student : "))

if salary>=30000:
    print("PF applicable")
    if salary>=50000:
        print("Bonus applicable")

else:
    print("Not applicable")

