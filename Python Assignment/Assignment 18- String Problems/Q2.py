# Assignment 18
# Question 2 : Space Counter in Chat Messages

message = input("Enter feedback message : ").lower().strip()

count = 0
space = " "

for m in message:
    if m in space:
        count = count + 1

print("Total vowels :",count)