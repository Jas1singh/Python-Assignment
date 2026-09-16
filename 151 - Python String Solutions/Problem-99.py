# Problem 99:

s = "azzb"

found = False

for i in range(1, len(s) - 1):

    if s[i] == 'z':
        if s[i - 1] == s[i + 1]:
            found = True
            break

print(found)
