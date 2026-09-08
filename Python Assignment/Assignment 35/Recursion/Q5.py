# Assignment 35 - Lambda Functions 
''' Question 4:
Assignment 10: Cyber Security (Strong Password Check)

A cybersecurity company considers a numeric password to be "strong" if every digit is even.

Task

Write a recursive function to check whether all digits of the given number are even.

Input 1
Enter Password:
248620
Output 1
Strong Password
Input 2
Enter Password:
248621
Output 2
Weak Password
 '''

def passCheck(n):
    if n==0:
        return True

    else:
        d = n%10
        if d%2!=0:
            return False

    return passCheck(n//10)

password = int(input("Enter password : "))

if passCheck(password):
    print("Strong Password")

else:
    print("Weak Password")
