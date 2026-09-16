# Assignment 10
# Question 8 : Mirror Difference Transaction Verification System

num = int(input("Enter the number : "))

temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

diff = abs(num - rev)

if diff == 0:
    digits = 1
else:
    digits = 0
    t = diff

    while t > 0:
        digits += 1
        t = t // 10

print("Reverse =", rev)
print("Difference =", diff)
print("Digits =", digits)

if diff == 0:
    print("Perfect Match")

elif diff % 9 == 0:
    print("Verified")

else:
    print("Rejected")