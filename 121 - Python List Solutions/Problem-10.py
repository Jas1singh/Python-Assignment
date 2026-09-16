''' Problem 10: Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''

A = []
n = int(input("Enter the size of list : "))

for i in  range(n):
    A.append(int(input()))

for i in range(n):
    if A[i]==0:
        A.remove(A[i])
        A.append(0)

print(A)        



