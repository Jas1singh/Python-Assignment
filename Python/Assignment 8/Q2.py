# Assignment 8
# Question 2 : Smallest Digit in Number

Serial_Number = (input("Enter the Serial_Number : "))
length = len(Serial_Number)

Lowest = 9

Serial_Number = int(Serial_Number)

while (Serial_Number>0):
    digit = Serial_Number % 10

    if digit<Lowest:
        Lowest = digit
    Serial_Number = Serial_Number // 10

print("Smallest digit = ",Lowest)

