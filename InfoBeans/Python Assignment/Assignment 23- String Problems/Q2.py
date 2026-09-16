# Assignment 23
''' Question 2 : AI Auto-Correct Consecutive Word Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

### Input:

```text
hello hello hello team meeting meeting started
```

### Output:

```text
hello team meeting started
```
'''


s = input()

words = s.split()

result = words[0]

for i in range(1, len(words)):
    if words[i] != words[i - 1]:
        result += " " + words[i]

print(result)