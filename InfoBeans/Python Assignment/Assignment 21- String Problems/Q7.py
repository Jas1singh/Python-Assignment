# Assignment 21
''' Question 7 : Remove Duplicate Words from a String
                 Voice Assistant Noise Correction System '''

str = input("Enter the string :")
words = str.split()

cleaned = ""

for w in words:
    if w not in cleaned:
        cleaned = cleaned + w + " "

print(cleaned)