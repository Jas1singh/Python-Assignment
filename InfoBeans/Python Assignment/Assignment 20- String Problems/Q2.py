# Assignment 20
# Question 2 : Corporate Employee Short ID Generator

Ename = input("Enter the Employee Name :").lower()

words = Ename.split()

ID = ""

for word in words:
    ID = ID + word[0].upper()

print("Employee Short ID:",ID)