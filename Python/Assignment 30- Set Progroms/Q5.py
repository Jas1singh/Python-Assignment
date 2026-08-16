# Assignment 30 
''' Question 5: 
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed.
'''

isbn_numbers = set()

while True:
    print("\n===== LIBRARY ISBN MANAGER =====")
    print("1. Add ISBN")
    print("2. Remove ISBN")
    print("3. Search ISBN")
    print("4. Display ISBN List")
    print("5. Count Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        isbn = input("Enter ISBN: ")

        if isbn in isbn_numbers:
            print("ISBN already exists.")
        else:
            isbn_numbers.add(isbn)
            print("ISBN added.")

    elif choice == 2:
        isbn = input("Enter ISBN: ")

        if isbn in isbn_numbers:
            isbn_numbers.remove(isbn)
            print("ISBN removed.")
        else:
            print("ISBN not found.")

    elif choice == 3:
        isbn = input("Enter ISBN to search: ")

        if isbn in isbn_numbers:
            print("ISBN found.")
        else:
            print("ISBN not found.")

    elif choice == 4:
        print("ISBN List:", isbn_numbers)

    elif choice == 5:
        print("Total Books:", len(isbn_numbers))

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")