# Problem 40: Search all occurrences of a word.

s = input("Enter the String : ")
ch = input("Enter the character : ")

words = s.split()

for i in range(len(words)):
    if ch == words[i]:
        print(i , end=" ")