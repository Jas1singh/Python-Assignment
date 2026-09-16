# Assignment 41 - Constructor
''' Question 2:
Electricity Bill Calculator
Scenario


An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0

'''

class ElectricityBill:

    def __init__(self,custid,custN,units):
        self.customer_ID = custid
        self.customer_Name = custN
        self.units = units
        self.rate =  8
        self.fixedCharge = 150

    def calculate_total_bill(self):
        self.total = self.units * self.rate + self.fixedCharge

    def display_bill(self):
        print(f'''\n  ------ Electricity Bill ------
Customer ID       : {self.customer_ID}
Customer Name     : {self.customer_Name}
Units Consumed    : {self.units}
Total Bill Amount : {self.total}''')



id = input("\nEnter Customer ID : ")
name = input("Enter Customer Name : ")
units = int(input("Enter Units Consumed : "))

b = ElectricityBill(id,name,units)

b.calculate_total_bill()
b.display_bill()
