# Problem 119:

s = "aeiouy"

vowels = "aeiou"
answer = ""

for i in range(len(s)):
    seen = set()

    for j in range(i, len(s)):
        if s[j] in vowels:
            seen.add(s[j])

        if len(seen) == 5:
            current = s[i:j+1]

            if answer == "" or len(current) < len(answer):
                answer = current

            break

print(answer)
