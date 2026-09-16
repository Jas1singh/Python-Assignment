# Assignment 29 
''' Question 7: A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)
'''


from collections import namedtuple

n = int(input("Enter no. of Players :"))

player = namedtuple("Player",["PlayerID","Name","Runs"])

pla = []
for i in range(n):
    print("\nEnter Details :")
    id = int(input("Enter ID of Player :"))
    name = input("Enter Name of Player :")
    runs = int(input("Enter Runs Scored :"))

    P = player(id,name,runs)
    pla.append(P)
  
max = 0
min = float('inf')
sum = 0 
print("\nDisplay Details")
for i in pla:
    print(i.PlayerID," ",i.Name," ",i.Runs)


for i in pla:
    if i.Runs>max:
        max = i.Runs

    if i.Runs < min:
        min = i.Runs

for i in pla:
    if i.Runs == max:
        print("\nHighest Scorer: ")
        print(i.PlayerID," ",i.Name," ",i.Runs)
       

    if i.Runs == min:
        print("\nLowest Scorer: ")
        print(i.PlayerID," ",i.Name," ",i.Runs)
     

    sum = sum + i.Runs

print("\nTotal Runs : ",sum)
print("\nAverage : ",sum / n)

print("\nPlayers Scoring More Than 50 Runs: ")
for  i in pla:
    if i.Runs>50:
        print(i.PlayerID," ",i.Name," ",i.Runs)

        
