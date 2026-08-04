# Assignment 24 
''' Question 4: Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
'''

size = int(input("Enter the size of the list: "))

nums = []
Palindrome = []

for i in range(size):
    x = int(input("Enter the numbers: "))
    nums.append(x)

for i in nums:
    rev = 0
    temp = i
    while temp>0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp= temp//10

    if i == rev:
        print(i)
        Palindrome.append(i)   


print("Palindromes :", end=" ")
for i in Palindrome:
    print(i, end=" ")

print("\nCount:", len(Palindrome))

if Palindrome:
    print("Largest Prime Number:", max(Palindrome))
else:
    print("Largest Prime Number: Not Available")

print("Sorted Prime List:", sorted(Palindrome))