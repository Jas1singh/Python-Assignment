# Assignment 7
# Question 14 : Floor Movement System (Elevator)

current = int(input("Enter current floor: "))
destination = int(input("Enter destination floor: "))

if current < destination:
    while current <= destination:
        print(current, end=" -> ")
        current += 1

elif current > destination:
    while current >= destination:
        print(current, end=" -> ")
        current -= 1

else:
    print("Already on the same floor")

