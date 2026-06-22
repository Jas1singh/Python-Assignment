# Python Assignment 2
# Question 1

total_seconds = int(input("Total event duration in seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")