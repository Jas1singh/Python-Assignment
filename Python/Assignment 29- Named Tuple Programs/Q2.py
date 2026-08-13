# Assignment 29 
''' Question 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
'''

from collections import namedtuple

n = int(input("Enter no. of Students :"))

student = namedtuple("Student",["Rollno","Name","Course","Marks"])

Stu = []
for i in range(n):
    print("\nEnter Details :")
    rno = int(input("Enter Roll no of Student :"))
    name = input("Enter Name of Student :")
    course = input("Enter Course :")
    marks = int(input("Enter Marks of Student :"))

    S = student(rno,name,course,marks)
    Stu.append(S)
  
max = 0
count = 0
sum = 0 
print("\nDisplay Details")
for i in Stu:
    print(i.Rollno," ",i.Name," ",i.Course," ",i.Marks)


C = input("\nEnter Course :")
for i in Stu:
    if i.Marks>max:
        max = i.Marks

    if i.Marks > 80:
        count = count + 1

for i in Stu:
    if i.Marks == max:
        print("\nTopper: ")
        print(i.Rollno," ",i.Name," ",i.Course," ",i.Marks)

    sum = sum + i.Marks
    
print("\nStudents Above 80: ",count)
print("\nAverage : ",sum / n)

print("\nStudents in Python Course:")
for  i in Stu:
    if i.Course==C:
        print(i.Rollno," ",i.Name," ",i.Course," ",i.Marks)