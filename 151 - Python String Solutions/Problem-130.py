# Problem 130:

s = "a b a c a"

words = s.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

maximum = 0
answer = ""

for word in count:
    if count[word] > maximum:
        maximum = count[word]
        answer = word

print(answer)
