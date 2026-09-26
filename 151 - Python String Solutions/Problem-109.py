# Problem 109:

s = "banana"
k = 3

smallest = s[0:k]

for i in range(1, len(s) - k + 1):
    current = s[i:i+k]

    if current < smallest:
        smallest = current

print(smallest)
