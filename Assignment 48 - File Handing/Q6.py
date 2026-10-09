# Assignment 48 - File Handing 
''' Question 6: 
Find the Longest Word

A document-processing application needs to identify the longest word in a text document.

Write a Python program that reads a file named "article.txt" and finds the longest word in the file.

Input File: article.txt

Python programming language is powerful.
Developers use Python for application development.

Expected Output:

Longest Word: programming
Length: 11

'''

with open("article.txt", "r") as file:
    content = file.read()

words = content.split()

longest_word = ""

for word in words:
    # Remove punctuation
    word = word.strip(".,!?;:")

    if len(word) > len(longest_word):
        longest_word = word


print("Longest Word:", longest_word)
print("Length:", len(longest_word))

