# Assignment 33 
''' Question 1: 
STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. The staff should be able to
enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit

Functional Requirements

1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

******** STUDENT RESULT MANAGEMENT ********

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.

'''

students = {}
def addStudent(roll_no):
    print("\n Add Student Details")

    name = input("Enter Student Name: ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for Subject {i}: "))
        marks.append(mark)

    students[roll_no] = {
        "name": name,
        "marks": marks
    }

    print("Student details added successfully!")

def calculateTotal(roll_no):
    marks = students[roll_no]["marks"]
    total = sum(marks)

    print("\nTotal : ", total)


def percentage(roll_no):
    if roll_no not in students:
        print("Student not found!")
        return
    
    marks = students[roll_no]["marks"]
    total = sum(marks)

    print("Percentage : ", total/5)

def grade(roll_no):
    if roll_no not in students:
        print("Student not found!")
        return
    
    marks = students[roll_no]["marks"]
    percent = sum(marks)/5

    if percent>=90:
        print("Grade = A+")

    elif percent>=80:
        print("Grade = A")

    elif percent>=70:
        print("Grade = B")

    elif percent>=60:
        print("Grade = C")

    elif percent>=50:
        print("Grade = D")

    else:
        print("Fail")


def display(roll_no):

    if roll_no not in students:
        print("Student not found!")
        return
    
    student = students[roll_no]

    name = student["name"]
    marks = student["marks"]


    print("---------Result Card---------")

    print("Name : ",name)
    print("Roll Number : ",roll_no)

    print("\nMarks")
    for i in range(5):
        print(f"Subject {i+1} : {marks[i]}")

    calculateTotal(roll_no)
    percentage(roll_no)
    grade(roll_no)
    highestMark(roll_no)
    lowestMark(roll_no)

def highestMark(roll_no):

    if roll_no not in students:
        print("Student not found!")
        return

    marks = students[roll_no]["marks"]

    highest = max(marks)

    print("Highest Mark =", highest)


def lowestMark(roll_no):

    if roll_no not in students:
        print("Student not found!")
        return

    marks = students[roll_no]["marks"]

    lowest = min(marks)

    print("Lowest Mark =", lowest)


print("\n******** STUDENT RESULT MANAGEMENT ********\n")

print('''1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit
''')

while True:
    choice = int(input("\nEnter your choice : "))
    match choice:
        case 1:
            roll_no = input("Enter Roll Number: ")
            addStudent(roll_no)

        case 2:
            roll_no = input("Enter Roll Number: ")
            calculateTotal(roll_no)

        case 3:
            roll_no = input("Enter Roll Number: ")
            percentage(roll_no)

        case 4:
            roll_no = input("Enter Roll Number: ")
            grade(roll_no)

        case 5:
            roll_no = input("Enter Roll Number: ")
            display(roll_no)

        case 6:
            roll_no = input("Enter Roll Number: ")
            highestMark(roll_no)

        case 7:
            roll_no = input("Enter Roll Number: ")
            lowestMark(roll_no)

        case 8:
            print("Program Exiting.......")
            break

        case _:
            print("Invalid choice! Please enter 1 to 8.")






