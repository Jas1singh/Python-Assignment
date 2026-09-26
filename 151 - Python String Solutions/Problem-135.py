# Problem 135:

s1 = "pale"
s2 = "ple"

if len(s1) != len(s2):
    print(False)
else:
    diff = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1

    print(diff == 1)
