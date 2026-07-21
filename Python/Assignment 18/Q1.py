# Assignment 18
# Question 1 : Vowel Counter in Customer Feedback

message = input("Enter feedback message : ").lower()

count = 0
vowel = "aeiou"

for m in message:
    if m in vowel:
        count = count + 1

print("Total vowels :",count)