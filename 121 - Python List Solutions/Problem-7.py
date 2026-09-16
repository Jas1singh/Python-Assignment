''' Problem 7: 
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1
'''

size = int(input("Enter the size of list : "))
a = []
repeat = []
for i in range(size):
    a.append(int(input()))

for i in range(len(a)-1,-1,-1):
    count = 0
    for j in range(len(a)-1,-1,-1):
        if a[i] == a[j]:
            count+=1
    if count >1:
        repeat.append(a[i])

for i in repeat:
    a.remove(i)   

print("Output")
for i in a:
    print(i)
