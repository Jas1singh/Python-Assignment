# Assignment 3
# Question 15 : Average Speed for Multiple Trips

distance1 = float(input("Enter distance 1 : "))
time1 = float(input("Enter time in hours : "))

distance2 = float(input("Enter distance 2 : "))
time2 = float(input("Enter time in hours: "))

totalDistance = distance1 + distance2
totalTime = time1 + time2

avgSpeed = totalDistance / totalTime

print("Average Speed =", avgSpeed, "km/h")

