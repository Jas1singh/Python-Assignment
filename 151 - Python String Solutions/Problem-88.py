# Problem 88:

s = "aaabc"
d = 2

result = ""
remaining = list(s)

while remaining:
    found = False

    for i in range(len(remaining)):
        ch = remaining[i]

        if len(result) < d or result[-d] != ch:
            result += ch
            remaining.pop(i)
            found = True
            break

    if not found:
        print("Not possible")
        break

else:
    print(result)
