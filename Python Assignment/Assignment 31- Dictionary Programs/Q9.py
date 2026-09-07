# Assignment 31 
''' Question 9: 
=========================================
INVENTORY MANAGEMENT SYSTEM
===========================

Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker

'''

d = {}

n = int(input("Enter the no. of stocks : "))

for i in range(n):
    key = input("Enter product :")
    value = int(input("Enter quantity :"))

    d[key] = value   

for k , v in d.items():
    if v < 30:
        print(k)

