class Employee:
    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print(
            self.employee_id,
            self.name,
            self.salary,
            self.department
        )
