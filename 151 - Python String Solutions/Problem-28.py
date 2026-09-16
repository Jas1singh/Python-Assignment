# Problem 28:

s = input("Enter the String : ")
word = input("Enter the word: ")

words = s.split()
count = 0

for w in words:
    if w == word:
        count+=1

print(count)
