# Problem 86:

s = "ab"

def permutation(s, ans=""):
    if len(s) == 0:
        print(ans)
        return

    for i in range(len(s)):
        permutation(s[:i] + s[i+1:], ans + s[i])

permutation(s)
