# Assignment 37 - Module 
''' Question 6: 
EMPLOYEE WORKING DATE & DEADLINE CALCULATOR

You are developing a small HR/Project Management utility.

The HR department wants to calculate important dates related to an employee or project.

Create a menu-driven program that provides the following operations:

========== EMPLOYEE & PROJECT DATE CALCULATOR ==========

1. Calculate Probation End Date
2. Calculate Project Deadline
3. Calculate Notice Period End Date
4. Calculate Days Remaining for Deadline
5. Check Employee Work Anniversary
6. Exit

Enter your choice:
CASE 1 – Calculate Probation End Date

An employee joins an organization on a particular date.

The company has a probation period of a specified number of months/days.

For this assignment, take probation period in days.

Input
Enter your choice: 1

Enter employee joining date (DD-MM-YYYY): 15-07-2026
Enter probation period in days: 90
Output
Joining Date : 15-07-2026
Probation Period : 90 days
Probation End Date : 13-10-2026

Students should use:

timedelta(days=...)
CASE 2 – Calculate Project Deadline

A software company starts a project on a particular date.

The project manager gives a deadline in terms of number of days.

Calculate the final deadline.

Input
Enter your choice: 2

Enter project start date (DD-MM-YYYY): 10-09-2026
Enter project duration in days: 120
Output
Project Start Date : 10-09-2026
Project Duration : 120 days
Project Deadline : 08-01-2027
Important

The program must correctly handle:

Month changes
Year changes
Leap years

Students should not manually calculate these.

CASE 3 – Calculate Notice Period End Date

An employee resigns from a company.

The employee's notice period is given in days.

Calculate the date on which the notice period ends.

Input
Enter your choice: 3

Enter resignation date (DD-MM-YYYY): 20-09-2026
Enter notice period in days: 60
Output
Resignation Date : 20-09-2026
Notice Period : 60 days
Last Working Date: 19-11-2026
Additional Test

Students should test:

Resignation Date : 15-12-2026
Notice Period : 60 days

The program must correctly move into 2027.

CASE 4 – Calculate Days Remaining for Deadline

A project has a deadline.

The program should take:

Current date
Project deadline

and calculate how many days are remaining.

Input
Enter your choice: 4

Enter current date (DD-MM-YYYY): 10-09-2026
Enter project deadline (DD-MM-YYYY): 25-09-2026
Output
Current Date : 10-09-2026
Project Deadline : 25-09-2026
Days Remaining : 15 days
If deadline has already passed

Input:

Enter current date (DD-MM-YYYY): 10-09-2026
Enter project deadline (DD-MM-YYYY): 01-09-2026

Output:

Current Date : 10-09-2026
Project Deadline : 01-09-2026
Deadline Status : Deadline has already passed
Days Overdue : 9 days
CASE 5 – Check Employee Work Anniversary

The HR department wants to check whether an employee's work anniversary is today.

Take:

Employee joining date
Current date
Input
Enter your choice: 5

Enter employee joining date (DD-MM-YYYY): 10-09-2020
Enter current date (DD-MM-YYYY): 10-09-2026
Output
Joining Date : 10-09-2020
Current Date : 10-09-2026

Work Anniversary: YES
Completed Years : 6 years
If anniversary is not today

Input:

Enter your choice: 5

Enter employee joining date (DD-MM-YYYY): 15-05-2022
Enter current date (DD-MM-YYYY): 10-09-2026

Output:

Joining Date : 15-05-2022
Current Date : 10-09-2026

Work Anniversary: NO
Completed Years : 4 years
CASE 6 – Exit
Enter your choice: 6

Thank you for using Employee & Project Date Calculator!
'''

from datetime import datetime,timedelta

while True:
    print('''\n========== EMPLOYEE & PROJECT DATE CALCULATOR ==========

1. Calculate Probation End Date
2. Calculate Project Deadline
3. Calculate Notice Period End Date
4. Calculate Days Remaining for Deadline
5. Check Employee Work Anniversary
6. Exit \n''')

    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            Jdate = input("Enter Joining date (DD-MM-YYYY):")
            d = int(input("Enter Probation Period in days :"))

            fDate = datetime.strptime(Jdate,"%d-%m-%Y")

            pEndDate = fDate + timedelta(days=d)

            print("Joining Date :",Jdate)
            print("Probation Period :", d)
            print("Probation End Date :", pEndDate)

        case 2:
            startDate = input("Enter project start date (DD-MM-YYYY):")

            d = int(input("Enter project duration in days:"))

            fDate = datetime.strptime(startDate,"%d-%m-%Y")

            deadlineDate = fDate + timedelta(days=d)

            print("Project Start Date :",startDate)
            print("Project Duration :", d)
            print("Project Deadline :", deadlineDate)

        case 3:
            regDate = int(input("Enter resignation date (DD-MM-YYYY):"))
            d = int(input("Enter notice period in days : "))

            fDate = datetime.strptime(regDate,"%d-%m-%Y")

            lastDate = fDate - timedelta(days=d)

            print("Resignation Date :",regDate)
            print("Notice Period :", d)
            print("Last Working Date:", lastDate)

        case 4:
            Cdate = input("Enter current date (DD-MM-YYYY):")
            deadlineDate = input("Enter project deadline (DD-MM-YYYY):")

            current = datetime.strptime(Cdate,"%d-%m-%Y")
            deadline = datetime.strptime(deadlineDate,"%d-%m-%Y")

            diff = deadline - current

            print("Current Date :",Cdate)
            print("Project Deadline Date :", deadlineDate)
            print("Days Remaining :", diff.days)

        case 5:
            Jdate = input("Enter Employee joining date (DD-MM-YYYY):")
            Cdate = input("Enter current date (DD-MM-YYYY):")

            joinDate = datetime.strptime(Jdate,"%d-%m-%Y")
            current = datetime.strptime(Cdate,"%d-%m-%Y")

            completedYears = current.year - joinDate.year

            print("Joining Date : ",joinDate)
            print("Current Date : ", current)

            
            if (joinDate.day , joinDate.month) == (current.day , current.month):
                print("Work Anniversary : Yes")
            else:
                print("Work Anniversary : No")

            if (current.month, current.day) < (joinDate.month, joinDate.day):
                completed_years -= 1

            print("Completed Years : ", completedYears)

        case 6:
            print("Exiting......")
            print("Thank you for using Employee & Project Date Calculator!")
            break

        case _:
            print("Invalid Choice !!")

