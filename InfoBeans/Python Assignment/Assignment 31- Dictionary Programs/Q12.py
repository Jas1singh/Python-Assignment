# Assignment 31 
''' Question 12: 
=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza

'''

orders = []
n = int(input("Enter the size of list : "))

print("Enter food items in list : ")
for i in range(n):
    orders.append(input())

d = {}

for order in orders:
    d[order] = d.get(order,0)+1

print(d)
print("Most Downloads :", max(d, key=d.get))