# Problem 91:

s1 = "aab"
s2 = "axy"
s3 = "aaxaby"

def is_interleaving(s1, s2, s3):

    if len(s1) + len(s2) != len(s3):
        return False

    i = 0
    j = 0

    for ch in s3:

        if i < len(s1) and ch == s1[i]:
            i += 1

        elif j < len(s2) and ch == s2[j]:
            j += 1

        else:
            return False

    return i == len(s1) and j == len(s2)


print(is_interleaving(s1, s2, s3))
