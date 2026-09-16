# Assignment 19
# Question 7 : Smart City Citizen Information Formatter

info = input("Enter the info. : ")


words = info.split()
# print(words)

formatted = ""

for word in words:
    formatted = formatted + word[0].upper() + word[1:] + " "

	
print(formatted)    

