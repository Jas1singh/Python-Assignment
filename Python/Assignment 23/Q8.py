# Assignment 23
''' Question 8 : Intelligent Search Query Compressor

A search engine company wants to compress user queries.

## Rules:

* Count frequency of each character
* Display characters in sorted order
* Ignore spaces
* Case insensitive

### Input:

```text
Google Search
```

### Output:

```text
a1c1e2g2h1l1o2r1s1t1
```
'''


s = input().lower().replace(" ", "")

done = ""

for ch in sorted(s):
    if ch not in done:
        print(ch + str(s.count(ch)), end="")
        done += ch