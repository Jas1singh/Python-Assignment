# Assignment 48 - File Handing 
''' Question 3: 
Online Shopping Order History

An e-commerce company maintains order information in orders.txt.

Each order contains:

OrderID,CustomerName,Product,Quantity,Price
Task

Write a program to:

Accept order details.
Store them in the file.
Read the file.
Calculate total amount for each order.
Display the order having the highest total amount.

Formula:

Total Amount = Quantity × Price
Sample Input
Enter number of orders: 3

O101,Rahul,Laptop,1,55000
O102,Priya,Mouse,3,800
O103,Amit,Keyboard,2,1500
Expected Output
Order Details
--------------------------------
O101 Rahul Laptop   Quantity: 1 Total: 55000
O102 Priya Mouse    Quantity: 3 Total: 2400
O103 Amit Keyboard  Quantity: 2 Total: 3000

Highest Order:
Order ID: O101
Customer: Rahul
Total Amount: 55000

'''

n = int(input("Enter number of orders: "))

with open("orders.txt", "w") as file:
    for i in range(n):
        data = input()
        file.write(data + "\n")


highest_total = 0
highest_order_id = ""
highest_customer = ""

print("\nOrder Details\n")

with open("orders.txt", "r") as file:
    for line in file:
        data = line.strip().split(" ")

        order_id = data[0]
        customer_name = data[1]
        product = data[2]
        quantity = int(data[3])
        price = float(data[4])

        total = quantity * price

        print(
            order_id,
            customer_name,
            product,
            "Quantity:", quantity,
            "Total:", int(total)
        )

        if total > highest_total:
            highest_total = total
            highest_order_id = order_id
            highest_customer = customer_name


print("\nHighest Order:")
print("Order ID:", highest_order_id)
print("Customer:", highest_customer)
print("Total Amount:", int(highest_total))
