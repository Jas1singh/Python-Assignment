# Assignment 16
# Question 8 : Trimorphic Number Analyzer

n = int (input("Enter the number :"))
temp = n
count = 0
cube = n ** 3

while temp >0:
    count = count + 1
    temp = temp // 10

if cube % 10**count == n:
    print("Trimorphic Number")

else:     
    print("Not Trimorphic Number") 

