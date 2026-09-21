from Assignment1.Student_Management_System import class_module

students = []

for i in range(5):
    print(f"\nEnter details of Student {i + 1}")

    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    student = class_module.Student(roll_no, name, marks)
    students.append(student)


print("\nAll Students:")
for student in students:
    student.display()


print("\nStudents having marks greater than 60:")
for student in students:
    if student.marks > 60:
        student.display()


highest_student = max(students, key=lambda student: student.marks)

print("\nHighest Marks:")
highest_student.display()


total_marks = sum(student.marks for student in students)
average_marks = total_marks / len(students)

print("\nAverage Marks:")
print(average_marks)
