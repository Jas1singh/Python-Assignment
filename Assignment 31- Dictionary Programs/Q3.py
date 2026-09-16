# Assignment 31 
''' Question 3: 
=========================================
WEBSITE PAGE VISIT TRACKER
==========================

A website records page visits.

pages = ["Home","About","Home","Contact","Home","About"]

Write a program to:

* Count visits of each page using a dictionary.
* Display page name and visit count.

Sample Output:
Home visited 3 times
About visited 2 times
Contact visited 1 time

'''

Pages = []
n = int(input("Enter the size of list : "))

print("Enter pages in list : ")
for i in range(n):
    Pages.append(input())

d = {}

for page in Pages:
    d[page] = d.get(page,0)+1

for k , v in d.items():
    print(k, "visited",v, "times")