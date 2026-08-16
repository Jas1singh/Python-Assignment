# Assignment 30 
''' Question 1: 
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.
'''

coding_club = set()
robotics_club = set()

while True:
    print("\n===== STUDENT CLUB MEMBERSHIP SYSTEM =====")
    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in Both Clubs")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club")
    print("8. Display All Unique Club Members")
    print("9. Display Total Unique Club Members")
    print("10. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        student = input("Enter Student ID: ")
        coding_club.add(student)
        print("Student added to Coding Club.")

    elif choice == 2:
        student = input("Enter Student ID: ")
        robotics_club.add(student)
        print("Student added to Robotics Club.")

    elif choice == 3:
        print("Coding Club:", coding_club)

    elif choice == 4:
        print("Robotics Club:", robotics_club)

    elif choice == 5:
        print("Students in Both Clubs:",
              coding_club.intersection(robotics_club))

    elif choice == 6:
        print("Only in Coding Club:",
              coding_club.difference(robotics_club))

    elif choice == 7:
        print("Only in Robotics Club:",
              robotics_club.difference(coding_club))

    elif choice == 8:
        print("All Unique Members:",
              coding_club.union(robotics_club))

    elif choice == 9:
        unique_members = coding_club.union(robotics_club)
        print("Total Unique Members:", len(unique_members))

    elif choice == 10:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

