# Assignment 48 - File Handing 
''' Question 8: 
Count Words Starting With a Particular Letter

A search engine wants to analyze words beginning with a particular character.

Write a Python program that:

1. Reads a file named "article.txt".
2. Accepts a character from the user.
3. Counts the number of words starting with that character.

Input File: article.txt

Python programming provides powerful features.
Programming helps developers build applications.

Sample Input:

Enter character: p

Expected Output:

Words starting with 'p': <display count>

'''

with open("article.txt", "r") as file:
    content = file.read()

character = input("Enter character: ")

words = content.split()

count = 0

for word in words:
    word = word.strip(".,!?;:")

    if word.lower().startswith(character.lower()):
        count += 1

print("Words starting with '" + character + "':", count)
