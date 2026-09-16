# Assignment 28 
''' Question 3: MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit

Requirements :

Choice 1 :
Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.

Choice 2 :
Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.

Choice 3 :
Display Employee-wise Maximum Score
Find and display the maximum value present in each row.

Sample Input
10 20 30
40 50 60
25 35 45

Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
'''

rows = int(input("Enter no. of Employees: "))
cols = int(input("Enter no. of Months : "))

print("\nEnter matrix elements:")
A = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

while True:
    print('''\nMenu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit''')

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            max = 0
            employee = 0
            for i in range(rows):
                Totalscore = 0
                for j in range(cols):
                    Totalscore = Totalscore + A[i][j]

                if Totalscore>max:
                    max = Totalscore
                    employee = i+1
            print(f"Employee {employee} has Highest Total Score : ",max)


        case 2:
            minAvg = float('inf')
            month = 0
            for j in range(cols):
                Totalscore = 0
                for i in range(rows):
                    Totalscore = Totalscore + A[i][j]
                avg = Totalscore/rows

                if avg<minAvg:
                    minAvg = avg
                    month = j+1
            print(f"Month {month} has Lowest Average Score : ",minAvg)


        case 3:
            for i in range(rows):
                max_score = A[i][0]

                for j in range(1, cols):
                    if A[i][j] > max_score:
                        max_score = A[i][j]

                print(f"Employee {i + 1} Max Score: {max_score}")
             
            
        case 4:
            print("Thank You for Using Matrix Diagonal Analysis System")
            break

        case _:
            print("Invalid Choice")


    again = input("Do you want to continue (Yes/No) :")
    
    match again.lower():
        case "yes":
            continue

        case "no":
            break

        case __:
            print("Enter correct choice")
            break
    
print("Thank You for Using Matrix Diagonal Analysis System !!") 

