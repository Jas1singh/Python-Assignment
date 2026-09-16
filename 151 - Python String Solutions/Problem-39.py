# Problem 39:  Search all occurrences of a character.

s = input("Enter the String : ")
ch = input("Enter the character : ")

for i in range(len(s)):
    if ch == s[i]:
        print(i , end=" ")