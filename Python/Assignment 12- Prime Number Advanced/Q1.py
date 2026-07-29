# Assignment 12
# Question 1 : Triple Operation Prime Verification System

n = int (input("Enter the Number : "))
temp = n
sum = 0
rev = 0

while temp>0:
    digit = temp % 10
    sum = sum + digit

    rev = rev * 10 + digit

    temp = temp // 10

difference = abs(n-rev) 
final = sum + difference
print("Sum of digits =",sum)
print("Reverse =",rev)
print("Difference =",difference)
print("Final Result =",final)

if final<=1:
    print("Not Prime")

else:
    i = 2
    while i<final:
        if final % i ==0:
            print("Not Prime")
            break
        i = i + 1

    else:
        print("Prime number")    


