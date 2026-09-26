# Assignment 45 -Polymorphism 
''' Question 1: 
Employee Bonus System

Create a parent class Employee with the following attributes:

employee_id
employee_name
salary

Create two child classes:

Developer
Manager


Requirements

Take employee details from the user.
Use super() to initialize the common attributes.
Create a method calculate_bonus() in the parent class.
Override calculate_bonus() in both child classes.
Developer gets 10% of salary as bonus.
Manager gets 20% of salary as bonus.
Display employee details, bonus and total salary.
Sample Input
Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 50000
Enter Employee Type: Developer

Expected Output
----- Employee Details -----
Employee ID   : 101
Employee Name : Rahul
Salary        : 50000
Employee Type : Developer
Bonus         : 5000
Total Amount  : 55000

'''

class Employee:
    def __init__(self,empID,empName,sal):
        self.employee_id = empID
        self.employee_name = empName
        self.salary = sal

    def calculate_bonus(self):
        pass

    def display(self):
        print(f'''
----- Employee Details -----
Employee ID   : {self.employee_id}
Employee Name : {self.employee_name}
Salary        : {self.salary}''')


class Developer(Employee):
    def __init__(self,id,name,sal,empType):
        super().__init__(id,name,sal)
        self.employee_type = empType
        
    def calculate_bonus(self):
        self.bonus = self.salary * 0.10

    def display(self):
        super().display()
        print(f'''Employee Type : {self.employee_type}
Bonus         : {self.bonus}
Total Amount  : {self.salary+self.bonus}''')


class Manager(Employee):
    def __init__(self,id,name,sal,empType):
        super().__init__(id,name,sal)
        self.employee_type = empType

    def calculate_bonus(self):
        self.bonus = self.salary * 0.20

    def display(self):
        super().display()
        print(f'''Employee Type : {self.employee_type}
Bonus         : {self.bonus}
Total Amount  : {self.salary+self.bonus}''')
        
id = int(input("Employee ID :")) 
name = input("Employee Name : ")
sal = int(input("Salary :"))
empType = input("Employee Type : ").lower()

if empType == "developer":
    d = Developer(id,name,sal,empType)
    d.calculate_bonus()
    d.display()

elif empType == "manager":
    m = Manager(id,name,sal,empType)
    m.calculate_bonus()
    m.display()

else:
    print("\nPlz select correct Employee Type")