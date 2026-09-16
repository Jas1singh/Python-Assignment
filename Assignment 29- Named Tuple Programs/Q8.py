# Assignment 29 
''' Question 8: MATRIX PATTERN DETECTION SYSTEM

A satellite monitoring center stores signal strengths in matrix form. Engineers want to identify special patterns in the matrix.

Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit

Requirements
Choice 1 – Count Even Numbers Above Main Diagonal

Count all even numbers where:

column > row
Choice 2 – Count Odd Numbers Below Main Diagonal

Count all odd numbers where:

row > column
Choice 3 – Display Boundary Elements

Display all elements present on:

First Row
Last Row
First Column
Last Column

without repeating corner elements.

Sample Input
1 2 3
4 5 6
7 8 9
Output
Even Numbers Above Main Diagonal = 2
(2, 6)

Odd Numbers Below Main Diagonal = 1
(7)

Boundary Elements:
1 2 3 6 9 8 7 4
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
    print('''Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit ''')
    choice = int(input("Enter your choice : "))
    
    match choice:
        case 1:
            even = []
            for i in range(rows):
                for j in range(rows):
                    if j>i and A[i][j]%2==0:
                        even.append(A[i][j])

            print("Addition of Matrix is : ")
            print(*even)


        case 2:
            odd = []
            for i in range(rows):
                for j in range(rows):
                    if i>j and A[i][j]%2!=0:
                        odd.append(A[i][j])

            print("Addition of Matrix is : ")
            print(*odd)


        case 3:
            for i in range(rows):
                for j in range(rows):
                    if i==0 or j==rows-1 or i==rows-1 or j==0:
                        print(A[i][j])


        case 4:
            print("Exitting..........")
            print("Thank You for Using Matrix Operations Management System")
            break

        case __:
            print("Wrong Choice")           

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