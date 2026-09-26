# Problem 17: Remove occurrences of a character.

s = input("Enter the String : ")
ch = input("Enter the character : ")

result = ""

for c in s:
    if c!=ch:
        result+=c

print(result)      
