# Problem 60:  Append two strings but remove adjacent duplicates.

s1 = input("Enter the S1 :")
s2 = input("Enter the S2 :")

s = s1 + s2

unique = ""

for i in range(len(s)):
    if i+1<len(s) and s[i]==s[i+1]:
        continue
    else:
        unique = unique + s[i]

print(unique)        



