# Assignment 40 - Classes & Object 
''' Question 2: 
Employee Salary Calculator

A company wants to calculate an employee's gross salary.

Create a class Employee with the following attributes:

Employee ID

Employee name

Basic salary

HRA percentage

DA percentage

Create the following methods:

calculate_hra() – Calculate HRA.

calculate_da() – Calculate DA.

calculate_gross_salary() – Calculate gross salary.

display_salary() – Display employee salary details.

Formula:

HRA = Basic Salary × HRA Percentage / 100
DA = Basic Salary × DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA

'''

class Employee:

    def set(self,id,n,s,Hper,Dper):
        self.id = id
        self.name = n
        self.salary = s
        self.hpercentage = Hper
        self.dpercentage = Dper

    def calculate_hra(self):
        self.HRA = self.salary * self.hpercentage / 100

    def calculate_da(self):
        self.DA = self.salary * self.dpercentage / 100
       
    def calculate_gross_salary(self):
        self.Gross = self.salary + self.hpercentage + self.dpercentage

    def display_salary(self):
        print("Employee ID : ",self.id)
        print("Employee Name : ",self.name)
        print("Basic Salary : ",self.salary)
        print("HRA of Employee : ",self.HRA)
        print("DA of Employee : ",self.DA)
        print("Gross Salary : ",self.Gross)

e = Employee()

e.set(101,"Ram",20000,75,50)
e.calculate_hra()
e.calculate_da()
e.calculate_gross_salary()
e.display_salary()