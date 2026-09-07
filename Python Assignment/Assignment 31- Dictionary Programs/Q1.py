# Assignment 31 
''' Question 1: 
=========================================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6

'''
d = {}

n = int(input("Enter the no. of items : "))

for i in range(n):
    key = input("Enter the Poduct :")
    value = int(input("Enter Quantity :"))

    d[key] = value

print("Toatal Quantity : ",sum(d.values()))
