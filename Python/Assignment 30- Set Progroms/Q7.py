# Assignment 30 
''' Question 7: 
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z.
'''

import string

sentence = ""

while True:
    print("\n===== MISSING ALPHABET FINDER =====")
    print("1. Enter Sentence")
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        sentence = input("Enter Sentence: ").lower()

    elif choice == 2:
        alphabets = set(string.ascii_lowercase)
        present = set(sentence)

        missing = alphabets.difference(present)

        print("Missing Alphabets:", sorted(missing))

    elif choice == 3:
        alphabets = set(string.ascii_lowercase)
        present = set(sentence)

        missing = alphabets.difference(present)

        print("Count of Missing Alphabets:", len(missing))

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
