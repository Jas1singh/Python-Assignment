# Assignment 29 
''' Question 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
'''

from collections import namedtuple

n = int(input("Enter no. of Orders :"))

customer = namedtuple("Customer",["orderID","Name","Product","Amount"])

Cust = []
for i in range(n):
    print("\nEnter Details :")
    orderid = input("Enter Order ID :")
    name = input("Enter Name of Customer :")
    product = input("Enter Product Name :")
    amount = int(input("Enter Amount :"))

    C = customer(orderid,name,product,amount)
    Cust.append(C)
  
max = 0
count = 0
sum = 0 

print("\nDisplay Details")
for i in Cust:
    print(i.orderID," ",i.Name," ",i.Product," ",i.Amount)


for i in Cust:
    if i.Amount>max:
        max = i.Amount

    if i.Amount > 10000:
        count = count + 1

    sum = sum + i.Amount
    

print("Highest Value Order:")
for i in Cust:
    if i.Amount==max:
        print(i.orderID," ",i.Name," ",i.Product," ",i.Amount)
  
print("\nTotal Sales : ",sum)

print("\nStudents Above 80: ",count)