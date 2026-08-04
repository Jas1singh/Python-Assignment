# Assignment 24 
''' Question 2: Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
'''

size = int(input("Enter the size of the list :"))

salary = []
sum = 0
avg = 0
aboveAvg = []

for i in range(size):
    x = int(input("Enter the Marks : "))
    salary.append(x)

for i in salary:
    sum = sum + i
    avg = sum / size
   
print("Salaries are : ",salary)
print("Average : ",int(avg))

for i in salary:
    if i > avg:
        aboveAvg.append(i)
        print("Above Average: ",aboveAvg)








