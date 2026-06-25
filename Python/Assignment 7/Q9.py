# Assignment 7
# Question 9 : Check All Digits Are Even

num = int(input("Enter number: "))

flag = True

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        flag = False
        break

    num //= 10

if flag:
    print("All Even")
else:
    print("Not All Even")

