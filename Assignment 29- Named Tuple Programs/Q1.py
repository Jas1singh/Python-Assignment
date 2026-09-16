# Assignment 29 
''' Question 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
'''

from collections import namedtuple

n = int(input("Enter no. of Employees :"))

employee = namedtuple("Employee",["ID","Name","Department","Salary"])

emp = []
for i in range(n):
    print("\nEnter Details :")
    id = int(input("Enter ID of Employee :"))
    name = input("Enter Name of Employee :")
    dept= input("Enter Department of Employee :")
    sal= int(input("Enter Salary of Employee :"))

    E = employee(id,name,dept,sal)
    emp.append(E)
  
max = 0
min = float('inf')
sum = 0 
print("\nDisplay Details")
for i in emp:
    print(i.ID," ",i.Name," ",i.Department," ",i.Salary)


Dep = input("\nEnter Department Id of the Employee :")
for i in emp:
    if i.Salary>max:
        max = i.Salary

    if i.Salary < min:
        min = i.Salary

for i in emp:
    if i.Salary == max:
        print("\nHighest Salary Employee: ")
        print(i.ID," ",i.Name," ",i.Department," ",i.Salary)

    if i.Salary == min:
        print("\nLowest Salary Employee: ")
        print(i.ID," ",i.Name," ",i.Department," ",i.Salary)

    sum = sum + i.Salary

print("\nAverage : ",sum / n)

print("\nEmployees in IT Department:")
for  i in emp:
    if i.Department==Dep:
        print(i.ID," ",i.Name," ",i.Department," ",i.Salary)



   





