# Assignment 4
# Question 5 : Salary Breakdown

Salary = int(input("Enter the monthly salary of the employee : "))
Total_Days = int(input("Enter the total working days : "))
Total_Hours = int (input("Enter the total working hours per day : "))

Salary_Per_Day = Salary/Total_Days
Salary_Per_Hour = Salary/(Total_Days*Total_Hours)

print("Salary per day =  ", Salary_Per_Day)
print("Salary per hour = ", Salary_Per_Hour)