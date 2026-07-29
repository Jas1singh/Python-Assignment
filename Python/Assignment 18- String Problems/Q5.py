# Assignment 18
# Question 5 : Advanced Password Security Checker

password = input("Enter the password : ")

capPassword = password[0].isupper()

last = password[-1]
count = 0
sp = 0
space = 0
special ="@#$%&*"
length = len(password)


for p in password:
	if p.isdigit():
		count =count + 1
		
	elif p.isspace():
		space =space +1
		
	elif p in special:
		sp = sp + 1
				          
				     
if length >=8 and length<=15 and count >=2 and sp!=0 and space ==0 and last.isdigit()==True and capPassword:
	print("Valid Password")

else:
	print ("Invalid")