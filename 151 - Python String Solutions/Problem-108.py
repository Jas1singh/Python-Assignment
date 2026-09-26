# Problem 108:

s = "ambidextrous"

s = s.lower()
seen = set()
valid = True

for ch in s:
    if ch in seen:
        valid = False
        break
    seen.add(ch)

print(valid)
