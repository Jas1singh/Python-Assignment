# Assignment 48 - File Handing 
''' Question 1: 
Student Attendance Manager

A school wants to maintain the attendance of students in a text file named attendance.txt.

Each line contains:

RollNo,StudentName,Status

where Status is either Present or Absent.


Write a Python program to:

Accept attendance details for N students.
Store the details in attendance.txt.
Read the file and display:
Total students
Number of present students
Number of absent students
Attendance percentage
Sample Input
Enter number of students: 5

Enter Roll No: 101
Enter Student Name: Rahul
Enter Status: Present

Enter Roll No: 102
Enter Student Name: Priya
Enter Status: Absent

Enter Roll No: 103
Enter Student Name: Amit
Enter Status: Present

Enter Roll No: 104
Enter Student Name: Neha
Enter Status: Present

Enter Roll No: 105
Enter Student Name: Rohit
Enter Status: Absent
Expected Output
Attendance Report
-------------------------
Total Students: 5
Present Students: 3
Absent Students: 2
Attendance Percentage: 60.00%

'''

n = int(input("Enter number of students: "))

with open("attendance.txt", "w") as file:
    for i in range(n):
        roll_no = input("Enter Roll No: ")
        student_name = input("Enter Student Name: ")
        status = input("Enter Status: ")

        file.write(roll_no + "," + student_name + "," + status + "\n")


total_students = 0
present_students = 0
absent_students = 0

with open("attendance.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        total_students += 1

        if data[2] == "Present":
            present_students += 1
        elif data[2] == "Absent":
            absent_students += 1


attendance_percentage = (present_students / total_students) * 100

print("\nAttendance Report\n")

print("Total Students:", total_students)
print("Present Students:", present_students)
print("Absent Students:", absent_students)
print("Attendance Percentage: {:.2f}%".format(attendance_percentage))
