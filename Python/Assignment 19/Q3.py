# Assignment 19
# Question 3 : Word Counter in Complaint Message

message = input("Enter the message :")

count = 0

for n in message:	
	if n.isspace():
		count =count +1
						    
print (count+1)

