# Problem 138:

s = "aab"

result = []

for mask in range(1 << (len(s) - 1)):

    parts = []
    start = 0

    for i in range(len(s) - 1):
        if mask & (1 << i):
            parts.append(s[start:i+1])
            start = i + 1

    parts.append(s[start:])

    valid = True

    for part in parts:
        if part != part[::-1]:
            valid = False
            break

    if valid:
        result.append(parts)

print(result)
