# Assignment 21
''' Question 6 : Find Occurrence of a Word in a String
               Product Review Analysis System '''

str = input("Enter the string :")
words = str.split()

word = input("Enter the word to find :")

count = 0

for w in words:
    if word==w:
        count = count + 1

print(count)