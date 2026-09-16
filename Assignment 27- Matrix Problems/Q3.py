# Assignment 27 
''' Question 3: =========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2

=========================================================
'''

while True:
    print('''Menu

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit''')

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            print("\nEnter matrix elements:")
            A = []

            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(int(input()))
                A.append(row)

            Result = []

            for row in A:
                count = 0

                for value in row:
                    n = value
                    temp = n
                    digits = 0

                    while temp > 0:
                        digits += 1
                        temp = temp // 10

                    temp = n
                    total = 0

                    while temp > 0:
                        digit = temp % 10
                        total = total + digit ** digits
                        temp = temp // 10

                    if total == n:
                        count += 1

                Result.append(count)

            for i in range(rows):
                print("Row", i + 1, "Armstrong Count =", Result[i])

        case 2:
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            print("\nEnter matrix elements:")
            A = []

            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(int(input()))
                A.append(row)

            Result = []

            for j in range(cols):
                count = 0

                for i in range(rows):
                    n = A[i][j]
                    temp = n
                    reverse = 0

                    while temp > 0:
                        digit = temp % 10
                        reverse = reverse * 10 + digit
                        temp = temp // 10

                    if reverse == n:
                        count += 1

                Result.append(count)

            for j in range(cols):
                print("Column", j + 1, "Palindrome Count =", Result[j])

        case 3:
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            print("\nEnter matrix elements:")
            A = []

            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(int(input()))
                A.append(row)

            Result = []

            for row in A:
                total = 0

                for value in row:
                    total += value

                average = total / cols
                Result.append(average)

            for i in range(rows):
                print("Row", i + 1, "Average =", Result[i])

        case 4:
            print("Thank You for Using Matrix Quality Check System")
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
    
print("Thank You for Using Matrix Quality Check System !!") 