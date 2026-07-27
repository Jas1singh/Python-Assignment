# Assignment 23
''' Question 5 : Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:

```text
aabcbcdbca
```

### Output:

```text
dbca
```

### Explanation:

`dbca` contains all unique characters: a,b,c,d
'''


s = input()

unique = ""
for ch in s:
    if ch not in unique:
        unique += ch

need = len(unique)

ans = s

for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        if s[j] not in temp:
            temp += s[j]
        if len(temp) == need:
            if len(s[i:j+1]) < len(ans):
                ans = s[i:j+1]
            break

print(ans)
