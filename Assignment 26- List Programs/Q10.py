# Assignment 26 
''' Question 10: Find Duplicate Numbers
==========================

Scenario

A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found
'''

n = int(input("Enter the Size :"))
arr = []

for i in range(n):
    arr.append(int(input()))

Duplicates = []

a = arr
found = False

for i in arr:
     for j in a:
        a.remove(j)
        if j in a:
            Duplicates.append(i)
            found = True

if found==False:
    print("No Duplicate Numbers Found")

else:
    print("Count of Duplicates = ",len(Duplicates))
    print("Count of Duplicates = ",sorted(Duplicates))
 