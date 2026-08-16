# Assignment 30 
''' Question 3:
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations.
'''

visitors = set()

while True:
    print("\n===== WEBSITE VISITOR TRACKING SYSTEM =====")
    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        visitor_id = input("Enter Visitor ID: ")
        visitors.add(visitor_id)
        print("Visitor added.")

    elif choice == 2:
        visitor_id = input("Enter Visitor ID: ")

        if visitor_id in visitors:
            visitors.remove(visitor_id)
            print("Visitor removed.")
        else:
            print("Visitor ID not found.")

    elif choice == 3:
        visitor_id = input("Enter Visitor ID: ")

        if visitor_id in visitors:
            print("Visitor found.")
        else:
            print("Visitor not found.")

    elif choice == 4:
        print("All Visitors:", visitors)

    elif choice == 5:
        print("Unique Visitors:", len(visitors))

    elif choice == 6:
        visitors.clear()
        print("Visitor data cleared.")

    elif choice == 7:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")