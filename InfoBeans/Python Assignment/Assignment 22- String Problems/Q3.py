# Assignment 22
''' Question 3 : Replace Consecutive Duplicate Characters with Single Character
                 Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.
Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
'''

str = input("Enter the string: ")

result = ""

for ch in str:
    if result == "" or ch != result[-1]:
        result += ch

print(result)    

# Alternate
# s = input("Enter the string: ")

# result = s[0]

# for i in range(1, len(s)):
#     if s[i] != s[i - 1]:
#         result += s[i]

# print(result)

