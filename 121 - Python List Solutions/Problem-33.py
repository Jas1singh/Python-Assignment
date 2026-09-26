#''' Problem 33: '''

nums = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

frequency = []

for num in nums:
    found = False

    for item in frequency:
        if item[0] == num:
            item[1] += 1
            found = True
            break

    if found == False:
        frequency.append([num, 1])

# Sort according to frequency
for i in range(len(frequency)):
    for j in range(i + 1, len(frequency)):
        if frequency[i][1] < frequency[j][1]:
            frequency[i], frequency[j] = frequency[j], frequency[i]

result = []

for i in range(k):
    result.append(frequency[i][0])

print("Top", k, "frequent elements:", result)
