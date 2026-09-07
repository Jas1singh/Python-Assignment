# Assignment 32 
''' Question 2: 
2.

ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:

Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student

Accept the following details:

Student ID
Student Name
Course Name
Mobile Number
Fees
City

Store the information in the nested dictionary.

Validation

If Student ID already exists:

Student ID Already Exists
2. Search Student

Accept Student ID from the user.

If found, display complete student information.

Sample Output
Student ID : 101
Name : Ajay
Course : Python
Mobile : 9876543210
Fees : 25000
City : Indore

If not found:

Student Not Found
3. Update Course

Accept Student ID.

If found:

Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Student

Accept Student ID.

If found:

Delete the record.
Sample Output
Student Deleted Successfully

Otherwise:

Student Not Found
5. Display All Students

Display all student records in a proper format.

Sample Output
-----------------------------------
Student ID : 101
Name : Ajay
Course : Python
Fees : 25000
-----------------------------------

Student ID : 102
Name : Ravi
Course : Java
Fees : 22000
-----------------------------------
6. Count Total Students

Display total number of students enrolled.

Sample Output
Total Students : 45
7. Display Students By Course

Accept a course name from the user.

Display all students enrolled in that course.

Sample Output
Enter Course : Python

101 Ajay
105 Neha
112 Aman

If no students are found:

No Students Found
8. Display Students By City

Accept city name from the user.

Display all students belonging to that city.

Sample Output
Enter City : Indore

101 Ajay
108 Ravi
115 Pooja
9. Find Student Paying Highest Fees

Display complete details of the student who has paid the highest fees.

Sample Output
Highest Fee Paying Student

Student ID : 121
Name : Neha
Course : Data Science
Fees : 50000
10. Find Student Paying Lowest Fees

Display complete details of the student who has paid the lowest fees.

Sample Output
Lowest Fee Paying Student

Student ID : 131
Name : Aman
Course : React
Fees : 15000
11. Exit

Terminate the application.

Sample Output
Thank You For Using Student Management System

'''

n = int(input("Enter the number of Students: "))

student = {}

for i in range(n):
    studentID = int(input("Enter student ID: "))
    studentName = input("Enter student Name: ")
    course = input("Enter course: ")
    Mobilenumber = int(input("Enter the mobile number: "))
    fees = int(input("Enter the fees: "))
    city = input("Enter the city: ")

    student[studentID] = {
        "name": studentName,
        "course": course,
        "mobilenumber": Mobilenumber,
        "fees": fees,
        "city": city
    }


while True:
    print('''
1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
''')

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("Add a new student:")

            studentID = int(input("Enter student ID: "))
            studentName = input("Enter student Name: ")
            course = input("Enter the course: ")
            Mobilenumber = int(input("Enter the mobile number: "))
            fees = int(input("Enter the fees: "))
            city = input("Enter the city: ")

            student[studentID] = {
                "name": studentName,
                "course": course,
                "mobilenumber": Mobilenumber,
                "fees": fees,
                "city": city
            }

            print("Student added successfully.")

        case 2:
            studentID = int(input("Enter the Student ID: "))

            if studentID in student:
                print("Student Found")
                for k, v in student.items():
                    if k == studentID:
                        print("Student ID:", k)
                        for key, val in v.items():
                            print(key,":",val)
            else:
                print("Student Not Found")

        case 3:
            studentID = int(input("Enter the Student ID: "))

            if studentID in student:
                newCourse = input("Enter new course: ")
                student[studentID]["course"] = newCourse
                print("Course updated successfully")
            else:
                print("Student Not Found")

        case 4:
            studentID = int(input("Enter the Student ID: "))

            if studentID in student:
                del student[studentID]
                print("Record deleted successfully")
            else:
                print("Student Record Not Found")

        case 5:
            print("Display All Students:")

            if len(student) == 0:
                print("No student records found.")
            else:
                for k, v in student.items():
                    print("Student ID:", k)
                    print("Name:", v["name"])
                    print("Course:", v["course"])
                    print("Mobile Number:", v["mobilenumber"])
                    print("fees:", v["fees"])
                    print("city:", v["city"])
                    print("-" * 30)

        case 6:
            print("Total Patients:", len(student))

        case 7:
            course = input("Enter the course: ")

            found = False

            for k, v in student.items():
                if v["course"].lower() == course.lower():
                    print(k, v["name"])
                    found = True

            if not found:
                print("No Student Found")

        case 8:
            city = input("Enter the city: ")

            found = False

            for k, v in student.items():
                if v["city"].lower() == city.lower():
                    print(k, v["name"])
                    found = True

            if not found:
                print("No Student Found")

        case 9:
            if len(student) == 0:
                print("No Student Found")
            else:
                highestFeesID = max(student, key=lambda x: student[x]["fees"])

                print("Highest Fee Student:")
                print("Student ID:", highestFeesID)
                print(student[highestFeesID])

        case 10:
            if len(student) == 0:
                print("No Student Found")
            else:
                lowestFeesID = min(student, key=lambda x: student[x]["fees"])

                print("Lowest Fee Student:")
                print("Student ID:", lowestFeesID)
                print(student[lowestFeesID])

        case 11:
            print("Program exited successfully.")
            print("Thank You For Using Student Management System.")
            break

        case _:
            print("Invalid choice. Please try again.")


    again = input("Do you want to continue (Yes/No) :")

    match again.lower():
        case "yes":
            continue

        case "no":
            break

        case __:
            print("Enter correct choice")
            break

print("Thank You For Using Student Management System") 