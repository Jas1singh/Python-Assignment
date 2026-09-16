# Assignment 11
# Question 7 : Composite Number Detector – Risk Version

n = int(input())

temp = n
total = 0

while temp > 0:
    total += temp % 10
    temp //= 10

prime = True

if total <= 1:
    prime = False
else:
    for i in range(2, total // 2 + 1):
        if total % i == 0:
            prime = False
            break

print("Sum =", total)

if prime:
    print("Lucky Number")
else:
    print("Normal Number")