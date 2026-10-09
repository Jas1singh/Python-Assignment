# Assignment 48 - File Handing 
''' Question 9: 
Find the Most Frequently Used Word

A content-analysis application wants to identify the most frequently used word in an article.

Write a Python program that reads a file named "article.txt" and finds the word that occurs the maximum number of times.

Input File: article.txt

Python is easy.
Python is powerful.
Python is popular.
Java is also popular.

Expected Output:

Most Frequently Used Word: Python
Frequency: 3
'''

with open("article.txt", "r") as file:
    content = file.read()

words = content.split()

word_count = {}

for word in words:
    word = word.strip(".,!?;:")
    word = word.lower()

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


most_frequent_word = ""
highest_frequency = 0

for word in word_count:
    if word_count[word] > highest_frequency:
        highest_frequency = word_count[word]
        most_frequent_word = word


print("Most Frequently Used Word:", most_frequent_word.capitalize())
print("Frequency:", highest_frequency)
