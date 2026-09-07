# Assignment 8
# Question 1 : Largest Digit in Number

password = (input("Enter the Password : "))
length = len(password)

highest = 0 

password = int(password)

for i in range(length+1):
    digit = password % 10

    if digit>highest:
        highest = digit

    password = password // 10

print("Largest digit = ",highest)

