# Assignment 35 - Recursion 
''' Question 2: 
Binary Converter for Embedded System

An embedded systems company develops microcontrollers that understand only binary values. Engineers enter decimal numbers, and the software must convert them into binary before sending them to the device.

As a software developer, write a recursive program to perform this conversion.

Task

Write a recursive function to convert a decimal number into its binary representation.

Input
Enter a decimal number:
25
Output
Binary Number = 11001

Note: Do not use Python's built-in bin() function.

'''

def deci_To_bin(n):
    if n==0:
        return "0"

    elif n==1:
        return "1"

    else:
        return deci_To_bin(n//2) + str(n%2)

n = int(input("Enter a decimal number : "))
print(deci_To_bin(n))