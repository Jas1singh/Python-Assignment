# Problem 147:

s = "a3b2c1"

result = ""
i = 0

while i < len(s):

    ch = s[i]
    i += 1

    number = ""

    while i < len(s) and s[i].isdigit():
        number += s[i]
        i += 1

    result += ch * int(number)

print(result)
