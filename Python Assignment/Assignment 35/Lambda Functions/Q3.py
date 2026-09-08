# Assignment 35 - Lambda Functions 
''' Question 3: 
Cricket Tournament – Highest Run Scorer

A cricket academy wants to reward the player who scored the highest number of runs in a tournament.

Write a Python program to identify the highest run scorer using reduce() and a lambda expression.

Input
players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]
Expected Output
Highest Run Scorer: Rohit

'''

from functools import reduce
n = int(input("Enter no. of Players : "))
players = []
for i in range(n):
    names = input("Enter player name : ")
    score = int(input("Enter player age : "))
    players.append((names,score))
    print()

result = reduce(lambda x,y:x if x[1]>y[1] else y,players)
print ("Highest Run Scorer: ",result[0])