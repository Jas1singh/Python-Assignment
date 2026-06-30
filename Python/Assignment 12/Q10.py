# Assignment 12
# Question 10 : Lift Mode Operation – Advanced Smart Elevator System

mode = int(input())

if mode == 1:
    current = int(input())
    destination = int(input())

    for i in range(current, destination + 1):
        print(i, end=" ")

elif mode == 2:
    current = int(input())
    destination = int(input())

    for i in range(current, destination - 1, -1):
        print(i, end=" ")

elif mode == 3:
    destination = int(input())

    for i in range(0, destination + 1, 2):
        print(i, end=" ")

else:
    for i in range(4):
        print("Emergency Alarm")

