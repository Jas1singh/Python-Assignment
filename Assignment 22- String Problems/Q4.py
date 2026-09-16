# Assignment 22
'''Question 4 : Find All Characters with Maximum Frequency
                Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.
The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d
'''

str=input("Enter input:")
c=0 

for i in str:
    count=0
    for j in str:
        if i==j:
         count+=1
    if count>c:
        c = count       

stored = ""
for i in str:
    count = 0
    for j in str:
        if i == j:
            count += 1
    if count == c and i not in stored:
        print(i, end=" ")
        stored = stored + i
