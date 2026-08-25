# Assignment 31 
''' Question 5: 
=========================================
WORD LENGTH GROUPING
====================

A content management system stores article tags.

tags = ["python","java","api","react","html","css"]

Write a program to:

* Group words according to their length.
* Store result in dictionary.

Sample Output:
{
3:['api','css'],
4:['java','html'],
5:['react'],
6:['python']
}

'''

Tags = []
n = int(input("Enter the size of list : "))

print("Enter tages in list : ")
for i in range(n):
    Tags.append(input())

g = {}

for word in Tags:
    l = len(word)
    if l not in g:
        g[l] = []
    g[l].append(word)   

for length in sorted(g):
    print(length, ":", sorted(g[length]))
