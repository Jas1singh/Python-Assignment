# Assignment 35 - Lambda Functions 
''' Question 2:
Hospital Management System – Oldest Patient

A hospital wants to give priority to the oldest patient during a free health check-up camp. The patient details are stored as tuples containing the patient's name and age.

As a Python developer, write a program to identify the oldest patient using the reduce() function with a lambda expression.

Input
patients = [
    ("Rahul", 45),
    ("Sneha", 62),
    ("Amit", 38),
    ("Kiran", 71),
    ("Pooja", 55)
]
Expected Output
Oldest Patient: Kiran

 '''

from functools import reduce
n = int(input("Enter no. of Patients : "))
patients = []
for i in range(n):
    names = input("Enter patient name : ")
    age = int(input("Enter patient age : "))
    patients.append((names,age))
    print()

result = reduce(lambda x,y:x if x[1]>y[1] else y,patients)
print ("Oldest Patient : ",result[0])