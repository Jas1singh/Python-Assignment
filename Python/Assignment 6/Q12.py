# Assignment 6
# Question 12 : Restaurant Bill with GST System

bill = float(input("Enter bill amount: "))

if bill <= 1000:
    gst = bill * 0.05
elif bill <= 5000:
    gst = bill * 0.12
else:
    gst = bill * 0.18

service_charge = 200 if bill > 3000 else 0

final_bill = bill + gst + service_charge

print("Final Bill Amount: ₹", final_bill)


