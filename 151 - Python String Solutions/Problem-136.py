# Problem 136:

s1 = "pale"
s2 = "ple"

if abs(len(s1) - len(s2)) > 1:
    print(False)
else:

    i = 0
    j = 0
    diff = 0

    while i < len(s1) and j < len(s2):

        if s1[i] != s2[j]:
            diff += 1

            if diff > 1:
                break

            if len(s1) > len(s2):
                i += 1
                continue

            elif len(s2) > len(s1):
                j += 1
                continue

        i += 1
        j += 1

    if i < len(s1) or j < len(s2):
        diff += 1

    print(diff == 1)
