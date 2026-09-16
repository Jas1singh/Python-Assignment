# Problem 34: Find the shortest word

s = input("Enter the String : ")

words = s.split()

min = len(s)
minWord = ""

for word in words:
    if len(word)<min:
        min = len(word)
        minWord = word

print(minWord)