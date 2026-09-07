# Assignment 11
# Question 1 : Prime Security Code Checker

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
else:
    print("Not Prime")