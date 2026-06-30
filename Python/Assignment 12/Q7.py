# Assignment 12
# Question 7 : Alternate Digit Prime Checker

n = int (input("Enter the Number : "))
temp = n
sum = 0
count = len(str(n))

for i in range(1,count,2):
    digit = temp % 10
    sum = sum + digit

    temp = temp // 10  

print("Alternate sum = ",sum)     

if sum<=1:
    print("Not Prime")

else:
    i = 2
    while i<sum:
        if sum % i ==0:
            print("Not Prime")
            break
        i = i + 1

    else:
        print("Prime number")    



