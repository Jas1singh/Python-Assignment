# Assignment 30 
''' Question 8: 
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters.
'''

users = frozenset()
characters = frozenset([0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])


while True:
    print("\nALLOWED CHARACTER VALIDATOR\n")
    print('''1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit
''')

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            uName = input("Enter the username : ")

        case 2:
            uName = input("Enter UserName : ")
            flag = False
            for i in uName:
                if i in characters:
                    flag = True

            if flag:
                print("Username is valid.")

            else:
                print("This username is not valid")           

           
        case 3:
            print("Allowed Characters are :", characters)
            
        case 4:
            print("Exiting.......")
            break

        case _:
            print("Invalid choice.")

