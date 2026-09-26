# Problem 107:

s = "The quick brown fox jumps over the lazy dog"

s = s.lower()
letters = set()

for ch in s:
    if 'a' <= ch <= 'z':
        letters.add(ch)

print(len(letters) == 26)
