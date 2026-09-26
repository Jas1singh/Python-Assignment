# Problem 101:  Valid Palindrome

s = "A man, a plan, a canal: Panama"

s = s.lower()
t = ""

for ch in s:
    if ch.isalnum():
        t += ch

if t == t[::-1]:
    print(True)
else:
    print(False)


