from Assignment2.Employee_Management_System import class_module

employees = []

for i in range(5):
    print(f"\nEnter details of Employee {i + 1}")

    employee_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    employee = class_module.Employee(
        employee_id,
        name,
        salary,
        department
    )

    employees.append(employee)

print("\nAll Employees:")
for employee in employees:
    employee.display()


print("\nEmployees with salary greater than 40000:")
for employee in employees:
    if employee.salary > 40000:
        employee.display()


print("\nEmployees from IT Department:")
for employee in employees:
    if employee.department.lower() == "it":
        employee.display()


highest_employee = max(employees, key=lambda employee: employee.salary)

print("\nHighest Salary Employee:")
highest_employee.display()


total_salary = sum(employee.salary for employee in employees)

print("\nTotal Salary:")
print(total_salary)

average_salary = total_salary / len(employees)

print("\nAverage Salary:")
print(average_salary)
