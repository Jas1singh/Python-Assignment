# Problem 111:

s = "aabbc"

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

odd = 0

for value in count.values():
    if value % 2 != 0:
        odd += 1

print(odd <= 1)
