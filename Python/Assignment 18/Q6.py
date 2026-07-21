# Assignment 18
# Question 6 : Railway Ticket PNR Analyzer

ticket = input("Enter the ticket no. : ")

remain = ticket[3:]
length = len(ticket)
check = ticket.startswith("PNR")				          
				     
if length ==12 and check==True and remain.isdigit()==True:
	print("Valid PNR No.")

else:
	print ("Invalid")