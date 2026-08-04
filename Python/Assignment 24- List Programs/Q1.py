# Assignment 24 
''' Question 1: Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3
'''

size = int(input("Enter the size of the list :"))

marks = []
sum = 0

for i in range(size):
    x = int(input("Enter the Marks : "))
    marks.append(x)

count = 0    
for i in marks:
    sum = sum + i

    if i > 75:
        count = count + 1

print("Marks are :",marks)
print("Highest =", max(marks))
print("Lowest =", min(marks)) 
print("Count Above 75 =", count)

