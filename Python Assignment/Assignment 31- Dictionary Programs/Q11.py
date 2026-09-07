# Assignment 31 
''' Question 11: 
=========================================
PRODUCT SALES ANALYSIS
======================

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1

'''

sales = []
n = int(input("Enter the size of list : "))

print("Enter the products : ")
for i in range(n):
    sales.append(input())

d = {}

for sale in sales:
    d[sale] = d.get(sale,0)+1

for i in sorted(d):
    print(i, ":",(d[i]))