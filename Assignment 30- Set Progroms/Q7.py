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

sentence = ""

while True:
    print("\nMISSING ALPHABET FINDER\n")
    print("1. Enter Sentence")
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        sentence = input("Enter Sentence: ").lower()

    elif choice == 2:
        if sentence=="":
            print("No sentence is found !!")

        else:
            alphabets = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
            present = set(sentence)

            missing = alphabets.difference(present)

            print("Missing Alphabets:", sorted(missing))

    elif choice == 3:
        alphabets = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        present = set(sentence)

        missing = alphabets.difference(present)

        print("Count of Missing Alphabets:", len(missing))

    elif choice == 4:
        print("Exiting.........")
        break

    else:
        print("Invalid choice.")
        
