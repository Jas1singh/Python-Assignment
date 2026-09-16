# Assignment 31 
''' Question 8: 
=========================================
LIBRARY BOOK ISSUE TRACKER
==========================

A library records issued books.

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]

Write a program to:

* Count how many times each book was issued.

Sample Output:
{
'Python':3,
'Java':2,
'C++':1
}

'''

books = []
n = int(input("Enter the size of list : "))

print("Enter the books : ")
for i in range(n):
    books.append(input())

d = {}

for book in books:
    d[book] = d.get(book,0)+1

print(d)