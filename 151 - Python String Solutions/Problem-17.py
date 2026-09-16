# Problem 17:

s = input("Enter the String : ")
ch = input("Enter the character : ")

result = ""

for c in s:
    if c!=ch:
        result+=c

print(result)      
