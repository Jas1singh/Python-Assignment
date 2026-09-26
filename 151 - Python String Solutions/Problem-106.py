# Problem 106:

s = "ab"

for i in range(1 << len(s)):
    sub = ""

    for j in range(len(s)):
        if i & (1 << j):
            sub += s[j]

    print(sub)
