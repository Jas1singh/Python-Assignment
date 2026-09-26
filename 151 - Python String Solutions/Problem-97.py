# Problem 97: Check if two given strings appear at the end of each other (ignoring case).

s1 = "abc"
s2 = "Xabc"

s1 = s1.lower()
s2 = s2.lower()

if s1 in s2 or s2 in s1:
    print(True)
else:
    print(False)
