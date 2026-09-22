from Student_Management_System import class_module

students = []

for i in range(5):
    print(f"\nEnter details of Student {i + 1}")

    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    obj = class_module.Student(roll_no, name, marks)
    students.append(obj)


print("\nAll Students:")
for obj in students:
    obj.display()


print("\nStudents having marks greater than 60:")
for obj in students:
    if obj.marks > 60:
        obj.display()


highest_student = max(students, key=lambda obj: obj.marks)

print("\nHighest Marks:")
highest_student.display()


total_marks = sum(obj.marks for obj in students)
average_marks = total_marks / len(students)

print("\nAverage Marks:")
print(average_marks)
