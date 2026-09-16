# Assignment 41 - Constructor 
''' Question 6: 
Library Book Management System


A library wants to maintain information about books. The librarian should be able to:

View book details.
Issue the book to a student.
Return the book.
Requirements

Create a class named Book with the following attributes:

book_id
title
author
status (Initially "Available")

Initialize the values using a constructor.

Create the following methods:
display_details() → Displays all book information.
issue_book() → Changes the status to "Issued".
return_book() → Changes the status to "Available".
Sample Input
Enter Book ID : B101
Enter Book Title : Python Programming
Enter Author Name : John Smith
Sample Output
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available

Book issued successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Issued

Book returned successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available

'''

class Book:

    def __init__(self,id,title,name,s="Available"):
        self.bookID = id
        self.title = title
        self.author = name
        self.status = s

    def issue_book(self):
        if self.status=="Available":
            self.status = "Issued"
            print("Book issued successfullly")
            self.display_details()
        else:
            print("Book is not available")
       
    def return_book(self):
        if self.status=="Issued":
            self.status = "Available"
            print("Book returned successfullly")
            self.display_details()
        else:
            print("Book is available")
        

    def display_details(self):
        print(f'''\n------ Book Details ------
Book ID     : {self.bookID}
Title       : {self.title}
Author      : {self.author}
Status      : {self.status}\n''')


        
id = input("\nEnter Book ID : ")
title = input("Enter Book Title : ")
name = input("Enter Author Name : ")

b = Book(id,title,name)

b.display_details()
b.issue_book()
b.return_book()
