# Assignment 11
# Question 8 : Prime Sum Lucky Number

n = int(input())

temp = n

largest = 0
smallest = 9

while temp > 0:
    digit = temp % 10

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    temp //= 10

total = largest + smallest

prime = True

if total <= 1:
    prime = False
else:
    for i in range(2, total // 2 + 1):
        if total % i == 0:
            prime = False
            break

print("Largest =", largest)
print("Smallest =", smallest)
print("Sum =", total)

if prime:
    print("Prime")
else:
    print("Not Prime")