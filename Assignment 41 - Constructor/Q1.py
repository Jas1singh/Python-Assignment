# Assignment 41 - Constructor
''' Question 1:
Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0

'''

class Employee:

    def __init__(self,id,n,s):
        self.id = id
        self.name = n
        self.salary = s

    def calculate_hra(self):
        self.HRA = self.salary * 0.20

    def calculate_da(self):
        self.DA = self.salary * 0.15

    def calculate_gross_salary(self):
        self.Gross = self.salary + self.DA + self.HRA

    def display_salary(self):
        print("\n------ Employee Salary Details ------")
        print("Employee ID     : ",self.id)
        print("Employee Name   : ",self.name)
        print("Basic Salary    : ",self.salary)
        print("HRA of Employee : ",self.HRA)
        print("DA of Employee  : ",self.DA)
        print("Gross Salary    : ",self.Gross)


id = input("Enter Employee ID :")
name = input("Enter Employee Name : ")
salary = int(input("Enter Basic Salary : "))

e = Employee(id,name,salary)
e.calculate_hra()
e.calculate_da()
e.calculate_gross_salary()
e.display_salary()
