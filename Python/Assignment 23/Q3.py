# Assignment 23
''' Question 3 : Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

```text
No unique digit found
```

### Input:

```text
A122334455667789
```

### Output:

```text
8
```
'''


s = input()

found = False

for ch in s:
    if ch.isdigit() and s.count(ch) == 1:
        print(ch)
        found = True
        break

if not found:
    print("No unique digit found")