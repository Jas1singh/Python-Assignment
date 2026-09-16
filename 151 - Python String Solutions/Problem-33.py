# Problem 33:  Find the longest word.

s = input("Enter the String : ")

words = s.split()

max = 0
maxWord = ""

for word in words:
    if len(word)>max:
        max = len(word)
        maxWord = word

print(maxWord)

