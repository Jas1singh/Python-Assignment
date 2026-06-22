# Assignment 4
# Question 4 : Travel Distance Calculation

Speed = int(input("Enter Speed of the Vehicle : "))
Time1 = int(input("Enter total hours  : "))
Time2= int(input("Enter total minutes  : "))

Time2 = Time2/60

Total_Time = Time1+Time2

Distance = Speed * Total_Time

print("Total Time = ", Total_Time)
print("Distance = ", Distance)


