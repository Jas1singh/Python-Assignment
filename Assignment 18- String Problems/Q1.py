# Assignment 18
# Question 1 : Vowel Counter in Customer Feedback

message = input("Enter feedback message : ")

count = 0
vowel = "aeiouAEIOU"

for m in message:
    if m in vowel:
        count = count + 1

print("Total vowels :",count)