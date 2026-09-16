# Assignment 16
# Question 9 : Abundant Number Detector

n = int(input("Enter the number : "))

sum = 0 

for i in range(1,n):
    if n % i ==0:
        sum = sum + i

if sum > n:
    print("Abundant Number")

else:    
    print("Not Abundant Number")



