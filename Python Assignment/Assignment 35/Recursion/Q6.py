# Assignment 35 - Recursion 
''' Question 5:
Hospital Record System (Search Digit)


A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

Task

Write a recursive function to determine whether a given digit is present.

Input
Enter Patient ID:
5837264

Enter Digit:
7
Output
Digit Found

 '''

def findDigit(n,d):
    temp = str(n)
    if n==0:
        return False

    if str(d) in temp:
        return True

    return findDigit(n//10,d)

n = int(input("Enter Patient ID :"))

d = int(input("Enter the search digit : "))

if findDigit(n,d):
    print("Digit Found")

else:
    print("Not Found")
