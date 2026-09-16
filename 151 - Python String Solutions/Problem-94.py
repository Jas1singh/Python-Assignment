# Problem 94:

s1 = "ADOBECODEBANC"
s2 = "ABC"

best = ""

for i in range(len(s1)):

    temp = ""

    for j in range(i, len(s1)):
        temp += s1[j]

        found = True

        for ch in s2:
            if ch not in temp:
                found = False
                break

        if found:
            if best == "" or len(temp) < len(best):
                best = temp
            break

print(best)
