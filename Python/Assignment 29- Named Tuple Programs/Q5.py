# Assignment 29 
''' Question 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
'''

from collections import namedtuple

n = int(input("Enter no. of Employees :"))

library = namedtuple("Library",["BookID","Title","Author","Price"])

lib = []
for i in range(n):
    print("\nEnter Details :")
    id = input("Enter ID of Book :")
    title = input("Enter Title of Book :")
    author= input("Enter Author Name :")
    price = int(input("Enter Price of Book :"))

    L = library(id,title,author,price)
    lib.append(L)
  
max = 0
sum = 0 
print("\nDisplay Details")
for i in lib:
    print(i.BookID," ",i.Title," ",i.Author," ",i.Price)


Auth = input("\nEnter Author Name :")
for i in lib:
    if i.Price>max:
        max = i.Price


for i in lib:
    if i.Price == max:
        print("\nMost Expensive Book: ")
        print(i.BookID," ",i.Title," ",i.Author," ",i.Price)

    sum = sum + i.Price

print("\nAverage Book Price : ",sum / n)

print("\nBooks Written By", Auth,":")
for i in lib:
    if i.Author==Auth:
        print(i.BookID," ",i.Title," ",i.Author," ",i.Price)