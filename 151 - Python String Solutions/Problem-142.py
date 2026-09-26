# Problem 142:

text = "aabaaab"
pattern = "aab"

combined = pattern + "$" + text

z = [0] * len(combined)

left = 0
right = 0

for i in range(1, len(combined)):

    if i <= right:
        z[i] = min(right - i + 1, z[i-left])

    while (
        i + z[i] < len(combined)
        and combined[z[i]] == combined[i + z[i]]
    ):
        z[i] += 1

    if i + z[i] - 1 > right:
        left = i
        right = i + z[i] - 1

result = []

for i in range(len(combined)):
    if z[i] == len(pattern):
        result.append(i - len(pattern) - 1)

print(result)
