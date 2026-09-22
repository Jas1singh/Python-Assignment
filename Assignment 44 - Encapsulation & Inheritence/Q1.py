# Assignment 44 - Encapsulation & Inheritence 
''' Question 1: 
EMPLOYEE MANAGEMENT SYSTEM
=========================================

SCENARIO:

A company wants to maintain information about different types of employees.

Create the following class hierarchy:

Employee
|
+-------- Developer
|
+-------- Manager

REQUIREMENTS:

1. Create a parent class Employee.

Employee should contain:

* employee_id
* employee_name
* salary

2. Create Developer and Manager classes that inherit from Employee.

3. Employee should have a method:

display_details()

4. Developer should have:

programming_language

and a method:

write_code()

5. Manager should have:

team_size

and a method:

manage_team()

6. The child-class constructors must initialize parent-class data using super().

7. Override display_details() in both child classes.

8. From the overridden method, call the parent display_details() using super().

9. salary must be encapsulated.

Implement:

@property
@salary.setter
@salary.deleter

10. Salary setter must reject salary <= 0.

11. Read ALL employee information from the user.

INPUT REQUIREMENT:

Ask the user:

Enter Employee ID:
Enter Employee Name:
Enter Salary:
Enter Employee Type:

1. Developer
2. Manager

If Developer:

Enter Programming Language:

If Manager:

Enter Team Size:

SAMPLE INPUT:

Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 45000
Enter Employee Type: 1
Enter Programming Language: Python

EXPECTED OUTPUT:

## Employee Details

Employee ID: 101
Employee Name: Rahul
Salary: 45000
Role: Developer
Programming Language: Python

Rahul is developing applications using Python.

'''

class Employee:
    def __init__(self, empID, empName, sal):
        self.employee_id = empID
        self.employee_name = empName
        self.salary = sal

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            print("Salary must be greater than 0.")
            self._salary = 0
        else:
            self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary

    def display_details(self):
        print("## Employee Details")
        print()
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.employee_name}")
        print(f"Salary: {self.salary}")


class Developer(Employee):
    def __init__(self, empID, empName, sal, lang):
        super().__init__(empID, empName, sal)
        self.programming_language = lang

    def display_details(self):
        super().display_details()
        print("Role: Developer")
        print(f"Programming Language: {self.programming_language}")

    def write_code(self):
        print(
            f"{self.employee_name} is developing applications "
            f"using {self.programming_language}."
        )


class Manager(Employee):
    def __init__(self, empID, empName, sal, teamSize):
        super().__init__(empID, empName, sal)
        self.team_size = teamSize

    def display_details(self):
        super().display_details()
        print("Role: Manager")
        print(f"Team Size: {self.team_size}")

    def manage_team(self):
        print(
            f"{self.employee_name} is managing a team "
            f"of {self.team_size} members."
        )


empID = int(input("Enter Employee ID: "))
empName = input("Enter Employee Name: ")
sal = float(input("Enter Salary: "))

print("Enter Employee Type:")
print("1. Developer")
print("2. Manager")

empType = int(input("Enter Employee Type: "))

if empType == 1:
    lang = input("Enter Programming Language: ")

    employee = Developer(empID, empName, sal, lang)

    print()
    employee.display_details()
    print()
    employee.write_code()

elif empType == 2:
    teamSize = int(input("Enter Team Size: "))

    employee = Manager(empID, empName, sal, teamSize)

    print()
    employee.display_details()
    print()
    employee.manage_team()

else:
    print("Invalid Employee Type.")

