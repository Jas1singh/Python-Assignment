# Problem 96:

s = "a b a c b"

words = s.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

highest = 0
second = 0

for word in frequency:
    if frequency[word] > highest:
        second = highest
        highest = frequency[word]

    elif frequency[word] > second and frequency[word] < highest:
        second = frequency[word]

for word in frequency:
    if frequency[word] == second:
        print(word)
