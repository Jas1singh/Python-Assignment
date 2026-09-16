# Problem 38: Reverse words without split().

s = input("Enter the String : ")

result = ""

for i in range(len(s)):
    if s[i].isspace():
        result = " " + result
    else:
        result = s[i] + result

print(result)