# Assignment 16
# Question 1 : Leap Year Event Scheduler – Multi-Year Analysis System

start = int (input("Enter the start year : "))
end = int (input("Enter the end year : "))

count = 0

for year in range(start,end+1):
    if (year%4==0 and year%100!=0) or year%400==0:
        print(year," -> Event Scheduled")
        count = count + 1

    else:
        print(year," -> No Event")  


print("Total Leap Years =",count)
print("Total Events Scheduled =",count)