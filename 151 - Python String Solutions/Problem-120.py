# Problem 120:

s = "abaeiouy"

vowels = "aeiou"
longest = ""
current = ""

for ch in s:
    if ch in vowels:
        current += ch

        if len(current) > len(longest):
            longest = current
    else:
        current = ""

print(longest)
