# Problem 95:

s = "aabbccdde"

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

highest = 0
second = 0

for ch in frequency:
    if frequency[ch] > highest:
        second = highest
        highest = frequency[ch]

    elif frequency[ch] > second and frequency[ch] < highest:
        second = frequency[ch]

for ch in frequency:
    if frequency[ch] == second:
        print(ch)
