# Assignment 11
# Question 3 : Composite Number Detector

n = int(input())

composite = False

if n > 3:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            composite = True
            break

if composite:
    print("Composite Number")
else:
    print("Not Composite")