# Assignment 41 - Constructor
''' Question 4:
Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage     Grade
90 and above    A
75 to 89        B
60 to 74        C
Below 60        D

Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88

Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B

'''

class Student:

    def __init__(self,n,r,m1,m2,m3):
        self.name = n
        self.rollNo = r
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def calculate_total(self):
        self.total = self.marks1 + self.marks2 + self.marks3

    def calculate_percentage(self):
        self.P = (self.total/300)*100

        if self.P>=90:
            self.grade = "A"

        elif self.P >= 75:
            self.grade = "B"

        elif self.P >= 60:
            self.grade = "C"

        else:
            self.grade = "D"

    # def grade_criteria(self):

    def display_result(self):
        print(f'''\n------ Student Result ------
Roll Number      : {self.rollNo}
Student Name     : {self.name}
Total Marks      : {self.total}
Percentage       : {self.P}
Grade            : {self.grade}''')


name = input("\nEnter name of Student : ")
roll_no = int(input("Enter Roll no of Student : "))
marks1 = int(input("Enter English Marks : "))
marks2 = int(input("Enter Mathematics : "))
marks3 = int(input("Enter Science : "))

s = Student(name,roll_no,marks1,marks2,marks3)

s.calculate_total()
s.calculate_percentage()
s.display_result()
