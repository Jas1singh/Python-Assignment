# Assignment 19
# Question 5 : Palindrome Product Code Checker

code = input("Enter the code : ").lower()

rev = code[::-1]

if code == rev:
    print ("palindrome Code")

else:
    print("Not a Palindrome Code")    

