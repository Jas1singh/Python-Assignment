# Assignment 14
# Question 2 : Perfect Number Analyzer

a = int (input("Enter the Strating Number : "))
b = int (input("Enter the Ending Number : "))

print("Perfect Numbers are : ") 
for i in range(a, b+1):
    sum = 0
    for j in range(1,i//2+1):
        if i % j == 0:
            sum = sum + j

    if sum == i and i !=0:
        print(i)        
