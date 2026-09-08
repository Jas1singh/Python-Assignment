# Assignment 35 - Lambda Functions 
''' Question 1: 
Student Registration System – Longest Name

A school is organizing an inter-school cultural event. During the registration process, the coordinator notices that some students have very long names, which may not fit properly on the printed ID cards.

As a software developer, your task is to write a Python program that identifies the student with the longest name from the list of registered students using the reduce() function along with a lambda expression.

Input
students = ["Riya", "Christopher", "Aman", "Neha", "Siddharth"]
Expected Output
Student with the longest name: Christopher

'''

from functools import reduce
n = int(input("Enter no. of employees : "))
names = []
for i in range(n):
    names.append((input()))

result = reduce(lambda x,y:x if len(x)>len(y) else y,names)
print ("Student with the longest name:",result)