# Assignment 16
# Question 2 : Fibonacci Series Generator

n = int(input("Enter the no. terms : "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a+b
    a = b
    b = c
    
