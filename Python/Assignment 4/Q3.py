# Assignment 4
# Question 3 : Student Marks Analysis

Marks1 = int(input("Enter Marks 1 : "))
Marks2 = int(input("Enter Marks 2 : "))
Marks3 = int(input("Enter Marks 3 : "))
Marks4 = int(input("Enter Marks 4 : "))
Marks5 = int(input("Enter Marks 5 : "))

total_Subjects = 5

Total = Marks1+Marks2+Marks3+Marks4+Marks5
Avg = Total/total_Subjects
Percentage = (Total/(total_Subjects*100)) * 100

print("Total = ", Total)
print("Average = ", Avg)
print("Percentage = ", Percentage)