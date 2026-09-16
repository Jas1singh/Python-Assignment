# Assignment 18
# Question 4 : Consonant Counter in Student Name Record

message = input("Enter Student name : ")

count = 0
vowel = "aeiouAEIOU"

for m in message:
    if m not in vowel and m!=" ":
        count = count + 1

print("Total Consonants :",count)