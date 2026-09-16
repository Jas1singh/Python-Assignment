# Assignment 14
# Question 9 : Leap Year Event Scheduler – Multi-Year Analysis System

start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

count = 0
year = start

while year <= end:

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "→ Event Scheduled")
        count += 1
    else:
        print(year, "→ No Event")

    year += 1

print("\nTotal Leap Years =", count)
print("Total Events Scheduled =", count)