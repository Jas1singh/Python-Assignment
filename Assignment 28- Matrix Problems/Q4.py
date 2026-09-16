# Assignment 28 
''' Question 4: Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.

Note: can you take care of the duplicates without using any additional Data Structure?

Example 1:

Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}

Output: 20 80

Explanation: 20 and 80 are the only
common elements in A, B and C.

'''

n1 = int(input("Enter the size of array A : "))
n2 = int(input("Enter the size of array B : "))
n3 = int(input("Enter the size of array C : "))

A = []
print("Enter elements of A")
for i in range(n1):
    A.append(int(input()))

B = []
print("Enter elements of B")
for i in range(n2):
    B.append(int(input()))

C = []
print("Enter elements of C")
for i in range(n3):
    C.append(int(input()))

Result = []
for i in range(n1):
    if A[i] in B and A[i] in C:
        if A[i] not in Result:
            Result.append(A[i])

for i in range(n2):
    if B[i] in A and B[i] in C:
        if B[i] not in Result:
            Result.append(C[i])

for i in range(n3):
    if C[i] in A and C[i] in A:
        if C[i] not in Result:
            Result.append(C[i])

print(Result)              







