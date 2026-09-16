# Assignment 19
# Question 4 : Employee ID Validator

Empid = input("Enter the Employee ID. : ")

remain = Empid[3:]
length = len(Empid)
check = Empid.startswith("EMP")				          
				     
if length ==8 and check==True and remain.isdigit()==True:
	print("Valid EMP ID")

else:
	print ("Invalid")

