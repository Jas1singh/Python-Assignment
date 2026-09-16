# Problem 87:

s = "aab"

def permutation(s, ans=""):
    if len(s) == 0:
        print(ans)
        return

    used = []

    for i in range(len(s)):
        if s[i] not in used:
            used.append(s[i])
            permutation(s[:i] + s[i+1:], ans + s[i])

permutation(s)
