# Assignment 25 
''' Question 6: A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0

'''

n = int(input("Enter the size of the list: "))

nums = []
Prime = []
NonPrime = []

for i in range(n):
    x = int(input("Enter the numbers: "))
    nums.append(x)

for i in nums:
    if i <= 1:
        NonPrime.append(i)
        continue

    for j in range(2, i // 2 + 1):
        if i % j == 0:
            NonPrime.append(i)
            break
    else:
        Prime.append(i)

total = 0
print("Prime IDs:", end=" ")
for i in Prime:
    total = total + i
    if i not in Prime:
        Prime.append(i)

print("Prime IDs:", Prime)
print("Sum = ", total)

if Prime:
    print("Maximum Prime ID:", max(Prime))
else:
    print("-1")

print("Count = ", len(Prime))