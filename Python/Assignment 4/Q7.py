# Assignment 4
# Question 7 : Cricket Run Rate

Runs = int(input("Enter the total runs : "))
Overs = float(input("Enter the total overs : "))

Overs = Overs*10

last_digit = Overs%10
Overs = Overs//10

Total_Balls = Overs*6 + last_digit

Run_Rate= Runs/Overs

print("Toal Balls = ", int(Total_Balls))
print("Run Rate = ", format(Run_Rate, ".2f"))
