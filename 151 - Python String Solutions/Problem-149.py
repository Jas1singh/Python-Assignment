# Problem 149:

s1 = "great"
s2 = "rgeat"

if len(s1) != len(s2):
    print(False)
else:
    print(sorted(s1) == sorted(s2))
