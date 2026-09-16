# Assignment 41 - Constructor
''' Question 3:
Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0

'''

class Product:

    def __init__(self,id,n,q,p):
        self.productID = id
        self.productName = n
        self.price = p
        self.quantity = q

    def calculate_total(self):
        self.total = self.price * self.quantity

    def final_amount(self):
        if self.total>5000:
            self.discount = self.total * 0.10
        else:
            self.discount = self.total * 0.05

        self.final = self.total - self.discount


    def display_salary(self):
        print(f'''\n------ Shopping Bill ------
Product ID        : {self.productID}
Product Name      : {self.productName}
Quantity          : {self.quantity}
Price Per Item    : ₹{self.price}
Total Amount      : ₹{self.total}
Discount          : ₹{self.discount}
Final Amount      : ₹{self.final}''')



id  = input("\nEnter Product ID : ")
name = input("Enter Product Name : ")
quantity = int(input("Enter Quantity : "))
price = int(input("Enter Price Per Item : "))

p = Product(id,name,quantity,price)

p.calculate_total()
p.final_amount()
p.display_salary()
