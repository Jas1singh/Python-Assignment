# Assignment 41 - Constructor
''' Question 5:
Hotel Room Booking System
Scenario

A hotel wants to generate the final bill of guests based on the duration of their stay.

Requirements

Create a class named Guest with:

guest_id
guest_name
number_of_days
room_charge_per_day

Initialize the values using a constructor.

Calculations
Room Bill = Number of Days × Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST

Sample Input
Enter Guest ID : G101
Enter Guest Name : Rohan Mehta
Enter Number of Days : 4
Enter Room Charge Per Day : 2500

Sample Output
------ Hotel Bill ------
Guest ID              : G101
Guest Name            : Rohan Mehta
Number of Days        : 4
Room Charge Per Day   : ₹2500.0
Room Bill             : ₹10000.0
GST (12%)             : ₹1200.0
Final Bill            : ₹11200.0

'''

class Guest:

    def __init__(self,id,name,days,charge):
        self.guestID = id
        self.gName = name
        self.days = days
        self.roomCharge = charge

    def calculate_Room_bill(self):
        self.bill = self.days * self.roomCharge

    def calculate_gst(self):
        self.Gst = self.bill * 0.12

    def calculate_final_bill(self):
        self.FinalBill = self.bill + self.Gst

    def display_salary(self):
        print(f'''\n------ Hotel Bill ------
Guest ID              : {self.guestID}
Guest Name            : {self.gName}
Number of Days        : {self.days}
Room Charge Per Day   : {self.roomCharge}
Room Bill             : {self.bill}
GST (12%)             : {self.Gst}
Final Bill            : {self.FinalBill}''')



id = input("\nEnter Guest ID : ")
name = input("Enter Guest Name : ")
days = int(input("Enter Number of Days : "))
charge = int(input("Enter Room Charge Per Day : "))

g = Guest(id,name,days,charge)

g.calculate_Room_bill()
g.calculate_gst()
g.calculate_final_bill()
g.display_salary()
