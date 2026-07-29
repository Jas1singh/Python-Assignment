# Assignment 11
# Question 9 : Even Odd Difference Prime System

n = int(input())

temp = n

even = 0
odd = 0

while temp > 0:
    digit = temp % 10

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    temp //= 10

diff = abs(even - odd)

prime = True

if diff <= 1:
    prime = False
else:
    for i in range(2, diff // 2 + 1):
        if diff % i == 0:
            prime = False
            break

print("Even Count =", even)
print("Odd Count =", odd)
print("Difference =", diff)

if prime:
    print("Prime")
else:
    print("Not Prime")