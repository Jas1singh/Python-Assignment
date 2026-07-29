# Assignment 23
''' Question 7 : Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

## Conditions:

* Minimum 10 characters
* At least:

  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:

```text
Pyth@n1234
```

### Output:

```text
Strong Password
```

### Input:

```text
Paaass@12
```

### Output:

```text
Weak Password
```
'''


s = input()

upper = lower = digit = special = False
repeat = False

specials = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/`~"

for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        upper = True
    elif 'a' <= s[i] <= 'z':
        lower = True
    elif '0' <= s[i] <= '9':
        digit = True
    elif s[i] in specials:
        special = True

    if i < len(s) - 1 and s[i] == s[i + 1]:
        repeat = True

if len(s) >= 10 and upper and lower and digit and special and not repeat and " " not in s:
    print("Strong Password")
else:
    print("Weak Password")