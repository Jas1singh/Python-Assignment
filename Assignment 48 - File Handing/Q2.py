# Assignment 48 - File Handing 
''' Question 2: 
Employee Salary Report

A company stores employee salary information in employees.txt.

Each record contains:

EmployeeID,EmployeeName,Department,Salary
Task

Write a Python program to:

Accept employee details.
Store them in the file.
Read the file.
Display employees whose salary is greater than ₹50,000.
Calculate the average salary.
Sample Input
Enter number of employees: 4

101,Ajay,IT,65000
102,Ravi,HR,45000
103,Priya,IT,72000
104,Amit,Sales,48000
Expected Output
Employees with Salary > 50000
--------------------------------
101  Ajay   IT       65000
103  Priya  IT       72000

Average Salary: 57500.00
'''

n = int(input("Enter number of employees: "))

# Writing employee details
with open("employees.txt", "w") as file:
    for i in range(n):
        data = input()
        file.write(data + "\n")


total_salary = 0
employee_count = 0

print("\nEmployees with Salary > 50000\n")

# Reading employee details
with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(" ")

        employee_id = data[0]
        employee_name = data[1]
        department = data[2]
        salary = float(data[3])

        total_salary += salary
        employee_count += 1

        if salary > 50000:
            print(employee_id, employee_name, department, int(salary))


average_salary = total_salary / employee_count

print("\nAverage Salary: {:.2f}".format(average_salary))
