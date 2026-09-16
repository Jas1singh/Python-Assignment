# Assignment 11
# Question 5 : Prime Security Code Checker – Advanced

n = int(input())

num = n + 1

while True:
    prime = True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Next Prime ID =", num)
        print("Gap =", num - n)
        break

    num += 1