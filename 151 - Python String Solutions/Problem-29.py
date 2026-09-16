# Problem 29: Remove occurrences of a word.

s = input("Enter the String : ")
word = input("Enter the word: ")

words = s.split()

result =""

for w in words:
    if w == word:
        continue
    else:
        result = result + w + " "

print(result)