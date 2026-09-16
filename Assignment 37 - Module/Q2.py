# Assignment 37 - Module 
''' Question 2: 
Employee Joining & Experience System

Create an employee experience calculator.

Read:

Employee name
Joining date
Current date

Calculate:

Total days worked
Total years worked
Total months approximately
Experience in Years Months Days
Whether employee has completed 1 year
Whether employee has completed 5 years

Example:

Enter employee name: Rahul
Enter joining date: 10-06-2021
Enter current date: 10-09-2026

Output:

Employee: Rahul
Joining Date: 10-06-2021
Experience: 5 Years 3 Months 0 Days
Total Days Worked: 1918
5 Years Completed: Yes
'''

from datetime import datetime

Ename = input("Enter employee name : ")
joinDate = input("Enter joining date :  ")
currentDate = input("Enter current date :  ")

Jdate = datetime.strptime(joinDate,"%d-%m-%Y")
Cdate = datetime.strptime(currentDate,"%d-%m-%Y")

y = Cdate.year - Jdate.year
m = Cdate.month - Jdate.month
d = Cdate.day - Jdate.day

if d < 0:
    d = d + 30
    m = m - 1

if m < 0:
    m = m + 12
    y = y - 1

diff = Cdate - Jdate

print("\nEmployee : ",Ename)
print("Joining Date : ",joinDate)

print("Experience :",y,"years ",m,"months ",d,"days")

print("Total Days Worked : ",diff.days,"days")

if y >=5:
    print("5 years completed : Yes")
else:
    print("5 years completed : No")


