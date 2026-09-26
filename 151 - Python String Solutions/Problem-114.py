# Problem 114:

s1 = "ace"
s2 = "abcde"

i = 0

for ch in s2:
    if i < len(s1) and s1[i] == ch:
        i += 1

print(i == len(s1))
