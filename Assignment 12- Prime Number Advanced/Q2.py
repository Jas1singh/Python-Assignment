# Assignment 12
# Question 2 : Multi Stage Prime Lock System

n = int (input("Enter the Number : "))
temp = n
sum = 0
product = 1
dcount = 0

while temp>0:
    digit = temp % 10
    sum = sum + digit

    product = product * digit

    temp = temp // 10

difference = (product-sum)

diff = difference

while diff>0:
    dcount = dcount + 1
    diff = diff // 10

final = dcount + difference

print("Sum of digits =",sum)
print("Product =",product)
print("Difference =",difference)
print("Digits =",dcount)
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