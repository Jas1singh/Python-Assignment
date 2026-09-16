# Assignment 40 - Classes & Object 
''' Question 6: 
Electricity Bill Calculator

An electricity board wants to calculate a customer's electricity bill based on units consumed.

Create a class ElectricityBill with the following attributes:

Consumer number

Consumer name

Units consumed

Rate per unit

Fixed charge

Create the following methods:

calculate_energy_charge() – Calculate units × rate per unit.

calculate_total_bill() – Add energy charge and fixed charge.

display_bill() – Display consumer details and bill amount.

Sample data:

Consumer Number: 501
Consumer Name: Amit
Units Consumed: 250
Rate Per Unit: 6
Fixed Charge: 100

Expected result:

Energy Charge: 1500
Total Bill: 1600

'''

class ElectricityBill:

    def set(self,custNo,custN,units,rate,charge):
        self.cust_Number = custNo
        self.cust_Name = custN
        self.units = units
        self.rate =  rate
        self.fixedCharge = charge

    def calculate_energy_charge(self):
        self.energy = self.units * self.rate

    def calculate_total_bill(self):
        self.total = self.energy + self.fixedCharge

    def display_bill(self):
        print("Energy Charge: ",self.energy)
        print("Total Bill: ",self.total)
    

b = ElectricityBill()
b.set()
b.calculate_energy_charge()
b.calculate_total_bill()
b.display_bill()