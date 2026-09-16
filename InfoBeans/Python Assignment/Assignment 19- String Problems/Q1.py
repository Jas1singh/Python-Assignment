# Assignment 19
# Question 1 : Email Username Validator

username = input("Enter the username : ")

first = username[0].isalpha()
special = True
space = 0
underscore = "_"
length = len(username)

for u in username:	
	if u.isspace():
		space =space +1
		
	elif not(u==underscore or u.isalnum()):
		special = False
		break
				          
				     
if length >=5 and length<=12 and space ==0 and first and special==True:
	print("Valid Username")

else:
	print ("Invalid")