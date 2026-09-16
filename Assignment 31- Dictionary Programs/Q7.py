# Assignment 31 
''' Question 7: 
=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Ravi

'''

d = {}

n = int(input("Enter the no. of students : "))

for i in range(n):
    key = input("Enter name :")
    value = int(input("Enter marks :"))

    d[key] = value   

for k , v in d.items():
    if v >= 50:
        print(k)