# Assignment 26 
''' Question 3: Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1

Test Case 3

Input:
[1, 2, 4, 5]

Output:
Missing Number = 3
'''

n = int(input("Enter the Size :"))
arr = []

for i in range(n):
    arr.append(int(input()))
    while i == 0 and arr[0] not in (1, 2):
        print("Enter only 1 to N sequence with missing one value")
        arr[0] = int(input("Enter Number Again : "))

for i in range(len(arr)):
        if arr[0]>1:
            print("Missing Number = ",arr[i]-1)
            break
        
        elif i+1<len(arr) and arr[i+1]!=arr[i]+1:
            print("Missing Number = ",arr[i]+1)
            break

else:
     print("No missing number in a sequence")    


# for i in range(len(arr)):
#     if i==0:
#         if arr[i]>1:
#             print("Missing Number = ",arr[i]-1)
#             break
        
#     else:
#         if arr[i+1]!=arr[i]+1:
#             print("Missing Number = ",arr[i]+1)
#             break