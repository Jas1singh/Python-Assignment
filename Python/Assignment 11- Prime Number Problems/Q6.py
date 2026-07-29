# Assignment 11
# Question 6 : Next Prime ID Generator – Smart Version

n = int(input())

count = 0
smallest = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

        if i != 1 and smallest == 0:
            smallest = i

if count > 2:
    print("Composite Number")
else:
    print("Not Composite")

print("Factors Count =", count)
print("Smallest Factor =", smallest)