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
    print("\nWEBSITE VISITOR TRACKING SYSTEM\n")
    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            visitor_id = input("Enter Visitor ID: ")
            visitors.add(visitor_id)
            print("Visitor added.")

        case 2:
            visitor_id = input("Enter Visitor ID: ")

            if visitor_id in visitors:
                visitors.remove(visitor_id)
                print("Visitor removed.")
            else:
                print("Visitor ID not found.")

        case 3:
            visitor_id = input("Enter Visitor ID: ")

            if visitor_id in visitors:
                print("Visitor found.")
            else:
                print("Visitor not found.")

        case 4:
            print("All Visitors:", visitors)

        case 5:
            print("Unique Visitors:", len(visitors))

        case 6:
            visitors.clear()
            print("Visitor data cleared.")

        case 7:
            print("Exiting.......")
            break

        case _:
            print("Invalid choice.")