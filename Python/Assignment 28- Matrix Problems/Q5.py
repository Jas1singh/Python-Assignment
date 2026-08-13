# Assignment 28 
''' Question 5: Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers.

Your task is to create an array of alternate positive and negative numbers
without changing the relative order of positive and negative numbers.

Note: Array should start with positive number.

Example 1:

Input:
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}

Output:
9 -2 4 -1 5 -5 0 -3 2

Example 2:

Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}

Output:
5 -5 2 -2 4 -8 7 1 8 0

'''


n = int(input("Enter the size of array: "))

A = []

print("Enter elements in Array")
for i in range(n):
    A.append(int(input()))

R = []
for i in range(n):
    R.append(0)

positive = 0
negative = 1

for i in A:
    if i >= 0:
        R[positive] = i
        positive += 2
        
    else:
        R[negative] = i
        negative += 2


# R = [[0] * 3] * 3
# print(R)