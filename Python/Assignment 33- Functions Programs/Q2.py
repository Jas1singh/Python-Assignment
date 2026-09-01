# Assignment 33 
''' Question 2:
NUMBER ANALYSIS SYSTEM

Scenario:

A software company wants to develop a Number Analysis System. The application should be menu-driven and perform different mathematical operations on a given number.

MENU

1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit

Requirements

Choice 1 – Check Perfect Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return True if the number is Perfect, otherwise False.
* Display an appropriate message based on the returned value.

Choice 2 – Check Prime Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return a message such as "Prime Number" or "Not a Prime Number".
* Display the returned message.

Choice 3 – Find Reverse of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return the reversed number.
* Display the returned value.

Choice 4 – Calculate Factorial

* Accept a number from the user.
* Pass the number to a function.
* The function should return the factorial value.
* Display the returned value.

Choice 5 – Display Factors of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return all factors of the given number.
* Display the returned factors.

Choice 6 – Exit

Sample Output

Enter Choice : 1

Enter Number : 28

28 is a Perfect Number

---

Enter Choice : 2

Enter Number : 17

Prime Number

---

Enter Choice : 3

Enter Number : 1234

Reverse Number : 4321

---

Enter Choice : 4

Enter Number : 5

Factorial : 120

---

Enter Choice : 5

Enter Number : 12

Factors : 1 2 3 4 6 12

---

Important Instructions

1. Create separate functions for each operation.
2. Use parameters to pass values to functions.
3. Use return statements appropriately.
4. Different functions should return different types of values such as Boolean, String, Integer, and Collection/List.
5. Avoid using global variables.
6. Implement the solution using a menu-driven approach.
7. Write meaningful function names and maintain proper code readability.

 '''


def checkPerfect(n):
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum = sum + i

    if sum == n:
        print(n, "is a Perfect Number")

    else:
        print(n, "is not a Perfect Number")


def checkPrime(n):
    prime = True

    for i in range(2,n//2+1):
        if n%i == 0:
            prime = False

    if prime:
        print(n, "is a Prime Number")

    else:
        print(n, "is not a Prime Number")


def reverse(n):
    rev = 0
    temp = n
    while temp>0:
        d = temp%10
        rev = rev * 10 + d
        temp = temp //10
    print("Reverse of",n,"is",rev)


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    print("factorial", fact)

    
def displayFactors(n):
    for i in range(1, n//2+1):
        if n % i == 0:
            print(i)


print("\n******** NUMBER ANALYSIS SYSTEM ********\n")

print('''1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit
''')

while True:
    choice = int(input("\nEnter your choice : "))
    match choice:
        case 1:
            n = int(input("Enter a Number: "))
            checkPerfect(n)

        case 2:
            n = int(input("Enter a Number: "))
            checkPrime(n)

        case 3:
            n = int(input("Enter a  Number: "))
            reverse(n)
        
        case 4:
            n = int(input("Enter a Number: "))
            factorial(n)

        case 5:
            n = int(input("Enter a Number: "))
            displayFactors(n)

        case 6:
            print("Program Exiting.......")
            break

        case _:
            print("Invalid choice! Please enter 1 to 8.")





