# Problem 137:

s = "eceba"
k = 2

left = 0
maximum = 0
answer = ""

count = {}

for right in range(len(s)):

    count[s[right]] = count.get(s[right], 0) + 1

    while len(count) > k:
        count[s[left]] -= 1

        if count[s[left]] == 0:
            del count[s[left]]

        left += 1

    if right - left + 1 > maximum:
        maximum = right - left + 1
        answer = s[left:right+1]

print(maximum)
print(answer)
