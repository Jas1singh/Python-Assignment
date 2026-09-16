# Assignment 26 
''' Question 4: Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3
'''

n = int(input("Enter the Size :"))
arr = []

for i in range(n):
    arr.append(int(input()))


max = 0

for i in range(len(arr)):
        current = arr[i]
        count = 1

        for j in range(len(arr)):
            if current+1 in arr:
                 current+=1
                 count+=1
            else:
                 break     

        if count > max:
             max = count    
     
print("Longest Consecutive Length = ",max)