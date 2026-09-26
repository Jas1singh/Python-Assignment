# Problem 118:

s = "banana"

longest = ""

for length in range(1, len(s)):
    seen = set()

    for i in range(len(s) - length + 1):
        sub = s[i:i+length]

        if sub in seen:
            if len(sub) > len(longest):
                longest = sub
        else:
            seen.add(sub)

print(longest)
