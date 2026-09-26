# Problem 110:

s = "banana"
k = 3

largest = s[0:k]

for i in range(1, len(s) - k + 1):
    current = s[i:i+k]

    if current > largest:
        largest = current

print(largest)
