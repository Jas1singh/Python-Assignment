# Assignment 20
# Question 6 : Advanced Student Registration Data Processing System

RegCode= input("Enter the Registration Code :")

alphabet = ""
digit = ""

for ch in RegCode:
    if ch.isdigit():
        digit = digit + ch

    elif ch.isalpha():
        ch = ch.lower()
        if ch not in alphabet:
            alphabet = alphabet + ch

alphabet = "".join(sorted(alphabet))
digit = "".join(sorted(digit,reverse=True))


if digit=="":
    print("No Digits Found")

else:
    result = alphabet + digit
    print("Result:",result)