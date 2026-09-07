# Assignment 35 - Recursion 
''' Question 3: 
Security PIN Verification (Palindrome Number)

A bank allows customers to choose a special PIN. For promotional purposes, the bank rewards customers whose PIN is a palindrome (reads the same from left to right and right to left).

As a software developer, write a recursive program to verify whether the entered PIN is a palindrome.

Task

Write a recursive function to reverse the given number and determine whether it is a palindrome.

Input 1
Enter PIN:
1221
Output 1
Palindrome Number
Input 2
Enter PIN:
1234
Output 2
Not a Palindrome Number

'''

def reverse(n, reversed=0):
    if n == 0:
        return reversed
    
    else:
        last_digit = n % 10
        reversed = (reversed * 10) + last_digit
        return reverse(n // 10, reversed)

n = int(input("Enter a decimal number : "))
rev = reverse(n)

if rev == n:
    print("Palindrome Number")

else:
    print("Not a Palindrome Number")