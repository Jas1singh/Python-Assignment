# Assignment 30 
''' Question 2: 
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.
'''

python_course = set()
java_course = set()

while True:
    print("\n===== ONLINE COURSE ENROLLMENT SYSTEM =====")
    print("1. Enroll Student in Python")
    print("2. Enroll Student in Java")
    print("3. Display Python Students")
    print("4. Display Java Students")
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled Only in Python")
    print("7. Find Students Enrolled Only in Java")
    print("8. Check Enrollment in Python Course")
    print("9. Display Total Unique Students")
    print("10. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        email = input("Enter Student Email: ")
        python_course.add(email)
        print("Student enrolled in Python.")

    elif choice == 2:
        email = input("Enter Student Email: ")
        java_course.add(email)
        print("Student enrolled in Java.")

    elif choice == 3:
        print("Python Students:", python_course)

    elif choice == 4:
        print("Java Students:", java_course)

    elif choice == 5:
        print("Students in Both Courses:",
              python_course.intersection(java_course))

    elif choice == 6:
        print("Only in Python:",
              python_course.difference(java_course))

    elif choice == 7:
        print("Only in Java:",
              java_course.difference(python_course))

    elif choice == 8:
        email = input("Enter Email to Check: ")

        if email in python_course:
            print("Student is enrolled in Python.")
        else:
            print("Student is not enrolled in Python.")

    elif choice == 9:
        unique_students = python_course.union(java_course)
        print("Total Unique Students:", len(unique_students))

    elif choice == 10:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")