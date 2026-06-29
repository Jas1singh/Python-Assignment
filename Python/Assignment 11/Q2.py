# Assignment 11
# Question 2 : Next Prime ID Generator

n = int(input())

num = n + 1

while True:
    prime = True

    if num <= 1:
        prime = False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                prime = False
                break

    if prime:
        print("Next Prime =", num)
        break

    num += 1