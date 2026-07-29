# Assignment 15
# Question 2 : Print Square, Cube and Square Root of all numbers from 1 to N

n = int(input("Enter the range : "))

for i in range(1,n+1):
    Square = i * i
    Cube = i * i * i
    SquareRoot = i ** 0.5

    print(" Square :",Square," Cube :",Cube," SquareRoot :",SquareRoot, end="\n")