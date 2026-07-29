# Assignment 22
''' Question 1 : Find the Longest Substring Without Repeating Characters
                 Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.
To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc '''

str = input("Enter the String : ")

max = 0
longest = ""

words = str.split()

for word in words:
    if len(word)>max:
        longest = word
print(longest)        



