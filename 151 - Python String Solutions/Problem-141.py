# Problem 141:

text = "abcxabc"
pattern = "abc"

m = len(pattern)
n = len(text)

base = 256
prime = 101

pattern_hash = 0
text_hash = 0
power = 1

for i in range(m - 1):
    power = (power * base) % prime

for i in range(m):
    pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
    text_hash = (base * text_hash + ord(text[i])) % prime

result = []

for i in range(n - m + 1):

    if pattern_hash == text_hash:

        if text[i:i+m] == pattern:
            result.append(i)

    if i < n - m:
        text_hash = (
            base * (text_hash - ord(text[i]) * power)
            + ord(text[i+m])
        ) % prime

        if text_hash < 0:
            text_hash += prime

print(result)
