# Assignment 4
# Question 1 : Restaurant Bill Split

Friends = int(input("Enter the no. of friends : "))
Total_Bill = int(input("Enter the total bill amount : "))
gst = int (input("Enter the gst on bill : "))
Service_Charge = int (input("Enter service charge percent : "))

gst = (Total_Bill*gst)/100
Service_Charge = (Total_Bill*Service_Charge)/100

Final_Bill = (gst + Service_Charge + Total_Bill)
Each_Pay = Final_Bill/Friends

print("Final Bill = ",Final_Bill)
print("Each person pays = ",Each_Pay)