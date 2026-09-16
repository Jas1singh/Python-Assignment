# Assignment 31 
''' Question 4: 
=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65

'''

d = {}

n = int(input("Enter the no. of students : "))

for i in range(n):
    key = input("Enter name :")
    value = int(input("Enter marks :"))

    d[key] = value

max = max(d.values())    
min = min(d.values())    

for k , v in d.items():
    if v == max:
        print("Highest Marks :",k,v)

    elif v == min:
        print("Lowest Marks :",k,v)
            