# Assignment 40 - Classes & Object 
''' Question 1: 
Student Result Calculator

 A school wants to calculate the total marks and percentage of a student.

Create a class Student with the following attributes:

Student name

Roll number

Marks in English

Marks in Mathematics

Marks in Science

Create the following methods:

calculate_total() – Calculate the total marks.

calculate_percentage() – Calculate the percentage.

display_result() – Display student details, total, and percentage.

Expected output:

Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%

'''

class Student:

    def set(self,n,r,m1,m2,m3):
        self.n = n
        self.r = r
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate_total(self):
        self.total = self.m1 + self.m2 + self.m3

    def calculate_percentage(self):
        self.P = (self.total/300)*100

    def display_result(self):
        print("Student Name : ",self.n)
        print("Roll Number : ",self.r)
        print("Total Marks : ",self.total)
        print("Percentage : ",self.P)

s = Student()

name = input("\n\nEnter name of Student : ")
roll_no = int(input("Enter Roll no of Student : "))
marks1 = int(input("Enter English Marks : "))
marks2 = int(input("Enter Mathematics : "))
marks3 = int(input("Enter Science : "))

s.set(name,roll_no,marks1,marks2,marks3)

s.calculate_total()
s.calculate_percentage()
s.display_result()