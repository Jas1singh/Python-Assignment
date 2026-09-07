# Assignment 26 
''' Question 8: Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found
'''

n = int(input("Enter the Size :"))
arr = []

for i in range(n):
    arr.append(int(input()))

max = 0
maxElement = None

for i in arr:
    count = 0
    for j in arr:
        if i==j:
            count +=1

    if count > max:
         max = count
         maxElement = i


if max > n//2:
        print("Majority Element = ",maxElement)   

else:
     print("No Majority Element Found")    

     


            
