# Problem 117:

s = "ababa"

found = False

for length in range(1, len(s)):
    seen = set()

    for i in range(len(s) - length + 1):
        sub = s[i:i+length]

        if sub in seen:
            print(True)
            print("Duplicate:", sub)
            found = True
            break

        seen.add(sub)

    if found:
        break

if not found:
    print(False)
