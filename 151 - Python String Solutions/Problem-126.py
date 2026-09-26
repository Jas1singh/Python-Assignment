# Problem 126:

s = "cat"

result = []

for i in range(len(s)):
    for j in range(len(s)):
        if j == i:
            continue

        for k in range(len(s)):
            if k == i or k == j:
                continue

            word = s[i] + s[j] + s[k]

            if word not in result:
                result.append(word)

print(result)
