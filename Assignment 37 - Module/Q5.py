# Assignment 37 - Module 
''' Question 5: 
MENU-DRIVEN PAST DATE & TIME CALCULATOR


Create a menu-driven Python program that allows the user to calculate a date/time in the past by subtracting days, weeks, hours, or minutes.

Menu
========== PAST DATE & TIME CALCULATOR ==========

1. Subtract Days
2. Subtract Weeks
3. Subtract Hours
4. Subtract Minutes
5. Exit

Enter your choice:
CASE 1 – Subtract Days
Input
Enter your choice: 1

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to subtract: 100
Output
Starting Date : 10-09-2026
Days Subtracted : 100
Past Date : 02-06-2026
CASE 2 – Subtract Weeks
Input
Enter your choice: 2

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to subtract: 6
Output
Starting Date : 10-09-2026
Weeks Subtracted : 6
Past Date : 30-07-2026
CASE 3 – Subtract Hours

Here the student must read both date and time.

Input
Enter your choice: 3

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to subtract: 15
Output
Starting Date & Time : 10-09-2026 10:30
Hours Subtracted : 15
Past Date & Time : 09-09-2026 19:30
CASE 4 – Subtract Minutes
Input
Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 01:00
Enter number of minutes to subtract: 90
Output
Starting Date & Time : 10-09-2026 01:00
Minutes Subtracted : 90
Past Date & Time : 09-09-2026 23:30
CASE 5 – Exit
Enter your choice: 5

Thank you for using Past Date & Time Calculator!

'''

from datetime import datetime,timedelta

while True:
    print('''\n========== PAST DATE CALCULATOR ==========

1. Subtract Days
2. Subtract Weeks
3. Subtract Hours
4. Subtract Minutes
5. Exit \n''')

    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            Sdate = input("Enter starting date (DD-MM-YYYY):")
            d = int(input("Enter no. of days to subtract :"))

            pDate = datetime.strptime(Sdate,"%d-%m-%Y")

            pastDate = pDate - timedelta(days=d)

            print("Starting Date :",Sdate)
            print("Days Subtracted :", d)
            print("Past Date :", pastDate)

        case 2:
            Sdate = input("Enter starting date (DD-MM-YYYY):")

            w = int(input("Enter no. of weeks to subtract :"))

            pDate = datetime.strptime(Sdate,"%d-%m-%Y")

            pastDate = pDate - timedelta(weeks=w)

            print("Starting Date :",Sdate)
            print("Weeks Subtracted :", w)
            print("Past Date :", pastDate)

        case 3:
            Sdate = input("Enter starting date (DD-MM-YYYY):")
            h = int(input("Enter no. of hours to subtract :"))

            pDate = datetime.strptime(Sdate,"%d-%m-%Y")

            pastDate = pDate - timedelta(hours=h)

            print("Starting Date :",Sdate)
            print("Hours Subtracted :", h)
            print("Past Date :", pastDate)

        case 4:
            Sdate = input("Enter starting date (DD-MM-YYYY):")
            m = int(input("Enter no. of minutes to subtract :"))

            pDate = datetime.strptime(Sdate,"%d-%m-%Y")

            pastDate = pDate - timedelta(minutes=m)

            print("Starting Date :",Sdate)
            print("Minutes Subtracted :", m)
            print("Past Date :", pastDate)

        case 5:
            print("Exiting......")
            break

        case _:
            print("Invalid Choice !!")