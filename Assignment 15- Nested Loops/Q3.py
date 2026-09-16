# Assignment 15
# Question 3 : Find out all the leap years between two entered years

start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

year = start

while year <= end:

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)

    year += 1