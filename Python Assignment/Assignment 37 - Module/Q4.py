# Assignment 37 - Module 
''' Question 4: 
Menu-Driven Future Date Calculator

Develop a menu-driven Python program using the datetime module to calculate a future date.

The program should allow the user to add days, weeks, hours, or minutes to a given date/time.

Use timedelta for all date and time calculations.

Menu
========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice:
Case 1 – Add Days

Read:

Starting date
Number of days
Input
Enter your choice: 1

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to add: 100
Output
Starting Date : 10-09-2026
Days Added : 100
Future Date : 19-12-2026
Case 2 – Add Weeks

Read:

Starting date
Number of weeks
Input
Enter your choice: 2

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to add: 4
Output
Starting Date : 10-09-2026
Weeks Added : 4
Future Date : 08-10-2026
Case 3 – Add Hours

For this case, the student should take date and time as input.

Input
Enter your choice: 3

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to add: 15
Output
Starting Date & Time : 10-09-2026 10:30
Hours Added : 15
Future Date & Time : 11-09-2026 01:30

This case should test whether students understand that adding hours can change the date.

Case 4 – Add Minutes

Take date/time and number of minutes.

Input
Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 23:30
Enter number of minutes to add: 90
Output
Starting Date & Time : 10-09-2026 23:30
Minutes Added : 90
Future Date & Time : 11-09-2026 01:00

Students must correctly handle the change from 10 September → 11 September.

Case 5 – Exit
Enter your choice: 5

Thank you for using Future Date Calculator!
Complete Sample Run

========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice: 1

Enter starting date (DD-MM-YYYY): 25-12-2026
Enter number of days to add: 15

Starting Date : 25-12-2026
Days Added : 15
Future Date : 09-01-2027


========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 31-12-2026 23:30
Enter number of minutes to add: 90

Starting Date & Time : 31-12-2026 23:30
Minutes Added : 90
Future Date & Time : 01-01-2027 01:00


========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice: 5

Thank you for using Future Date Calculator!

'''

from datetime import datetime,timedelta

while True:
    print('''\n========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit \n''')

    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            Sdate = input("Enter starting date (DD-MM-YYYY):")
            d = int(input("Enter no. of days to add :"))

            fDate = datetime.strptime(Sdate,"%d-%m-%Y")

            futureDate = fDate + timedelta(days=d)

            print("Starting Date :",Sdate)
            print("Days Added :", d)
            print("Future Date :", futureDate)

        case 2:
            Sdate = input("Enter starting date (DD-MM-YYYY):")
            w = int(input("Enter no. of weeks to add :"))

            fDate = datetime.strptime(Sdate,"%d-%m-%Y")

            futureDate = fDate + timedelta(weeks=w)

            print("Starting Date :",Sdate)
            print("Weeks Added :", w)
            print("Future Date :", futureDate)

        case 3:
            Sdate = input("Enter starting date (DD-MM-YYYY):")
            h = int(input("Enter no. of hours to add :"))

            fDate = datetime.strptime(Sdate,"%d-%m-%Y")

            futureDate = fDate + timedelta(hours=h)

            print("Starting Date :",Sdate)
            print("Hours Added :", h)
            print("Future Date :", futureDate)

        case 4:
            Sdate = input("Enter starting date (DD-MM-YYYY):")
            m = int(input("Enter no. of minutes to add :"))

            fDate = datetime.strptime(Sdate,"%d-%m-%Y")

            futureDate = fDate + timedelta(minutes=m)

            print("Starting Date :",Sdate)
            print("Minutes Added :", m)
            print("Future Date :", futureDate)

        case 5:
            print("Exiting......")
            break

        case _:
            print("Invalid Choice !!")