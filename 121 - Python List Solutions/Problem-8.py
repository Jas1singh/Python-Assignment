''' Problem 8: Contains Duplicates
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.
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

    if count==2:
        print("True")
        break

else:
    print("All elements are distinct.")
        
    



