# Assignment 7
# Question 9 : Check All Digits Are Even

num = int(input("Enter number: "))

check = 1

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        check = 0
        break

    num = num // 10

if check==1:
    print("All Even")
else:
    print("Not All Even")

