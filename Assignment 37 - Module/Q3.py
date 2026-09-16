# Assignment 37 - Module 
''' Question 3: 
Date Difference Calculator

Create a program that accepts two dates and displays:

Enter first date: 10-09-2026
Enter second date: 25-12-2026

Display:

Difference in days
Difference in weeks
Difference in hours
Difference in minutes

Example:

Days Difference: 106
Weeks Difference: 15
Hours Difference: 2544
Minutes Difference: 152640

'''
from datetime import datetime

date1 = input("Enter first date: ")
date2 = input("Enter second date: ")

d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")

diff = d2 - d1

print("Difference in days:", diff.days)
print("Difference in weeks:", diff.days / 7)
print("Difference in hours:", diff.total_seconds() / 3600)
print("Difference in minutes:", diff.total_seconds() / 60)


