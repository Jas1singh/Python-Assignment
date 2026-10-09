# Assignment 48 - File Handing 
''' Question 5: 
Count Vowels and Consonants
A language-learning application wants to analyze the characters used in a paragraph.

Write a Python program that reads a file named "paragraph.txt" and counts:

1. Total number of vowels
2. Total number of consonants

Ignore numbers, spaces and special characters.

Input File: paragraph.txt

Python Programming is Interesting.

Expected Output:

Total Vowels: <display count>
Total Consonants: <display count>

'''

with open("paragraph.txt", "r") as file:
    content = file.read()

vowels = 0
consonants = 0

for ch in content:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Total Vowels:", vowels)
print("Total Consonants:", consonants)
