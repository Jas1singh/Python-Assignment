# Assignment 31 
''' Question 6: 
=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore

'''

cities = []
n = int(input("Enter the size of list : "))

print("Enter cities in list : ")
for i in range(n):
    cities.append(input())

d = {}

for city in cities:
    d[city] = d.get(city,0)+1

print(d)
# print("Most Downloads :", max(d, key=d.get))

max = max(d.values())
for k , v in d.items():
    if v == max:
        print("Most Downloads :",k)
