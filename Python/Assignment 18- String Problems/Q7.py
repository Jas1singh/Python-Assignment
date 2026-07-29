# Assignment 18
# Question 7 : Vehicle Number Plate Checker

plate = input("Enter the plate no. : ")

start = plate[:2].isalpha()
next = plate[2:4].isdigit()

length = len(plate)
				          			     
if length ==10 and start==True and next==True:
	print("Valid Vehicle Number")

else:
	print ("Invalid")