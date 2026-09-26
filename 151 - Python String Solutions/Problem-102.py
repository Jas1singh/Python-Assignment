# Problem 102: Reverse a String Using Recursion

s = "abc"

def reverse(s):
    if len(s) == 0:
        return ""
    return reverse(s[1:]) + s[0]

print(reverse(s))
