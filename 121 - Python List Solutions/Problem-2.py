''' Problem 2: Remove Duplicates from Sorted Array 
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

size = int(input("Enter the size of list : "))
a = []

for i in range(size):
    a.append(int(input()))

a.sort()
count = 0

for i in range(len(a)-1,0,-1):
    if a[i]==a[i-1]:
        a.pop(i)
        a.append("_")

print("output")
for i in range(len(a)):
    if not a[i]=="_":
        count+=1
        
print(count)    
print(a)

