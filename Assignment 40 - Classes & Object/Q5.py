# Assignment 40 - Classes & Object 
''' Question 5: 
Shopping Bill Calculator

 A retail shop wants to calculate the total bill for a customer.

Create a class ShoppingBill with the following attributes:

Product name

Product price

Quantity

Discount percentage

GST percentage

Create the following methods:

calculate_subtotal() – Calculate price × quantity.

calculate_discount() – Calculate the discount amount.

calculate_gst() – Calculate GST on the discounted amount.

calculate_final_bill() – Calculate the final payable amount.

display_bill() – Display the complete bill details.

Formula:

Subtotal = Price × Quantity
Discounted Amount = Subtotal - Discount
GST = Discounted Amount × GST Percentage / 100
Final Bill = Discounted Amount + GST

'''

class Product:

    def set(self,n,p,q,Dper,Gstper):
        self.name = n
        self.price = p
        self.quantity = q
        self.discountpercentage = Dper
        self.Gstpercentage = Gstper

    def calculate_subtotal(self):
        self.Subtotal = self.price * self.quantity

    def calculate_discount(self):
        self.DiscountedAmount = self.Subtotal - self.discountpercentage/100
       
    def calculate_gst(self):
        self.Gst = self.DiscountedAmount * self.Gstpercentage / 100

    def calculate_final_bill(self):
        self.FinalBill = self.DiscountedAmount + self.Gst

    def display_salary(self):
        print("\nProduct Name : ",self.name)
        print("Product Price : ",self.price)
        print("Product Quantity : ",self.quantity)
        print("Subtotal : ",self.Subtotal)
        print("GST : ",self.Gst)
        print("Final Bill : ",self.FinalBill)

p = Product()

p.set("Laptop",40000,5,10,18)
p.calculate_subtotal()
p.calculate_discount()
p.calculate_gst()
p.calculate_final_bill()
p.display_salary()
