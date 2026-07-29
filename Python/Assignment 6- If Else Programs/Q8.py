# Assignment 6
# Question 8 : Weather Monitoring System

temperature = float(input("Enter temperature: "))

if temperature < 0:
    condition = "Freezing"
elif temperature <= 20:
    condition = "Cold"
elif temperature <= 35:
    condition = "Warm"
else:
    condition = "Hot"

print("Weather Condition:", condition)

