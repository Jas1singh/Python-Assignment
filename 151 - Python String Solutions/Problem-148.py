# Problem 148:

s = "abcab"
k = 2

seen = set()
answer = ""

for i in range(len(s) - k + 1):

    sub = s[i:i+k]

    if sub in seen:
        answer = sub
        break

    seen.add(sub)

print(answer)
