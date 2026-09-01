# Assignment 18
# Question 3 : Character Occurrence Checker in Product Review

message = input("Enter feedback message : ").lower()
ch = input("Enter character to check : ").lower()

count = 0

for m in message:
    if m == ch:
        count = count + 1

print("Total vowels :",count)