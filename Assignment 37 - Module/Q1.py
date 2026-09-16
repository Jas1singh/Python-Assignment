# Assignment 37 - Module 
''' Question 1:
Age Calculator

Create a program that accepts the user's date of birth and calculates:

Current age in years
Completed months
Total number of days lived
Next birthday date
Number of days remaining for the next birthday

Input:

Enter DOB (DD-MM-YYYY): 15-08-1998

Expected Output:

Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days

 '''

from datetime import datetime

dob = input("Enter your DOB (dd-mm-yyyy) :  ")
bdate = datetime.strptime(dob,"%d-%m-%Y")
today = datetime.now()

age = today.year - bdate.year

if (today.month, today.day) < (bdate.month, bdate.day):
    age -= 1

diff = today - bdate

print(age,"Years")
print("Total days lived : ",diff.days)

nextdob = input("Enter Next Birthday Date (dd-mm-yyyy) :  ")

bdateNext = datetime.strptime(nextdob,"%d-%m-%Y")
diff2 = bdateNext - today

print("Days Remaining: ",diff2.days,"days")

