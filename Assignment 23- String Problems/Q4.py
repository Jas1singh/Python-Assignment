# Assignment 23
''' Question 4 : Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

```text
file file image file image data
```

### Output:

```text
file file(1) image file(2) image(1) data
```
'''


s = input()

names = s.split()

result = ""

for i in range(len(names)):
    c = 0
    for j in range(i):
        if names[i] == names[j]:
            c += 1

    if c == 0:
        result += names[i]
    else:
        result += names[i] + "(" + str(c) + ")"

    if i != len(names) - 1:
        result += " "

print(result)