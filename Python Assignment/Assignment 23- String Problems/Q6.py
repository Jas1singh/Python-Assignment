# Assignment 23
''' Question 6 : AI Chat Toxic Pattern Detector

An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

If found:

```text
Spam Pattern Found
```

Else:

```text
Clean Message
```

### Input:

```text
heyyy broooo welcome
```

### Output:

```text
Spam Pattern Found
```
'''

s = input()

found = False

for i in range(len(s) - 2):
    if s[i] == s[i + 1] == s[i + 2]:
        found = True
        break

if found:
    print("Spam Pattern Found")
else:
    print("Clean Message")