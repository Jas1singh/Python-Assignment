# Assignment 23
''' Question 1 : Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.
To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

```text
abcabcbb
```

Output:

```text
abc
```
'''


s = input()

ans = ""

for length in range(len(s) - 1, 0, -1):
    found = False
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        if s.count(sub) > 1:
            ans = sub
            found = True
            break
    if found:
        break

print(ans)
