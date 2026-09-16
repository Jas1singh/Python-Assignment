# Assignment 27 
''' Question 4: =========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

=========================================================
'''


rows = int(input("Enter size of matrix: "))

print("\nEnter matrix elements:")
A = []

for i in range(rows):
    row = []
    for j in range(rows):
        row.append(int(input()))
    A.append(row)

while True:
    print('''\nMenu

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit''')

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            Main = []

            for i in range(rows):
                Main.append(A[i][i])

            print("Main Diagonal Elements:")
            print(*Main)

        case 2:
            Secondary = []

            for i in range(rows):
                Secondary.append(A[i][rows - 1 - i])

            print("Secondary Diagonal Elements:")
            print(*Secondary)

        case 3:
            MainSum = 0
            SecondarySum = 0

            for i in range(rows):
                MainSum += A[i][i]
                SecondarySum += A[i][rows - 1 - i]

            print("Main Diagonal Sum =", MainSum)
            print("Secondary Diagonal Sum =", SecondarySum)

            if MainSum > SecondarySum:
                print("Main Diagonal Sum is Greater")
            elif SecondarySum > MainSum:
                print("Secondary Diagonal Sum is Greater")
            else:
                print("Both Diagonal Sums are Equal")

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