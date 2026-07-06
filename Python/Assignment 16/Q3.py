# Assignment 16
# Question 3 : Fibonacci Population Growth Tracker

n = int(input("Enter the no. of Months : "))

a = 0
b = 1
sum = 0
count =0

print("Population Growth : ")
for i in range(n):
    if i == 0:
        c = 0

    elif i == 1:
        c = 1
        
    else:
        c = a + b
        a = b
        b = c

    sum = sum + c

    if c>5:
        count+=1

print("Total Population =",sum)
print("Months with Population > 5 = ",count)
