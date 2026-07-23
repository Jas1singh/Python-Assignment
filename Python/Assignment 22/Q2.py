# Assignment 22
''' Question 2 : Find the Most Frequently Occurring Word
                 News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.
Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india '''

str = input("Enter the string :")
words = str.split()

max = 0
maxWord = ""

for word in words:
    count = 0
    for w in words:
        if w==word:
            count = count + 1

    if count>max:
        max = count
        maxWord = word

print(maxWord)     