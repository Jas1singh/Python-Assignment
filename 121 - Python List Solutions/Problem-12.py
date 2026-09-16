''' Problem 12: Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

A = []
n = int(input("Enter the size of list : "))

for i in range(n):
    A.append(int(input()))

maxSum = A[0]
maxSub = []
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum = sum + A[j]
        if sum > maxSum:
            maxSum = sum
            maxSub = A[i:j+1]

print(maxSum)
# print(maxSub)

    

