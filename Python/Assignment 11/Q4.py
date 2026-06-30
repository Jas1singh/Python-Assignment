# Assignment 11
# Question 4 : Prime Checker Advanced 

n = int(input())

prime = True

if n <= 1:
    prime = False
else:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            prime = False
            break

if prime:
    print("Prime Number")

    num = n + 1

    while True:
        p = True

        for i in range(2, num // 2 + 1):
            if num % i == 0:
                p = False
                break

        if p:
            print("Next Prime =", num)
            break

        num += 1

else:
    print("Not Prime")

    num = n - 1

    while num >= 2:
        p = True

        for i in range(2, num // 2 + 1):
            if num % i == 0:
                p = False
                break

        if p:
            print("Previous Prime =", num)
            break

        num -= 1