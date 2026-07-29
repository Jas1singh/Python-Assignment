# Assignment 16
# Question 7 : Adam Number Verification System

n =  int(input("Enter the Number : "))

n_rev = 0 
rev = 0
square = n ** 2

while n > 0 :
    d = n % 10
    n_rev = n_rev * 10 + d
    n = n // 10

print(n_rev) 

n_revSquare = n_rev ** 2

print(n_revSquare)


temp = square

while temp > 0 :
      digit = temp % 10
      rev = rev * 10 + digit
      temp = temp // 10
 

if rev == n_revSquare :
     print("Adam Number")

else:
     print("Not Adam Number")
