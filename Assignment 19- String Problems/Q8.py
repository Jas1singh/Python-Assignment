# Assignment 19
# Question 8 : Airport Passenger Name Formatting System 

passengerInfo = input("Enter the info. : ")


words = passengerInfo.split()
# print(words)

formatted = ""

for word in words:
    formatted = formatted + word[0].upper() + word[1:] + " "

	
print(formatted)    
