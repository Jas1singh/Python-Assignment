from Employee_Management_System import class_module

employees = []

for i in range(5):
    print(f"\nEnter details of Employee {i + 1}")

    employee_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    obj = class_module.Employee(employee_id,name,salary,department)

    employees.append(obj)

print("\nAll Employees:")
for obj in employees:
    obj.display()


print("\nEmployees with salary greater than 40000:")
for obj in employees:
    if obj.salary > 40000:
        obj.display()


print("\nEmployees from IT Department:")
for obj in employees:
    if obj.department.lower() == "it":
        obj.display()


highest_employee = max(employees, key=lambda obj: obj.salary)

print("\nHighest Salary Employee:")
highest_employee.display()


total_salary = sum(obj.salary for obj in employees)

print("\nTotal Salary:")
print(total_salary)

average_salary = total_salary / len(employees)

print("\nAverage Salary:")
print(average_salary)
