# Assignment 16
# Question 5 : Automorphic Number Lock

n = int (input("Enter the number :"))
temp = n
count = 0
square = n ** 2

while temp >0:
    count = count + 1
    temp = temp // 10

if square % 10**count == n:
    print("Automorphic Number")

else:     
    print("Not Automorphic Number") 

    

