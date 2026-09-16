# Assignment 27 
''' Question 2: =========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System

=========================================================
'''

while True:
    print('''Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit ''')
    choice = int(input("Enter your choice : "))

    match choice:
        case 1:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of cols: "))

            print("\nEnter Matrix A:")
            A = []
            for i in range(rows):
                row =[]
                for j in range(cols):
                    row.append(int(input()))
                A.append(row)

            Result = []
            for row in A:
                prime = []
                for value in row:
                    if value <= 1:
                        continue

                    for i in range(2, value // 2 + 1):
                        if value % i == 0:
                            break
                    else:
                        prime.append(value)
                Result.append(prime)

            print("Prime Numbers are : ")
            print(*Result)


        case 2:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of cols: "))

            print("\nEnter Matrix A:")
            A = []

            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(int(input()))
                A.append(row)

            Result = []


            for j in range(cols):
                perfect = []

                for i in range(rows):
                    n = A[i][j]
                    total = 0

                    for k in range(1, n // 2 + 1):
                        if n % k == 0:
                            total += k

                    if total == n:
                        perfect.append(n)

                Result.append(perfect)

            print("Perfect Numbers column-wise are:")
            print(*Result)


        case 3:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of cols: "))

            print("\nEnter Matrix A:")
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

                Result.append(total)

            print("Row-wise Sum is : ")
            print(*Result)

        case 4:
            print("Program Exittig........")
            print("Thank You for Using Matrix Analysis System")
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

print("Thank You !!") 

