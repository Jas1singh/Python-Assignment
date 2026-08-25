# Assignment 30 
''' Question 4: 
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed.
'''


subjects = frozenset(['Python','Java','Mysql','React','Spring Boot'])

while True:
    print("\nFROZEN SET SUBJECT MANAGEMENT\n")
    print('''1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit''')

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            print("All Subjects:", subjects)

        case 2:
            subjectName = input("Enter Subject Name : ")

            if subjectName in subjects:
                print("Subject found.")
            else:
                print("Subject not found.")

        case 3:
            print("No. of Subjects:", len(subjects))

        case 4:
            Newsub = input("Enter new subject :")
            subjects.add(Newsub)

        case 5:
            print("Exiting.......")
            break

        case _:
            print("Invalid choice.")
