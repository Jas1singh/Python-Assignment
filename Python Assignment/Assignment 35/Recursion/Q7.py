# Assignment 35 - Lambda Functions 
''' Question 6:
Mobile Recharge System

A telecom company issues lucky recharge coupons only if the coupon number is prime.

Task

Write a recursive function to determine whether a given number is prime.

Input
Enter Coupon Number:
29
Output
Prime Number

 '''

def checkPrime(n,i):
    if n<=1:
        return False
    
    if i>n//2:
        return True
    
    if n%i==0:
        return False

    else:
        return checkPrime(n,i+1)

n = int(input("Enter the number : "))

if checkPrime(n,2):
    print("Prime")
else:
    print("Not Prime")
    