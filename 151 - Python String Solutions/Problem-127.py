# Problem 127:

arr = ["eat", "tea", "tan", "ate", "nat"]

groups = {}

for word in arr:
    key = "".join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print(list(groups.values()))
