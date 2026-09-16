# Assignment 28 
''' Question 2: Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")

'''

n = int(input("Enter the size of an array : "))

arr = []

print("Enter the Passwords ")
for i in range(n):
    arr.append((input()))

print(arr)    

pairs = []    

for i in range(n):
    for j in range(i+1,n):

        common = False

        for x in arr[i]:
            for y in arr[j]:
                if x==y:
                    common = True
                    break

            if common:
                break
        if not common:
            pairs.append((arr[i],arr[j]))

print(len(pairs))                  
print(pairs)                  

