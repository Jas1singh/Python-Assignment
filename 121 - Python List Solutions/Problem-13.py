''' Problem 13:  Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
'''

A = []
n = int(input("Enter the size of list : "))

for i in range(n):
    A.append(int(input()))

max = 0
result = []

for i in range(n):
     if A[i]>max :
          max = A[i]

for i in range(1,max+1):
     if i not in A:
          result.append(i)

if len(result) == 0:
    result.append(max + 1)          

print(result)
     