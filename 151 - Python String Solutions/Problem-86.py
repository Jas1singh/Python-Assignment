# Problem 86: Print all permutations of a string without repetition.

s = "ab"

def permutation(s, ans=""):
    if len(s) == 0:
        print(ans)
        return

    for i in range(len(s)):
        permutation(s[:i] + s[i+1:], ans + s[i])

permutation(s)
